FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV STATIC_DIR=static

CMD ["bash", "-c", "python -m app.seed && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
