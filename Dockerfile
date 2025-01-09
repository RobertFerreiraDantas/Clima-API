FROM python:3.11-slim


RUN apt-get update && apt-get install -y odbc-postgresql unixodbc


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt


CMD ["gunicorn", "Producao:app"]