import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,KeyboardButton

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def start_message(message):
    buttons(message)


def order_buttons(message):
    order_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1_x = types.KeyboardButton("Yetkazib berish 🚘")
    button2_x = types.KeyboardButton("Olib ketish 🏃")
    button3_x = types.KeyboardButton("Orqaga  ⬅️")
    order_keyboard.add(button1_x, button2_x, button3_x)
    bot.send_message(message.from_user.id, "KATEGRIYALARDAN BIRINI TANLANG!", reply_markup=order_keyboard)


def buttons(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton("Buyurtma berish🛍")
    button2 = types.KeyboardButton("Cashback💸")
    button3 = types.KeyboardButton("Tadbirlar🎉")
    button4 = types.KeyboardButton("Fikr bildirish✍️")
    button5 = types.KeyboardButton("Ma`lumotℹ️")
    button6 = types.KeyboardButton("Sozlamalar⚙️")
    keyboard.add(button1)
    keyboard.add(button2, button3)
    keyboard.add(button4, button5)
    keyboard.add(button6)
    bot.send_message(message.from_user.id, "KATEGRIYALARDAN BIRINI TANLANG!", reply_markup=keyboard)


def geolocation(message):
    keyboard_location = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Joylashuvni jo`natish📍", request_location=True)
    button_check1 = types.KeyboardButton(text="Tasdiqlash ✅", request_location=False)
    button_check2 = types.KeyboardButton(text="Ortga ⬅️", request_location=False)
    keyboard_location.add(button_geo, button_check1,button_check2)
    bot.send_message(message.from_user.id, "Buyurtmangizni qaerga yetkazib berish kerak 🚙? Agar lokatsiyangizni📍 "
                                           "yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini "
                                           "aniqlaymiz 💵", reply_markup=keyboard_location)


def shaxobcha(message):
    keyboard_shaxobcha = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="📍 Eng yaqin shaxobchamizni aniqlash", request_location=True)
    button_x = types.KeyboardButton(text="⬅️ Orqaga")
    keyboard_shaxobcha.add(button_1, button_x)
    bot.send_message(message.from_user.id, "GEOJOYLASHUVNI YUBORING!", reply_markup=keyboard_shaxobcha)


@bot.message_handler(content_types=["location"])
def location(message):
    global latitude1
    if message.location is not None:
        # print(message.location)
        # print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        # latitude1 = f"{message.location.latitude}"
        # longtitude1 = f"{message.location.longitude}"
        latitude1 = message.location


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "Buyurtma berish🛍":
        order_buttons(message)
    elif message.text == "Yetkazib berish 🚘":
        geolocation(message)
    elif message.text == "Olib ketish 🏃":
        shaxobcha(message)
    elif message.text=="⬅️ Orqaga":
        order_buttons(message)
    elif message.text=="Ortga ⬅":
        order_buttons(message)
    elif message.text=="Tasdiqlash ✅":
        #tasdiqlash(message)
        reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        reply_markup.add(*[
            KeyboardButton(text="📥 Savat"),
            KeyboardButton(text="🍱Setlar"),
            KeyboardButton(text="🌯 Lesterlar"),
            KeyboardButton(text="🍗 Tovuqcha"),
            KeyboardButton(text="🚘 Buyurtma berish"),
            KeyboardButton(text="🍔 Burgerlar"),
            KeyboardButton(text="🌭 Longer/Hot-dog"),
            KeyboardButton(text="🍟 Sneklar"),
        ])
        bot.send_message(message.from_user.id, "10:00 - 22:00 - 1 km gacha bo’lgan buyurtmalar yetkazish narxi 5000 so’m "
                                           "10:00 - 22:00 - 3 km gacha 9000 so’m keyingi har 1 km uchun -1000 sum "
                                           "Toshkent shahri bo’ylab.\n\n Nimadan boshlaymiz?",
                         reply_markup=reply_markup)
    elif message.text=="Ortga ⬅️":
        order_buttons(message)




bot.polling(none_stop=True)
