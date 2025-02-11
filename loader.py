from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("API_TOKEN")

# Inicialización del bot
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)

# Crear la aplicación, que contiene al bot y al dispatcher
from aiogram import F
from aiogram import Application

application = Application.builder().token(API_TOKEN).build()

# Aquí registramos los manejadores
# Por ejemplo, un comando simple de inicio
async def cmd_start(message: types.Message):
    await message.answer("¡Hola! Soy un bot.")

# Registro de manejadores
application.add_handler(types.CommandHandler("start", cmd_start))

# Ejecutar el bot
if __name__ == "__main__":
    executor.start_polling(application, skip_updates=True)
