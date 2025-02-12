from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode  # Aiogram 3.x usa "enums"
from aiogram.fsm.storage.memory import MemoryStorage  # Aiogram 3.x usa "fsm.storage"

BOT_TOKEN = "TU_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # En Aiogram 3.x, no se pasa "bot" aquí

dp["bot"] = bot  # Se asigna manualmente el bot al Dispatcher
