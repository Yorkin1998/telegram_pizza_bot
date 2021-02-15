from RUSSIAN import *
import json

bot = telebot.TeleBot("1340272262:AAH3XgBU08irFeU5t5529P3YMb-QIHhEhG0")

a = ''
savatx = {}
savat1 = []
c = {}
listToStr = ""
pizza_name = ''
text_of_savat = []


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id_from_db = get_user_from_db(message.from_user.id)
    if user_id_from_db:
        bot.send_message(message.from_user.id, "SIZ OLDIN REGISTRATSIYA QILGANSIZ!😊")
        languages(message)
    else:
        # set_user_to_db(message.from_user.id, message.from_user.first_name,tel_number=tel_numberx)
        bot.send_message(message.from_user.id,
                         "\nHURMATLI MIJOZ REGISTRATSIYADAN O`TISH UCHUN TELEFON RAQAMINGIZNI JO`NATING\n")
    # bot.send_message(message.from_user.id, "WELCOME TO THIS BOT!")
    # print(message.text)
    # languages(message)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
        keyboard.add(button_phone)  # Добавляем эту кнопку
        bot.send_message(message.chat.id, 'Номер телефона', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        user_id_from_db = get_user_from_db(message.from_user.id)
        if user_id_from_db:
            db = get_db()
            if db:
                for user in db:
                    try:
                        if user['user_id'] == message.from_user.id:
                            user['tel_number'] = message.contact.phone_number
                            languages(message)
                    except KeyError:
                        return None
        else:
            tel_numberx = message.contact.phone_number
            print(message.from_user.id)
            set_user_to_db(message.from_user.id, message.from_user.first_name, tel_numberx)
            languages(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global til
    # print(message.text)
    if message.text == "UZB 🇺🇿":
        til = "UZBEK 🇺🇿"
        answer_in_uzb(message)
    elif message.text == "RUS 🇷🇺":
        til = "RUS"
        ruscha_otvet(message)
        rus_knopkalari(message)
    elif message.text == "ENG 🇺🇸":
        til = "ENG"
    elif message.text == "BUYURTMA QILISH 🥡":
        pizzalar(message)
    elif message.text == "SOZLAMALAR ⚙️":
        sozlamalar(message)
    elif message.text == "FIKR BILDIRISH 📝":
        bot.send_message(message.from_user.id, "FIKRLARINGIZNI  @bonny_up ga YOZING!")
    elif message.text == "ORTGA QAYTISH 🔙":
        uzbek_function_on(message)

    # RUSSIAN PART STARTS FROM HERE
    elif message.text == "Оставить комментарий 📝":
        bot.send_message(message.from_user.id,
                         "Что вы думаете о нас? Кликните и Оставьте комментарий здесь @bonny_up 📝📝📝")
    elif message.text == "Параметры ⚙️":
        parametri(message)
    elif message.text == "Заказать 🥡":
        pizzi(message)
    elif message.text == "ПОСМОТРЕТЬ КОРЗИНУ 🗑":
        til = "RUS"
        savati_qara(message)
    elif message.text == "КОМБО ПИЦЦА 🏵":
        til = "RUS"
        BILL_rus = 1
        photo = 'https://cdn0.radioromantika.ru/vardata/modules/news/files/1/2224/news_file_2224_5a7c289d54653.jpg'
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL_rus)
    elif message.text == "Назад ◀️":
        languages(message)
    elif message.text == "ORTGA QAYTISH":
        languages(message)
    elif message.text == "ПИЦЦА ШАШЛЫК ️🍢":
        til = "RUS"
        BILL_rus = 2
        photo = "https://images.food52.com/VvroscTetPUoHgAGIUcoXLNA65M=/1200x900/e40cd6c0-2a48-40e9-9d4e-bfbb525d4d1d--Meatball_Pizza_3.jpg"
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL_rus)
    elif message.text == "КУРИННАЯ БАРБЕКЮ 🐥":
        til = "RUS"
        BILL_rus = 3
        photo = 'https://i.pinimg.com/originals/b9/af/94/b9af94f06bf1f20630c2031992493505.jpg'
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL_rus)


    elif message.text == "KOMBO 🏵":
        BILL = 1
        photo = 'https://cdn0.radioromantika.ru/vardata/modules/news/files/1/2224/news_file_2224_5a7c289d54653.jpg'
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL)
    elif message.text == "KABOBLIK ️🍢":
        SUM2 = 35000
        BILL = 2
        pizza2 = "KABOBLIK ️🍢  35000 SO'M"
        photo = "https://images.food52.com/VvroscTetPUoHgAGIUcoXLNA65M=/1200x900/e40cd6c0-2a48-40e9-9d4e-bfbb525d4d1d--Meatball_Pizza_3.jpg"
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL)
    elif message.text == "TOVUQLI BARBEQUE 🐥":
        SUM3 = 25000
        BILL = 3
        pizza3 = "TOVUQLI BARBEQUE 🐥 25000 SO'M"
        photo = 'https://i.pinimg.com/originals/b9/af/94/b9af94f06bf1f20630c2031992493505.jpg'
        bot.send_photo(message.from_user.id, photo)
        inline(message, BILL)
    elif message.text == "SAVATCHANGIZNI KO'RING🗑":
        savati_qara(message)
    elif message.text == "NARX 💷":
        til="UZBEK 🇺🇿"
        serverga_jonat(message)
        bot.send_message(message.from_user.id,
                         "HARIDINGIZ UCHUN RAHMAT! YETKAZMANI KUTING! KEYINGI SAFAR SIZNI YANA KUTIB QOLAMZ!\nYANA "
                         "BUYURTMA BERISH UCHUN /start ni bosing!")
        uzbek_function_on(message)
    elif message.text == "НАЛИЧНЫЕ 💷":
        til="RUS"
        serverga_jonat(message)
        bot.send_message(message.from_user.id,
                         "СПАСИБО ЗА ПОКУПКУ! ЖДИТЕ ДОСТАВКУ!\n "
                         "ЧТОБЫ ЗАКАЗАТЬ ЕЩЕ РАЗ, НАЖМИТЕ /start!")
        rus_knopkalari(message)
