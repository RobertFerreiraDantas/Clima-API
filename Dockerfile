FROM python:3.12.3-slim

WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


ENV FLASK_APP=Producao.py


COPY . .


CMD ["python", "Producao.py"]

