FROM python:3.8-slim

WORKDIR /app

# Cambiar al usuario root explícitamente
USER root

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Asegurar que pip esté actualizado
RUN python3 -m ensurepip && python3 -m pip install --upgrade pip

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar dependencias de Python sin caché
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python3", "main.py"]
