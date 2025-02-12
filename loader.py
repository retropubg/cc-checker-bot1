from aiogram import Bot, Dispatcher, types
import logging

BOT_TOKEN = 'TU_TOKEN_AQUI'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def get_chat_id(message: types.Message):
    print(f'Chat ID: {message.chat.id}')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
