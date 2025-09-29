import time
from aiogram import executor
from bot_code import dp  # импорт Dispatcher из bot_code.py

while True:
    try:
        print("Бот запускается...")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print("Ошибка! Перезапуск через 10 секунд:", e)
        time.sleep(10)