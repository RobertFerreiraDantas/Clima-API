import requests
import pyodbc
from dotenv import load_dotenv
import os
from flask import Flask

app = Flask(__name__)  


load_dotenv()


conexao = pyodbc.connect(
    f"DRIVER={os.getenv('DB_DRIVER')};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"PORT={os.getenv('DB_PORT')};"   
    f"DATABASE={os.getenv('DB_DATABASE')};"
    f"USER={os.getenv('DB_USER')};"
    f"PASSWORD={os.getenv('DB_PASSWORD')};"
)
cursor = conexao.cursor()

cursor.execute("TRUNCATE TABLE clima_cidade")
conexao.commit()

for i in range(3):
    cidades = [455825, 455833, 455824]

    def extracao():
        url = f"https://api.hgbrasil.com/weather?key={os.getenv('API_KEY')}&woeid={cidades[i]}"

        dados = requests.get(url)
        dados = dados.json()

        return dados

    def transforma_dados(dados):
        cidade = dados["results"]["city_name"]
        data = dados["results"]["date"]
        descricao = dados["results"]["description"]
        temperatura = dados["results"]["temp"]
        hora = dados["results"]["time"]

        dados_transformados = {
            "cidade": cidade,
            "data": data,
            "descricao": descricao,
            "temperatura": temperatura,
            "hora": hora

        }

        colunas = ", ".join(dados_transformados.keys())
        marcadores = ", ".join(["?"] * len(dados_transformados))
        query = f"INSERT INTO clima_cidade ({colunas}) VALUES ({marcadores})"
        cursor.execute(query, tuple(dados_transformados.values()))
        conexao.commit()

        return dados_transformados

    if __name__ == "__main__":
        dado = extracao()
        dado_tratado = transforma_dados(dado)


cursor.close()
conexao.close()
