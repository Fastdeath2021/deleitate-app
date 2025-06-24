# Usa una imagen base
FROM python:3.10-slim

WORKDIR /app

# Copia requirements e instala
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el backend
COPY backend/ .

EXPOSE 5000

CMD ["python", "app.py"]
