import os
from aiogram import Bot, Dispatcher

# Токен берём из секрета GitHub
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)