def languages(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton("UZB 🇺🇿")
    itembtn3 = types.KeyboardButton("RUS 🇷🇺")
    # itembtn2 = types.KeyboardButton("ENG 🇺🇸")
    markup1.add(itembtn1, itembtn3)
    bot.send_message(message.from_user.id,
                     "BOTGA XUSH KELIBSIZ TILNI TANLANG!\nДОБРО ПОЖАЛОВАТЬ НА БОТ!\nWELCOME TO THIS BOT",
                     reply_markup=markup1)




def telli_jonat(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
    keyboard.add(button_phone)  # Добавляем эту кнопку
    bot.send_message(message.from_user.id, 'Номер телефона', reply_markup=keyboard)

def muloqot_turi(message):
    muloqot_turidagin = types.InlineKeyboardMarkup(row_width=3)
    uz_language = types.InlineKeyboardButton(text="UZBEK", callback_data="uzb_language")
    rus_language = types.InlineKeyboardButton(text="RUSSIAN", callback_data="rus_language")
    muloqot_turidagin.add(uz_language, rus_language)
    bot.send_message(message.from_user.id, reply_markup=muloqot_turidagin, text=INFO)



def sozlamalar_inline(message, INFO):
    sozlamalr_inline = types.InlineKeyboardMarkup(row_width=3)
    language = types.InlineKeyboardButton(text="MULOQOT TILI", callback_data="language")
    tel = types.InlineKeyboardButton(text="TELEFON", callback_data="tel")
    sozlamalr_inline.add(language, tel)
    bot.send_message(message.from_user.id, text=INFO, reply_markup=sozlamalr_inline)


def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="MANZILNI YUBORISH", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.from_user.id, "JOYLASHGAN MANZILINGIZNI JO`NATING!", reply_markup=keyboard)


def geo_rus(message):
    keyboard_rus = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="ОТПРАВИТЬ АДРЕС", request_location=True)
    keyboard_rus.add(button_geo)
    bot.send_message(message.from_user.id, "ОТПРАВЬТЕ МЕСТОПОЛОЖЕНИЕ!", reply_markup=keyboard_rus)


@bot.message_handler(content_types=["location"])
def location(message):
    global latitude1
    if message.location is not None:
        # print(message.location)
        # print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        # latitude1 = f"{message.location.latitude}"
        # longtitude1 = f"{message.location.longitude}"
        latitude1 = message.location
        tolov_turi(message)


