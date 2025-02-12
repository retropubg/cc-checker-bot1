from aiogram import Bot, Dispatcher, types
from aiogram.fsm import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ParseMode
import logging

# Configuración básica
BOT_TOKEN = "8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y"
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Configuración de logging (opcional)
logging.basicConfig(level=logging.INFO)

# Definir los estados
class Form(StatesGroup):
    name = State()  # Estado para el nombre

# Comando de inicio
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("¡Hola! ¿Cuál es tu nombre?")
    await Form.name.set()  # Establece el estado 'name'

# Recibir el nombre y cambiar al siguiente estado
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer(f"¡Hola {message.text}!")
    await state.finish()  # Termina el estado

# Ejecutar el bot
if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp)
    
