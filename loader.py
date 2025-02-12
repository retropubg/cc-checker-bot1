from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# Token de tu bot
bot = Bot(token="8048311747:AAGyGx8dCxU3zsDsct5Hd6T6Ign5G6gVq6Y")
dp = Dispatcher(bot, storage=MemoryStorage())  # Dispatcher centralizado

# Función para registrar todos los handlers
def register_all_handlers():
    from handlers.bin_info import register_handlers  # Importar y registrar
    from handlers.mchk import register_handlers
    from handlers.admin import register_handlers
    from handlers.sk import register_handlers
    from handlers.ssh import register_handlers
    from handlers.callback import register_handlers
    from handlers.pp import register_handlers
    from handlers.scrape import register_handlers

    register_handlers(dp)  # Registra los handlers de cada módulo
