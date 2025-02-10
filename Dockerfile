FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias

RUN python3 -m ensurepip && python3 -m pip install --upgrade pip

# Asegurar que pip está actualizado antes de instalar dependencias
RUN python3 -m pip3 install --upgrade pip

# Instalar aiogram manualmente antes de leer requirements.txt
RUN python3 -m pip3 install aiogram==3.13.1

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar dependencias de Python sin caché
RUN python3 -m pip3 install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python3", "loader.py"]
