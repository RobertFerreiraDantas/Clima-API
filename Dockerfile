FROM python:3.12.3-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 10000


COPY . .


CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10000", "Producao:app"]


