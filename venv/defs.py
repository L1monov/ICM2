import telebot
from telebot import types


def kind (fak):
    if fak == "MIP":
        markup = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton(text='Первый курс', callback_data=f"{USER['fak']}_{'first'}")
        second = types.InlineKeyboardButton(text='Второй курс', callback_data=f"{USER['fak']}_{'second'}")
        third = types.InlineKeyboardButton(text='Третий курс', callback_data=f"{USER['fak']}_{'trird'}")
        fourth = types.InlineKeyboardButton(text='Четвертый курс', callback_data=f"{USER['fak']}_{'fourth'}")
        fifth = types.InlineKeyboardButton(text='Пятый курс', callback_data=f"{USER['fak']}_{'fifth'}")
        markup.add(first, second, third, fourth, fifth)
        return markup