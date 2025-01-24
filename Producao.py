import requests
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Base, projeto_clima
import unidecode
from datetime import datetime
from flask import Flask

load_dotenv()


POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

POSTGRES_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}?sslmode=require"
)


engine = create_engine(POSTGRES_URL)
sessionLocal = sessionmaker(bind=engine)


def criar_tabela():
    Base.metadata.create_all(engine)


def extracao(woeid):
    url = f"https://api.hgbrasil.com/weather?key={os.getenv('API_KEY')}&woeid={woeid}"

    dados = requests.get(url)
    dados.encoding = 'utf-8'
    dados = dados.json()

    return dados


def transforma_dados(dados):
    cidade = dados["results"]["city_name"]
    data = datetime.strptime(dados["results"]["date"], "%d/%m/%Y").date()
    descricao = dados["results"]["description"]
    temperatura = dados["results"]["temp"]
    hora = datetime.strptime(dados["results"]["time"], "%H:%M").time()

    dados_transformados = {
        "cidade": cidade,
        "data": data,
        "descricao": descricao,
        "temperatura": temperatura,
        "hora": hora

    }

    return dados_transformados


def salvar_banco(dados):
    session = sessionLocal()
    novo_registro = projeto_clima(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()


app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo "

if __name__ == "__main__":
    try:
        for i in range(3):
            cidades = [455825, 455833, 455824]
            dado = extracao(woeid=cidades[i])
            if i == 0:
                sessio = sessionLocal()
                sessio.query(projeto_clima).delete()
                sessio.commit()
                sessio.close()
            if dado:
                dado_tratado = transforma_dados(dado)
                if dado_tratado["cidade"] == "São Paulo":
                    dado_tratado["cidade"] = unidecode.unidecode(dado_tratado["cidade"])
                salvar_banco(dado_tratado)
    except Exception as e:
        print(f"Erro :{e}")

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host="0.0.0.0", port=port)