def answer_in_uzb(message):
    bot.reply_to(message, "SIZ O`ZBEK TILINI TANLADINGIZ")
    uzbek_function_on(message)


def tolov_turi(message):
    if til == "UZBEK 🇺🇿":
        tolov = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        narx = types.KeyboardButton("NARX 💷")
        # click = types.KeyboardButton("CLICK 💳")
        tolov.add(narx)  ##click)
        bot.send_message(message.from_user.id, "TO`LOV TURI", reply_markup=tolov)
    if til == "RUS":
        tolov_rus = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        narx_rus = types.KeyboardButton("НАЛИЧНЫЕ 💷")
        tolov_rus.add(narx_rus)
        bot.send_message(message.from_user.id, "ВИД ПЛАТЕЖА ", reply_markup=tolov_rus)


def serverga_jonat(message):
    global INFO
    db = get_db()
    if db:
        for user in db:
            try:
                if user['user_id'] == message.from_user.id:
                    ID = user['user_id']
                    ISMI = user['first_name']
                    NOMERI = user['tel_number']
                    # QUESTION=str(ISMI)+str(ID)+str(NOMERI)
                    INFO = "USERNI ISMI: " + str(ISMI) + '\n' + "USERNI ID: " + str(
                        ID) + '\n' + "USERNI RAQAMI: " + str(NOMERI)
                    print(ID, ISMI, NOMERI)
            except KeyError:
                return None
    text_to_server = INFO + '\n' + lrm + '\n' + str(latitude1) + '\n'
    bot.send_message(get_user_from_db(user_id=29193830), text=text_to_server)


def uzbek_function_on(message):
    mark = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("BUYURTMA QILISH 🥡")
    item2 = types.KeyboardButton("SOZLAMALAR ⚙️")
    item3 = types.KeyboardButton("FIKR BILDIRISH 📝")
    item4 = types.KeyboardButton("ORTGA QAYTISH")
    mark.add(item1, item2, item3, item4)
    bot.send_message(message.from_user.id, "KATEGORIYALARDAN BIRINI TANLANG!", reply_markup=mark)


def pizzalar(message):
    print(message)
    pizza_button1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    pizza11 = types.KeyboardButton("KOMBO 🏵")
    pizza21 = types.KeyboardButton("KABOBLIK ️🍢")
    pizza31 = types.KeyboardButton("TOVUQLI BARBEQUE 🐥")
    pizza41 = types.KeyboardButton("ORTGA QAYTISH 🔙")
    pizza51 = types.KeyboardButton("SAVATCHANGIZNI KO'RING🗑")
    pizza_button1.add(pizza11, pizza21, pizza31, pizza41, pizza51)
    bot.send_message(message.from_user.id, "PIZZALAR SIZGA MUNTAZIR! ☺☺️☺️☺️", reply_markup=pizza_button1)


def savati_qara(message):
    full_text = ""
    global lrm
    obwiy_summa = 0
    strong_set = set()
    global very_full_text
    if til == "UZBEK 🇺🇿":
        try:
            if not c[message.from_user.id]['CART']:
                bot.send_message(message.from_user.id, "SAVATINGIZ BO'SH!!!")
        except KeyError:
            bot.send_message(message.from_user.id, "SAVATINGIZ BO`SH AVVAL PIZZA ZAKAZ QILING!!!")
        else:
            for i in c[message.from_user.id]['CART']:
                print(i)
                full_text = f"SIZ TANLAGAN PIZZALAR!\n\nPIZZA TURI : {i['PIZZA TURI']}\nSONI: {i['SONI']}\nUMUMIY: {i['UMUMIY']} SO'M"
                obwiy_summa += i['UMUMIY']
                strong_set.add(full_text)
            lrm = ' '.join(strong_set)
            # bot.send_message(message.from_user.id,lrm)
            buyurtmaga_berish(message, lrm, obwiy_summa)
            print(lrm)
            print(obwiy_summa)
    elif til == "RUS":
        try:
            if not c[message.from_user.id]['CART']:
                bot.send_message(message.from_user.id, "ВАША КОРЗИНА ПУСТА!!!")
        except KeyError:
            bot.send_message(message.from_user.id, "ЗАКАЗЫВАЙТЕ ПИЦЦУ ДО ПУСТОЙ КОРЗИНЫ!!!")
        else:
            for i in c[message.from_user.id]['CART']:
                print(i)
                full_text = f"ВЫБИРАЕМАЯ ПИЦЦА!\n\nПИЦЦА : {i['PIZZA TURI']}\nЧИСЕЛ: {i['SONI']}\nОБЩАЯ: {i['UMUMIY']} СУМ"
                obwiy_summa += i['UMUMIY']
                strong_set.add(full_text)
            lrm = ' '.join(strong_set)
            # bot.send_message(message.from_user.id,lrm)
            zakazat(message, lrm, obwiy_summa)
            print(lrm)
            print(obwiy_summa)


