from telebot import types

def number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Отправить номер телефона", request_contact=True)
    kb.add(button)
    return kb