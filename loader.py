import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Token del bot (¡NO lo compartas públicamente!)
BOT_TOKEN = "TU_TOKEN_AQUI"

# ID del chat donde enviar el mensaje
CHAT_ID = -1002474159521  # Reemplázalo con el ID correcto

# Crear el bot y el dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def send_message():
    """Envia un mensaje al grupo de Telegram"""
    await bot.send_message(CHAT_ID, "Este es un mensaje enviado desde mi bot.", parse_mode="HTML")

async def main():
    """Ejecuta la función de envío de mensaje y cierra el bot correctamente"""
    await send_message()
    await bot.session.close()

# Ejecutar la función principal
if __name__ == "__main__":
    asyncio.run(main())
