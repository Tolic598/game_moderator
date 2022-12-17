from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5018144842:AAHmknEVURWrdtgLXJ6d4ol9PVlYwEvLN2w'
storage=MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)