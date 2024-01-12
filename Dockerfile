# Dockerfile.server
FROM python:3.8

WORKDIR /app

COPY server.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "server:app", "--reload","--host", "0.0.0.0", "--port", "5000"]
