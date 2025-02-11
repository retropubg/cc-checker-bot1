from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import handlers
import time

PREFIX = "!/."

OWNER = ["6699273462"]
OWNER_NAME = "@eretro_7"
CHANNEL = "https://t.me/cyberassemble"
GROUP = "https://t.me/assemblechat"

def ok(mm):
    mg = str(mm)
    paid = open("paid.txt").read().splitlines()
    if mg in OWNER:
        return "OWNER"
    elif mg in paid:
        return "PAID"
    else:
        return "FREE"

from loader import dp, bot  # Ensure 'bot' is also imported

@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
    kk = await message.reply("<b>He</b>")
