from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode  # Aiogram 3.x usa directamente "types" para ParseMode
from aiogram.fsm.storage.memory import MemoryStorage  # Para el almacenamiento en memoria

BOT_TOKEN = "TU_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # En Aiogram 3.x, no se pasa "bot" aquí

dp["bot"] = bot  # Se asigna manualmente el bot al Dispatcher
