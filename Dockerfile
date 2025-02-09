FROM python:3.8-buster

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

python3 -m ensurepip
python3 -m pip3 install --upgrade pip
python3 -m pip3 install --no-cache-dir -r requirements.txt


# Copiar el archivo requirements.txt
COPY requirements.txt .

# Actualizar pip e instalar las dependencias de PythonRUN python3 -m ensurepip && python3 -m pip install --upgrade pip
RUN pip3 install -U -r requirements.txt
requirements.txt

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python3", "main.py"]
