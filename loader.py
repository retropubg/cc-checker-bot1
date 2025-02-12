from aiogram import Bot, Dispatcher, types
from aiogram.fsm import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage  # Esto debería estar disponible en v3.x
import asyncio

BOT_TOKEN = "8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y"
CHAT_ID = -1002474159521  # Reemplázalo con el ID correcto

# Crear el bot y el dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()  # Almacenamiento en memoria para FSM
dp = Dispatcher(storage=storage)

# Manejador de comandos 'start'
@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("¡Hola! Soy tu bot. ¿En qué puedo ayudarte?", parse_mode="HTML")

# Manejador de comandos 'help'
@dp.message(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer("Puedes usar los siguientes comandos:\n/start para comenzar.\n/help para obtener ayuda.", parse_mode="HTML")

async def main():
    """Ejecuta el bot y espera a que lleguen mensajes"""
    try:
        # Inicia el bot y escucha los comandos.
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error al ejecutar el bot: {e}")
    finally:
        await bot.session.close()

# Ejecutar la función principal
if __name__ == "__main__":
    asyncio.run(main())
