FROM python:3.11-slim


RUN mkdir -p /var/lib/apt/lists/partial \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       odbc-postgresql \
       unixodbc \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


CMD ["gunicorn", "Producao:app"]
