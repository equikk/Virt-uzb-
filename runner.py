from aiogram import executor
from bot_code import dp

print("Бот запускается...")
executor.start_polling(dp, skip_updates=True)