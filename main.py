import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import handlers
import time
from loader import dp, bot  # Asegúrate de que 'bot' esté importado correctamente

# Configuración
PREFIX = "!/."
OWNER = ["6699273462"]
OWNER_NAME = "@eretro_7"
CHANNEL = "https://t.me/cyberassemble"
GROUP = "https://t.me/assemblechat"

# Función para verificar usuarios
def ok(mm):
    mg = str(mm)
    paid = open("paid.txt").read().splitlines()
    if mg in OWNER:
        return "OWNER"
    elif mg in paid:
        return "PAID"
    else:
        return "FREE"

# Manejador de comandos
@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
    await message.reply("<b>He</b>", parse_mode="HTML")

# Iniciar el bot
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
