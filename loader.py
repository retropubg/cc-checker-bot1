from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot
from aiogram import Dispatcher

# Crear el bot y el dispatcher
bot = Bot(token="8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y")
dp = Dispatcher(bot, storage=MemoryStorage())
