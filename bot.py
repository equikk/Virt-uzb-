from aiogram import types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot_code import bot, dp
import re

# Админ
OWNER_USERNAME = "yrener"

# Языки
LANGS = {
    "ru": {
        "menu": "🏠 Главное меню",
        "feedback": "📩 Связь с владельцем:",
        "server_btn": "Игровые серверы 🎮",
        "feedback_btn": "Обратная связь",
        "choose_server": "🌐 Выберите сервер:",
        "back": "⬅️ Назад",
        "ask_money": "Сколько миллионов вам нужно?",
        "payment": "💳 Оплатить",
        "selected": "✅ Вы выбрали сервер <b>{server}</b>\n{money} выбрано!"
    },
    "uz_cyrl": {
        "menu": "🏠 Асосий меню",
        "feedback": "📩 Эгаси билан боғланиш:",
        "server_btn": "O‘yin serverlari 🎮",
        "feedback_btn": "Мулоҳаза",
        "choose_server": "🌐 Серверни танланг:",
        "back": "⬅️ Орқага",
        "ask_money": "Сизга нечи миллион пул керак?",
        "payment": "💳 Тўлаш",
        "selected": "✅ Сиз <b>{server}</b> серверини танладингиз\n{money} танланди!"
    },
    "uz_lat": {
        "menu": "🏠 Asosiy menyu",
        "feedback": "📩 Egasi bilan bog‘lanish:",
        "server_btn": "O‘yin serverlari 🎮",
        "feedback_btn": "Mulohoza",
        "choose_server": "🌐 Serverni tanlang:",
        "back": "⬅️ Orqaga",
        "ask_money": "Sizga nechi million pul kerak?",
        "payment": "💳 To‘lash",
        "selected": "✅ Siz <b>{server}</b> serverini tanladingiz\n{money} tanlandi!"
    }
}

# Сохраняем выбор пользователя
user_data = {}

# Полный список серверов
servers = [
    "RED 🔴", "GREEN 🟢", "BLUE 🔵", "YELLOW 🟡", "ORANGE 🟠", "PURPLE 🟣",
    "LIME 🍋", "PINK 🌸", "CHERRY 🍒", "BLACK ⚫", "INDIGO 🔵🟣", "WHITE ⚪",
    "MAGENTA 💖", "CRIMSON ❤️", "GOLD 🟡✨", "AZURE 🌊", "PLATINUM 🪙",
    "AQUA 💧", "GRAY 🌫️", "ICE ❄️", "CHILLI 🌶️", "CHOCO 🍫", "MOSCOW 🏙️",
    "SPB 🎭", "UFA 🕌", "SOCHI 🏖️", "KAZAN 🐉", "SAMARA 🚤", "ROSTOV 🐎",
    "ANAPA 🌅", "EKATERINBURG 🏔️", "KRASNODAR 🍇", "ARZAMAS 🚜",
    "NOVOSIBIRSK ❄️🏙️", "GROZNY 🛡️", "SARATOV 🌉", "OMSK 🐻", "IRKUTSK 🐟",
    "VOLGOGRAD 🗿", "VORONEZH 🌳", "BELGOROD ⛪", "MAKHACHKALA 🏔️",
    "VLADIKAVKAZ 🦅", "VLADIVOSTOK ⚓", "KALININGRAD 🏰", "CHELYABINSK 🔧",
    "KRASNOYARSK 🌲", "CHEBOKSARY 🌸", "KHABAROVSK 🦌", "PERM 🏞️", "TULA 🏹",
    "RYAZAN 🐎", "MURMANSK 🚢", "PENZA 🌾", "KURSK 🐯", "ARKHANGELSK ⛪❄️",
    "ORENBURG 🐏", "KIROV 🎭", "KEMEROVO ⛏️", "TYUMEN ⛽", "TOLYATTI 🚗",
    "IVANOVO 👗", "STAVROPOL 🌻", "SMOLENSK 🕍", "PSKOV 🏰", "BRYANSK 🌲",
    "OREL 🦉", "YAROSLAVL 🦊", "BARNAUL 🌾", "LIPETSK 🏛️", "ULYANOVSK 🚂",
    "YAKUTSK ❄️🌬️", "TAMBOV 🌰", "BRATSK 🏞️", "ASTRAKHAN 🐟", "CHITA 🌲",
    "KOSTROMA 🏡", "VLADIMIR 🏯", "KALUGA 🌳", "N.NOVGOROD 🏛️", "TAGANROG ⚓",
    "VOLOGDA 🌨️", "TVER 🏰", "TOMSK 🎓", "IZHEVSK 🔧", "SURGUT 🏗️",
    "PODOLSK 🌆", "MAGADAN ❄️🌄", "CHEREPOVETS 🌲"
]

# ====== Здесь вставь все свои обработчики сообщений ======
# Старт, установка языка, обратная связь, игровые серверы, выбор сервера, ввод денег, назад

# 🔥 Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
