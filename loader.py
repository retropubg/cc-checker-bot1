from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
BOT_TOKEN = "8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # En Aiogram 3, NO se pasa bot aquí.

# Asociar el bot manualmente al dispatcher
dp["bot"] = bot
