import telebot
from telebot import types
import db
import defs
import parsing
import datetime
bot = telebot.TeleBot('5490108271:AAEWDnpV7AkloYuGsr1hcHLL-4Gsb3ID15s')


#XUY


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if db.CheckUser(user_id) == 'No':
        db.NewUser(user_id,username,first_name,last_name)
    mesg = bot.send_message(message.chat.id, '👋Привет, я бот-помощник по поиску распписание👋 \n🔍Давай найдём трою группу🔎\n❕(Пример : ИБ-321)❕')
    bot.register_next_step_handler(mesg, find_group)
@bot.message_handler(commands=['info'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp_week = types.KeyboardButton("Расп. неделя")
    rasp_tomorrow = types.KeyboardButton("Расп. завтра")
    rasp_today = types.KeyboardButton("Расп. сегодня")
    profil = types.KeyboardButton("Профиль")
    settings = types.KeyboardButton("Настройки")
    markup.add(rasp_week, rasp_tomorrow, rasp_today)
    markup.add(profil, settings)
    bot.send_message(message.chat.id, 'Нихуя ты умный. \nБот был разработан командой ICM', reply_markup=markup)
@bot.message_handler(commands=['admin'])
def admin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp_week = types.KeyboardButton("Расп. неделя")
    rasp_tomorrow = types.KeyboardButton("Расп. завтра")
    rasp_today = types.KeyboardButton("Расп. сегодня")
    profil = types.KeyboardButton("Профиль")
    settings = types.KeyboardButton("Настройки")
    markup.add(rasp_week, rasp_tomorrow, rasp_today)
    markup.add(profil, settings)
    if db.all_user(message.from_user.id) == 'No':
        bot.send_message(message.chat.id, 'Ты не одмен', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"{db.all_user(message.from_user.id)}", reply_markup=markup)

def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if db.CheckUser(user_id) == 'No':
        db.NewUser(user_id,username,first_name,last_name)
    mesg = bot.send_message(message.chat.id, 'Привет, я бот-помощник по поиску распписание. \nДавай найдём трою группу.\n(Пример : ИБ-321)')
    bot.register_next_step_handler(mesg, find_group)

def find_group (message):
    try:
        faculty = db.find_number_group(message.text.upper())[0]
        kind = db.find_number_group(message.text.upper())[1]
        group = db.find_number_group(message.text.upper())[2]
        markup = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton(text='Да, всё верно!', callback_data=f"{'menu'}")
        no = types.InlineKeyboardButton(text='Нет, ты ошибся', callback_data=f"{'wrong_choicec'}")
        markup.add(yes, no)
        msg = f"Кажется я что-то нашёл\nФакультет : {faculty}\nКурс {kind}\nГруппа {group}\nЯ правильно нашёл?"
        db.UpdateInfoUser(message.from_user.id, message.text)
        bot.send_message(message.chat.id, msg, reply_markup=markup)
    except Exception as ex:
        print (ex)
        mesg = bot.send_message(message.chat.id, 'Ты ввел что-то неверное , введи еще раз.\n(Пример : ИБ-321)')
        bot.register_next_step_handler(mesg, find_group)
def new_offer(message):
    msg = f"Спасибо за предложение"
    db.New_Offer(message.from_user.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp_week = types.KeyboardButton("Расп. неделя")
    rasp_tomorrow = types.KeyboardButton("Расп. завтра")
    rasp_today = types.KeyboardButton("Расп. сегодня")
    profil = types.KeyboardButton("Профиль")
    settings = types.KeyboardButton("Настройки")
    markup.add(rasp_week, rasp_tomorrow, rasp_today)
    markup.add(profil, settings)
    bot.send_message(message.chat.id, msg, reply_markup=markup)
def new_mistake(message):
    msg = f"Спасибо за обратную связь"
    db.New_Mistake(message.from_user.id, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rasp_week = types.KeyboardButton("Расп. неделя")
    rasp_tomorrow = types.KeyboardButton("Расп. завтра")
    rasp_today = types.KeyboardButton("Расп. сегодня")
    profil = types.KeyboardButton("Профиль")
    settings = types.KeyboardButton("Настройки")
    markup.add(rasp_week, rasp_tomorrow, rasp_today)
    markup.add(profil, settings)
    bot.send_message(message.chat.id, msg, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == "menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rasp_week = types.KeyboardButton("Расп. неделя")
        rasp_tomorrow = types.KeyboardButton("Расп. завтра")
        rasp_today = types.KeyboardButton("Расп. сегодня")
        profil = types.KeyboardButton("Профиль")
        settings = types.KeyboardButton("Настройки")
        markup.add(rasp_week, rasp_tomorrow, rasp_today)
        markup.add(profil, settings)
        bot.send_message(callback.message.chat.id, 'Главное меню', reply_markup=markup)
    if callback.data == "wrong_choicec":
        mesg = bot.send_message(callback.message.chat.id, 'Поробуй ввести еще раз.\n(Пример ИБ-321)')
        bot.register_next_step_handler(mesg, find_group)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rasp_week = types.KeyboardButton("Расп. неделя")
        rasp_tomorrow = types.KeyboardButton("Расп. завтра")
        rasp_today = types.KeyboardButton("Расп. сегодня")
        profil = types.KeyboardButton("Профиль")
        settings = types.KeyboardButton("Настройки")
        markup.add(rasp_week, rasp_tomorrow, rasp_today)
        markup.add(profil, settings)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)
    if (message.text == "Расп. неделя"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rasp_Monday = types.KeyboardButton('Понедельник')
        rasp_Tuesday = types.KeyboardButton('Вторник')
        rasp_Wednesday = types.KeyboardButton('Среда')
        rasp_Thursday = types.KeyboardButton('Четверг')
        rasp_Friday = types.KeyboardButton('Пятница')
        rasp_Saturday = types.KeyboardButton('Суббота')
        menu = types.KeyboardButton('Меню')
        markup.add(rasp_Monday, rasp_Tuesday, rasp_Wednesday)
        markup.add(rasp_Thursday, rasp_Friday,rasp_Saturday)
        markup.add(menu)
        bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=markup)
    if (message.text == "Понедельник"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 0)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 0)}\n{msg}")
    if (message.text == "Вторник"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 1)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 1)}\n{msg}")
    if (message.text == "Среда"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 2)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 2)}\n{msg}")
    if (message.text == "Четверг"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 3)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 3)}\n{msg}")
    if (message.text == "Пятница"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 4)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 4)}\n{msg}")
    if (message.text == "Суббота"):
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], 5)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], 5)}\n{msg}")
    if (message.text == "Расп. завтра"):
        if datetime.datetime.today().weekday() == 6:
            print(123)
            day = 0
        if datetime.datetime.today().weekday() != 6:
            print(321)
            day = datetime.datetime.today().weekday() + 1
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], day)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], day)}\n{msg}")
    if (message.text == "Расп. сегодня"):
        day = datetime.datetime.today().weekday()
        lesson = parsing.rasp_day(db.InfoUser(message.from_user.id)[2], day)
        if lesson == 'Пар нет':
            bot.send_message(message.chat.id, 'Пар нет , можно расслабиться')
        else:
            msg = ''
            for i in lesson:
                name_lesson = lesson[i]['name']
                msg = f"{msg}################ \n{name_lesson}\n"
                type_lesson = lesson[i]['type']
                msg = f"{msg}{type_lesson}\n"
                aud_lesson = lesson[i]['aud']
                msg = f"{msg}{aud_lesson}\n"
                time_lesson = lesson[i]['time']
                msg = f"{msg}{time_lesson}\n"
                prepod = lesson[i]['prepod']
                msg = f"{msg}{prepod}\n"
            bot.send_message(message.chat.id, f"{parsing.type_week(db.InfoUser(message.from_user.id)[2], day)}\n{msg}")
    if (message.text == "Профиль"):
        faculty = db.InfoUser(message.from_user.id)[0]
        if faculty == 'МИП':
            facylty = 'Менеджмент и предпринимательство'
        if faculty == 'ТД':
            facylty = 'Торговое дело'
        if faculty == 'КТИИБ':
            facylty = 'Компьютерные технологии и информационная безопасность'
        if faculty == 'УЭФ':
            facylty = 'Учетное-экономический'
        if faculty == 'ЭИФ':
            facylty = 'Экономика и финансы'
        if faculty == 'ЮР':
            facylty = 'Юридический факультет'
        if faculty == 'ЛИЖ':
            facylty = 'Лингвистики и журналистики'
        kind = db.InfoUser(message.from_user.id)[1]
        group = db.InfoUser(message.from_user.id)[2]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu = types.KeyboardButton("Меню")
        change_group = types.KeyboardButton("Изменить группу")
        markup.add(menu, change_group)
        bot.send_message(message.chat.id, f"Ваш факультет: {faculty}\nВаш курс: {kind}\nВаша группа: {group}",reply_markup=markup)
    if (message.text == "Изменить группу"):
        mesg = bot.send_message(message.chat.id,'Введи группу\n(Пример : ИБ-321)')
        bot.register_next_step_handler(mesg, find_group)
    if (message.text == "Настройки"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ofers = types.KeyboardButton("Предложение")
        mistake = types.KeyboardButton("Сообщить об ошибке")
        menu = types.KeyboardButton("Меню")
        markup.add(ofers)
        markup.add(mistake)
        markup.add(menu)
        bot.send_message(message.chat.id, f"Настройки",reply_markup=markup)
    if (message.text == "Предложение"):
        mesg = bot.send_message(message.chat.id, 'Введите Ваше предложение')
        bot.register_next_step_handler(mesg, new_offer)
    if (message.text == "Сообщить об ошибке"):
        mesg = bot.send_message(message.chat.id, 'Введите ошибку')
        bot.register_next_step_handler(mesg, new_mistake)

print ('bot rolling')
bot.polling(none_stop=True)




