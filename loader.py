from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "7020048572:AAG5bV9yhIk4DVw3ynUo-j9GHS743f9xVyA"

# Crear el objeto bot sin parse_mode
bot = Bot("7020048572:AAG5bV9yhIk4DVw3ynUo-j9GHS743f9xVyA")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Asignar el bot manualmente
dp["bot"] = bot

# Ejemplo de envío de mensaje con parse_mode
async def send_message():
    await bot.send_message(chat_id="TU_CHAT_ID", text="Este es un <b>mensaje HTML</b>", parse_mode="HTML")
