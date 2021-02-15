import telebot
import json
from telebot import types

savatx = {}
savat1 = []
c = {}
bot = telebot.TeleBot("1340272262:AAH3XgBU08irFeU5t5529P3YMb-QIHhEhG0")


def ruscha_otvet(message):
    bot.reply_to(message, "ВЫ ВЫБИРАЛИ РУССКОГО ЯЗЫКА! 🇷🇺")


def rus_knopkalari(message):
    rus_knopkalari = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    knopka1 = types.KeyboardButton("Заказать 🥡")
    knopka2 = types.KeyboardButton("Параметры ⚙️")
    knopka3 = types.KeyboardButton("Оставить комментарий 📝")
    knopka4 = types.KeyboardButton("Назад ◀️")
    rus_knopkalari.add(knopka1, knopka2, knopka3, knopka4)
    bot.send_message(message.from_user.id, "ВЫБЕРИТЕ ОДНУ ИЗ КАТЕГОРИЙ!", reply_markup=rus_knopkalari)


def pizzi(message):
    print(message)
    pizza_knopka = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    pizza_1 = types.KeyboardButton("КОМБО ПИЦЦА 🏵")
    pizza_2 = types.KeyboardButton("ПИЦЦА ШАШЛЫК ️🍢")
    pizza_3 = types.KeyboardButton("КУРИННАЯ БАРБЕКЮ 🐥")
    pizza_4 = types.KeyboardButton("НАЗАД 🔙")
    pizza_5 = types.KeyboardButton("ПОСМОТРЕТЬ КОРЗИНУ 🗑")
    pizza_knopka.add(pizza_1, pizza_2, pizza_3, pizza_4, pizza_5)
    bot.send_message(message.from_user.id, "ПИЦЦА ЖДУТ ВАС! ☺☺️☺️☺️", reply_markup=pizza_knopka)

def soni_rus(message):
    nomeri_rus = types.InlineKeyboardMarkup(row_width=3)
    nomer_1 = types.InlineKeyboardButton(text="1", callback_data="odin")
    nomer_2 = types.InlineKeyboardButton(text="2", callback_data="dva")
    nomer_3 = types.InlineKeyboardButton(text="3", callback_data="tri")
    nomer_4 = types.InlineKeyboardButton(text="4", callback_data="chetiri")
    nomer_5 = types.InlineKeyboardButton(text="5", callback_data="pyat")
    nomer_6 = types.InlineKeyboardButton(text="6", callback_data="shest")
    nomer_7 = types.InlineKeyboardButton(text="7", callback_data="sem")
    nomer_8 = types.InlineKeyboardButton(text="8", callback_data="vosem")
    nomer_9 = types.InlineKeyboardButton(text="9", callback_data="devet")
    nomeri_rus.add(nomer_1, nomer_2, nomer_3, nomer_4, nomer_5, nomer_6, nomer_7, nomer_8, nomer_9)
    bot.send_message(message.from_user.id, text="ВЫБЕРИТЕ КОЛИЧЕСТВУ!", reply_markup=nomeri_rus)

def parametri(message):
    db = get_db()
    if db:
        for user in db:
            try:
                if user['user_id'] == message.from_user.id:
                    ID = user['user_id']
                    ISMI = user['first_name']
                    NOMERI = user['tel_number']
                    # QUESTION=str(ISMI)+str(ID)+str(NOMERI)
                    INFO = "ВАШЕ ИМЯ: " + str(ISMI) + '\n' + "ВАШ ID: " + str(
                        ID) + '\n' + "ВАШ НОМЕР: " + str(NOMERI)
                    print(ID, ISMI, NOMERI)
                    bot.send_message(message.from_user.id, INFO)
            except KeyError:
                return None


def get_db():
    with open('data.json', 'r') as f:
        return json.load(f)


def get_user_from_db(user_id):
    db = get_db()
    if db:
        for user in db:
            try:
                if user['user_id'] == user_id:
                    return user_id
            except KeyError:
                return None
    return None


def set_user_to_db(user_id, first_name, tel_number):
    db = get_db()
    data = {'user_id': user_id, 'first_name': first_name, 'tel_number': tel_number}
    db.append(data)
    with open('data.json', 'w+') as f:
        json.dump(db, f)
