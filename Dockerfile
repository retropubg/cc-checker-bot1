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
    curl \
    && rm -rf /var/lib/apt/lists/*


# Regresar al directorio principal para el código de Python
WORKDIR /app

# Asegurar que pip esté actualizado
RUN python3 -m ensurepip && python3 -m pip install --upgrade pip

# Copiar el archivo requirements.txt de Python
COPY requirements.txt .

# Instalar dependencias de Python sin caché
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de Python
COPY . .


# Comando para ejecutar tanto Python como Express al mismo tiempo
CMD ["python3", "loader.py"]
