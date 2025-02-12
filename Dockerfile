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

# Instalar Node.js y npm (para Express)
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Verificar que Node.js y npm se hayan instalado correctamente
RUN node -v && npm -v

# Crear un directorio para la aplicación Node.js
WORKDIR /app/node

# Inicializar npm y crear package.json
RUN npm init -y

# Instalar Express
RUN npm install express

# Crear un archivo de servidor Express básico
RUN echo "const express = require('express');\n\
const app = express();\n\
const port = 3000;\n\
app.get('/', (req, res) => {\n\
  res.send('¡Hola desde Express!');\n\
});\n\
app.listen(port, () => {\n\
  console.log(`Servidor Express escuchando en http://localhost:${port}`);\n\
});" > app.js

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

# Exponer el puerto para Express y Python
EXPOSE 3000 8000

# Comando para ejecutar tanto Python como Express al mismo tiempo
CMD ["sh", "-c", "python3 loader.py & node /app/node/app.js"]
