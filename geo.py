import telebot
from telebot import types
BOT_TOKEN="ozizi tokenizi yozasz"
bot=telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    geo_rus(message)

def geo_rus(message):
    keyboard_rus = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="ОТПРАВИТЬ АДРЕС", request_location=True)
    keyboard_rus.add(button_geo)
    bot.send_message(message.from_user.id, "ОТПРАВЬТЕ МЕСТОПОЛОЖЕНИЕ!", reply_markup=keyboard_rus)


@bot.message_handler(content_types=["location"])
def location(message):
    global latitude1
    if message.location is not None:
        latitude1 = message.location
        """NEXT FUNCTION next(message)"""


bot.polling(none_stop=True)