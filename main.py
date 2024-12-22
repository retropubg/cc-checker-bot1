from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import handlers
import time


PREFIX = "!/."


OWNER = ["5136746907"]

OWNER_NAME = "@I_M_R_A_S"

CHANNEL = "https://t.me/cyberassemble"

GROUP = "https://t.me/assemblechat"

def ok(mm):
  mg = str(mm)
  paid = open("paid.txt").read().splitlines()
  if mg in OWNER:
    user = "OWNER"
    return user
  elif mg in paid:
    user = "PAID"
    return user
  elif mg not in paid:
    user = "FREE"
    return user
  else:
    user = "FREE"
    return user

from loader import dp


@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
  kk = await message.reply("<b> Hello, I'm cc checker  Bot made by Cyber Assamble</b>")
  time.sleep(2)
  seconds = time.time()
  local_time = time.ctime(seconds)
  await kk.edit_text(
    f"""<b> Hello  @{message.from_user.username} \Welcome to cc Checker bot  : {local_time} \To see all the commands send /cmds \n By the way your UserID is <code> {message.from_user.id} </code>\n Bot by: </b> <a href='https://t.me/cyberassemble'><b>CYBER ASSEMBLE </b></a>""",
    disable_web_page_preview=True)



if __name__ == '__main__':

  executor.start_polling(dp, skip_updates=True)
