from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import re

# 🔐 Токен
TOKEN = "8373353346:AAEE-OFD1tMJYSLNvI23ZNPEyCMIRjH9kug"
OWNER_USERNAME = "yrener"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

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

# Старт — выбор языка
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Русский 🇷🇺", "Ўзбекча 🇺🇿 (Кирилл)", "O‘zbekcha 🇺🇿 (Lotin)")
    await message.answer("👋 Выберите язык / Tilni tanlang:", reply_markup=kb)

# Установка языка
@dp.message_handler(lambda m: m.text.strip() in ["Русский 🇷🇺", "Ўзбекча 🇺🇿 (Кирилл)", "O‘zbekcha 🇺🇿 (Lotin)"])
async def set_language(message: types.Message):
    if "Русский" in message.text:
        lang = "ru"
    elif "Кирилл" in message.text:
        lang = "uz_cyrl"
    else:
        lang = "uz_lat"

    user_data[message.from_user.id] = {"lang": lang}
    lang_pack = LANGS[lang]

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(lang_pack["feedback_btn"])
    kb.add(lang_pack["server_btn"])
    await message.answer(lang_pack["menu"], reply_markup=kb)

# Обратная связь
@dp.message_handler(lambda m: m.from_user.id in user_data and m.text.strip() == LANGS[user_data[m.from_user.id]["lang"]]["feedback_btn"])
async def feedback(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]["lang"]
    lang_pack = LANGS[lang]

    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton("✍️ Связаться", url=f"https://t.me/{OWNER_USERNAME}")
    )
    await message.answer(lang_pack["feedback"], reply_markup=kb)

# Игровые серверы
@dp.message_handler(lambda m: m.from_user.id in user_data and m.text.strip() == LANGS[user_data[m.from_user.id]["lang"]]["server_btn"])
async def show_servers(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]["lang"]
    lang_pack = LANGS[lang]

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(servers), 2):
        kb.row(*[KeyboardButton(s.strip()) for s in servers[i:i+2]])
    kb.add(lang_pack["back"])
    await message.answer(lang_pack["choose_server"], reply_markup=kb)

# Выбор сервера
@dp.message_handler(lambda m: m.from_user.id in user_data and m.text.strip() in [s.strip() for s in servers])
async def choose_server(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]["lang"]
    lang_pack = LANGS[lang]

    user_data[user_id]["server"] = message.text.strip()
    await message.answer(lang_pack["ask_money"])

# Ввод денег
@dp.message_handler(lambda m: m.from_user.id in user_data and re.search(r"\d+", m.text))
async def ask_money(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]["lang"]
    lang_pack = LANGS[lang]

    text = message.text.lower().replace(" ", "")
    number = int(re.findall(r"\d+", text)[0])

    if "ккк" in text or "kkk" in text:
        money = f"{number} Milliard"
    elif "кк" in text or "kk" in text:
        money = f"{number} Million"
    elif number >= 1000000000:
        money = f"{number/1000000000:.1f} Milliard"
    elif number >= 1000000:
        money = f"{number/1000000:.1f} Million"
    else:
        money = f"{number}"

    server = user_data[user_id].get("server", "❓")
    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton(lang_pack["payment"], url=f"https://t.me/{OWNER_USERNAME}")
    )
    await message.answer(
        lang_pack["selected"].format(server=server, money=money),
        reply_markup=kb
    )

# Назад
@dp.message_handler(lambda m: m.from_user.id in user_data and m.text.strip() == LANGS[user_data[m.from_user.id]["lang"]]["back"])
async def back_to_menu(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]["lang"]
    lang_pack = LANGS[lang]

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(lang_pack["feedback_btn"])
    kb.add(lang_pack["server_btn"])
    await message.answer(lang_pack["menu"], reply_markup=kb)

# 🔥 Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)