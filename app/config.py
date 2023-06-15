from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN_API = "6112226257:AAEwsiAj5GohAAv9ITTg0MqcWuF0tKUAALk"
bot = Bot(token=TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Конфигурация
