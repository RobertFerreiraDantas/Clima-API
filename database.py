from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class projeto_clima(Base):
    __tablename__ = "clima_das_cidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cidade = Column(String)
    data = Column(DateTime)
    descricao = Column(String)
    temperatura = Column(Integer)
    hora = Column(DateTime)