def inline(message, BILL):
    global pizza_name, soqqa, pizza_name_rus, soqqa_rus,til
    # O`zbek
    if BILL == 1:
        soqqa = 45000
        pizza_name = "KOMBO 🏵 45000 SO'M"
    elif BILL == 2:
        soqqa = 35000
        pizza_name = "KABOBLIK ️🍢  35000 SO'M"
    elif BILL == 3:
        soqqa = 25000
        pizza_name = "TOVUQLI BARBEQUE 🐥 25000 SO'M"
    # rus
    if BILL == 1:
        soqqa_rus = 45000
        pizza_name_rus = "КОМБО ПИЦЦА 🏵 🏵 45000 СУМ"
    elif BILL == 2:
        soqqa_rus = 35000
        pizza_name_rus = "ПИЦЦА ШАШЛЫК ️🍢  35000 СУМ"
    elif BILL == 3:
        soqqa_rus = 25000
        pizza_name_rus = "КУРИННАЯ БАРБЕКЮ 🐥 25000 СУМ"

    if til == "UZBEK 🇺🇿":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_yes = types.InlineKeyboardButton(text="SAVATGA QO'SHISH", callback_data="QOSH")
        key_no = types.InlineKeyboardButton(text="PIZZA TARKIBI", callback_data="TARKIBI")
        key_he = types.InlineKeyboardButton(text="SAVATDAGI NARSALAR", callback_data="SAVAT")
        keyboard.add(key_yes, key_no, key_he)
        bot.send_message(message.from_user.id, reply_markup=keyboard, text=pizza_name)
    if til == "RUS":
        keyboard_rus = types.InlineKeyboardMarkup(row_width=2)
        key_yes_rus = types.InlineKeyboardButton(text="ДОБАВИТЬ В КОРЗИНУ", callback_data="ДОБАВИТЬ В КОРЗИНУ")
        key_no_rus = types.InlineKeyboardButton(text="ИНГРЕДИЕНТЫ ПИЦЦЫ", callback_data="ИНГРЕДИЕНТЫ ПИЦЦЫ")
        key_he_rus = types.InlineKeyboardButton(text="ПРЕДМЕТЫ В КОРЗИНЕ", callback_data="ПРЕДМЕТЫ В КОРЗИНЕ")
        keyboard_rus.add(key_yes_rus, key_no_rus, key_he_rus)
        bot.send_message(message.from_user.id, reply_markup=keyboard_rus, text=pizza_name_rus)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "QOSH":
        sonlar = types.InlineKeyboardMarkup(row_width=3)
        bir = types.InlineKeyboardButton(text="1", callback_data="1")
        ikki = types.InlineKeyboardButton(text="2", callback_data="2")
        uch = types.InlineKeyboardButton(text="3", callback_data="3")
        tort = types.InlineKeyboardButton(text="4", callback_data="4")
        besh = types.InlineKeyboardButton(text="5", callback_data="5")
        olti = types.InlineKeyboardButton(text="6", callback_data="6")
        yetti = types.InlineKeyboardButton(text="7", callback_data="7")
        sakkiz = types.InlineKeyboardButton(text="8", callback_data="8")
        toqqiz = types.InlineKeyboardButton(text="9", callback_data="9")
        ortga = types.InlineKeyboardButton(text="ORTGA🔙", callback_data="go_back")
        savatchezi_korin = types.InlineKeyboardButton(text="SAVATDA..", callback_data="see_cart")
        sonlar.add(bir, ikki, uch, tort, besh, olti, yetti, sakkiz, toqqiz, ortga, savatchezi_korin)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=sonlar)
    elif call.data=="go_back":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_yes = types.InlineKeyboardButton(text="SAVATGA QO'SHISH", callback_data="QOSH")
        key_no = types.InlineKeyboardButton(text="PIZZA TARKIBI", callback_data="TARKIBI")
        key_he = types.InlineKeyboardButton(text="SAVATDAGI NARSALAR", callback_data="SAVAT")
        keyboard.add(key_yes, key_no, key_he)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=keyboard)
    elif call.data=="see_cart":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=" --------SAVATDA--------")
        savati_qara(call)
    elif call.data == "TARKIBI":
        if pizza_name == "KOMBO 🏵 45000 SO'M":
            bot.send_message(call.from_user.id, "Pomidor sousi, Mozzarella pishloqi, Gouda pishloqi, pepperoni, Dor Blue pishloqi, yangi pomidor, Ranch sousi")
        elif pizza_name == "KABOBLIK ️🍢  35000 SO'M":
            bot.send_message(call.from_user.id, "Bekon, jambon, shampinyon, pomidor, yangi o'tlar, pomidor sousi, mozzarella.")
        elif pizza_name == "TOVUQLI BARBEQUE 🐥 25000 SO'M":
            bot.send_message(call.from_user.id, "Nozik tuzlangan va dudlangan tovuq go'shti, markali qaymoqli sous, mozzarella.")
    elif call.data == "SAVAT":
        savati_qara(call)
    elif call.data == "language":
        muloqot_turidagin = types.InlineKeyboardMarkup(row_width=3)
        uz_language = types.InlineKeyboardButton(text="UZBEK 🇺🇿", callback_data="uzb_language")
        rus_language = types.InlineKeyboardButton(text="RUSSIAN 🇷🇺", callback_data="rus_language")
        muloqot_turidagin.add(uz_language, rus_language)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=muloqot_turidagin)
    elif call.data == "uzb_language":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="MUVAFFAQIYATLI O`ZBEK TILI TANLANDI!🇺🇿")
        uzbek_function_on(call)

    elif call.data == "rus_language":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="РУССКИЙ ЯЗЫК УСПЕШНО ВЫБРАН!🇷🇺")
        rus_knopkalari(call)



    elif call.data=="tel":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="ILTIMOS BIZGA TELEFON RAQAMINGIZNI YUBORING!")
        telli_jonat(call)
    elif call.data == "1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 1, 'UMUMIY': soqqa * 1}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 2, 'UMUMIY': soqqa * 2}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 3, 'UMUMIY': soqqa * 3}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 4, 'UMUMIY': soqqa * 4}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "5":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 5, 'UMUMIY': soqqa * 5}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "6":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 6, 'UMUMIY': soqqa * 6}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "7":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 7, 'UMUMIY': soqqa * 7}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "8":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 8, 'UMUMIY': soqqa * 8}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "9":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 9, 'UMUMIY': soqqa * 9}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "clear_basket":
        c.clear()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATINGIZ MUVAFFAQIYATLI BO`SHATILDI! ✅")

    elif call.data == "delivery":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="YAXSHI ENDI")
        geo(call)

    # RUSSIAN LANGUAGE STARTS FROM HERE
    elif call.data == "ДОБАВИТЬ В КОРЗИНУ":
        soni_rus(call)
    elif call.data == "ИНГРЕДИЕНТЫ ПИЦЦЫ":
        if pizza_name_rus == "КОМБО ПИЦЦА 🏵 🏵 45000 СУМ":
            bot.send_message(call.from_user.id,
                             "Томатный соус, сыр Моцарелла, сыр Гауда, пепперони, Дор Блю сыр, свежие томаты, соус Ранч")
        elif pizza_name_rus == "ПИЦЦА ШАШЛЫК ️🍢  35000 СУМ":
            bot.send_message(call.from_user.id,
                             " Бекон, ветчина, шампиньоны, помидоры, свежая зелень, фирменный томатный соус, моцарелла.")
        elif pizza_name_rus == "КУРИННАЯ БАРБЕКЮ 🐥 25000 СУМ":
            bot.send_message(call.from_user.id,
                             "Нежная маринованная и копченая курочка, фирменный сливочный соус, моцарелла.")
    elif call.data == "ПРЕДМЕТЫ В КОРЗИНЕ":
        pass
    elif call.data == "odin":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name, 'SONI': 1, 'UMUMIY': soqqa_rus * 1}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "dva":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 2, 'UMUMIY': soqqa_rus * 2}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "tri":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 3, 'UMUMIY': soqqa_rus * 3}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "chetiri":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 4, 'UMUMIY': soqqa_rus * 4}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "pyat":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 5, 'UMUMIY': soqqa_rus * 5}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "shest":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 6, 'UMUMIY': soqqa_rus * 6}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "sem":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 7, 'UMUMIY': soqqa_rus * 7}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "vosem":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 8, 'UMUMIY': soqqa_rus * 8}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "devet":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="SAVATGA MUVAFFAQIYATLI QO`SHILDI! ✅")
        savatx = {'PIZZA TURI': pizza_name_rus, 'SONI': 9, 'UMUMIY': soqqa_rus * 9}
        if c.get(call.from_user.id, None):
            c[call.from_user.id]['CART'].append(savatx)
        else:
            c[call.from_user.id] = {'CART': [savatx]}
        print(c)
    elif call.data == "clear_basket_rus":
        c.clear()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="ВАША КОРЗИНА УСПЕШНО ОЧИЩЕН!✅")

    elif call.data == "delivery_rus":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="ХОРОШО")
        geo_rus(call)


