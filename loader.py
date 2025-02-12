import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Token del bot (¡NO lo compartas públicamente!)
BOT_TOKEN = "8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y"

# ID del chat donde enviar el mensaje
CHAT_ID = -1002262720445  # Reemplázalo con el ID correcto

# Crear el bot y el dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def send_message():
    """Envia un mensaje al grupo de Telegram"""
    try:
        await bot.send_message(CHAT_ID, "Este es un mensaje enviado desde mi bot.", parse_mode="HTML")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
    finally:
        await bot.session.close()  # Cierra la sesión correctamente

async def main():
    """Ejecuta la función de envío de mensaje"""
    await send_message()

# Ejecutar la función principal
if __name__ == "__main__":
    asyncio.run(main())
