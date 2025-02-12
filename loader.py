from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage  # Almacenamiento en memoria

BOT_TOKEN = "7020048572:AAG5bV9yhIk4DVw3ynUo-j9GHS743f9xVyA"

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")  # Solo usa "HTML" directamente, sin ParseMode
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # En Aiogram 3.x, el bot se asigna manualmente al Dispatcher

dp["bot"] = bot  # Asignamos el bot manualmente al Dispatcher en Aiogram 3.x
