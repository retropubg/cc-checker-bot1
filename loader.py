from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
BOT_TOKEN = '7851924299:AAEj70SJUOzeS5w-GHUpUiK-GiPV1CHRaSE'
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
