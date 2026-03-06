FROM python:3.11-slim

# Evita que Python genere archivos .pyc y permite que los logs fluyan en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos dependencias primero para aprovechar la caché de capas de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# El puerto 8000 se mantiene como referencia, pero el CMD lo hará dinámico
EXPOSE 8000

# Quitamos --reload (no se recomienda en producción) y usamos la variable $PORT
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]