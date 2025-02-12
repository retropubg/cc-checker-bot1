from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Sustituye esto con tu token real
BOT_TOKEN = "7020048572:AAG5bV9yhIk4DVw3ynUo-j9GHS743f9xVyA"

# ID del chat donde quieres enviar el mensaje
CHAT_ID = -1002474159521  # Reemplaza con el ID de tu chat

# Crear el objeto bot
bot = Bot(token=BOT_TOKEN)

# Configurar el almacenamiento de FSM
storage = MemoryStorage()

# Crear el Dispatcher
dp = Dispatcher(storage=storage)
dp["bot"] = bot

# Función asincrónica para enviar un mensaje
async def send_message():
    # Enviar mensaje al grupo
    await bot.send_message(CHAT_ID, "Este es un mensaje enviado desde mi bot.", parse_mode="HTML")