def buyurtmaga_berish(message, lrm, obwiy_summa):
    buyurtma = types.InlineKeyboardMarkup(row_width=1)
    buyurtma_ber = types.InlineKeyboardButton(text="BUYURTMA BERISH 🚖", callback_data="delivery")
    savati_boshat = types.InlineKeyboardButton(text="SAVATNI BO`SHATISH ❌", callback_data="clear_basket")
    buyurtma.add(buyurtma_ber, savati_boshat)
    bot.send_message(message.from_user.id, text=lrm, reply_markup=buyurtma)


def zakazat(message, lrm, obwiy_summa):
    zakaz = types.InlineKeyboardMarkup(row_width=1)
    zakaz_qil = types.InlineKeyboardButton(text="ЗАКАЗАТЬ 🚖", callback_data="delivery_rus")
    korzinka_ochistit = types.InlineKeyboardButton(text="ОЧИСТИТЬ КОРЗИНУ ❌", callback_data="clear_basket_rus")
    zakaz.add(zakaz_qil, korzinka_ochistit)
    bot.send_message(message.from_user.id, text=lrm, reply_markup=zakaz)


def soni(message):
    sonlar = types.InlineKeyboardMarkup(row_width=3)
    bir = types.InlineKeyboardButton(text="1", callback_data="1")
    ikki = types.InlineKeyboardButton(text="2", callback_data="2")
    uch = types.InlineKeyboardButton(text="3", callback_data="3")
    tort = types.InlineKeyboardButton(text="4", callback_data="4")
    besh = types.InlineKeyboardButton(text="5", callback_data="5")
    olti = types.InlineKeyboardButton(text="6", callback_data="6")
    yetti = types.InlineKeyboardButton(text="7", callback_data="7")
    sakkiz = types.InlineKeyboardButton(text="8", callback_data="8")
    toqqiz = types.InlineKeyboardButton(text="9", callback_data="9")
    ortga=types.InlineKeyboardButton(text="ORTGA🔙",callback_data="go_back")
    savatchezi_korin=types.InlineKeyboardButton(text="SAVATDA..",callback_data="see_cart")
    sonlar.add(bir, ikki, uch, tort, besh, olti, yetti, sakkiz, toqqiz,ortga,savatchezi_korin)
    bot.send_message(message.from_user.id, text="QIYMATINI TANLANG!", reply_markup=sonlar)


def sozlamalar(message):
    db = get_db()
    if db:
        for user in db:
            try:
                if user['user_id'] == message.from_user.id:
                    ID = user['user_id']
                    ISMI = user['first_name']
                    NOMERI = user['tel_number']
                    # QUESTION=str(ISMI)+str(ID)+str(NOMERI)
                    INFO = "SIZNING ISMINGIZ: " + str(ISMI) + '\n' + "SIZNING ID: " + str(
                        ID) + '\n' + "SIZNING RAQAMINGIZ: " + str(NOMERI)
                    print(ID, ISMI, NOMERI)
                    #bot.send_message(message.from_user.id, INFO)
                    sozlamalar_inline(message, INFO)
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


bot.polling(none_stop=True)
