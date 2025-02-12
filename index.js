const express = require('express');
const app = express();

// Definir el puerto desde la variable de entorno PORT, o 3000 por defecto
const port = process.env.PORT || 3000;

// Ruta básica para verificar si el servidor está funcionando
app.get('/', (req, res) => {
  res.send('¡Hola, mundo! El servidor está funcionando.');
});

// Hacer que el servidor escuche en el puerto especificado
app.listen(port, '0.0.0.0', () => {
  console.log(`Servidor funcionando en http://0.0.0.0:${port}`);
});
