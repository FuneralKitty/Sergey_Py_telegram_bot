from src.json_formatter import DataManagement
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import *
import json

bot = telebot.TeleBot(TOKEN)


def ask_hardness(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input hardness u prefer')
    text = "Выберите сложность / Choose difficulty level:"
    with open('All_data/users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Получение языка пользователя из данных
    user_language = data.get(str(message.from_user.id), {}).get('language')

    # Определение сложности в зависимости от языка пользователя
    match user_language:
        case 'русский':
            hardness = hardness_ru
        case 'english':
            hardness = hardness_eng
        case 'italiano':
            hardness = hardness_italian
        case _:
            # Если язык пользователя не определен или не соответствует ожидаемым значениям,
            # можно предоставить пользователю возможность выбрать сложность на языке по умолчанию
            # или отправить сообщение об ошибке
            return bot.send_message(message.chat.id, "Ошибка: Невозможно определить язык пользователя.")


    # Добавление кнопок сложности на основе определенного языка
    markup.add(*(KeyboardButton(hard) for hard in hardness))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def get_hardness(message):
    d = DataManagement('All_data/users.json')
    d.dump_json_data(message,key='hardness')
    with open('All_data/users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Получение языка пользователя из данных
    user_language = data.get(str(message.from_user.id), {}).get('language')

    # Определение сложности в зависимости от языка пользователя
    match user_language:
        case 'русский':
            text1, text2 = 'Сложность установлена на: ', 'Продолжаем ...'
        case 'english':
            text1, text2 = 'Difficulty set to: ', 'Continue ...'
        case 'italiano':
            text1, text2 = 'Difficoltà impostata su: ', 'Continua ...'

    bot.send_message(message.chat.id, f"{text1} {message.text}")
    # If you want to clear the keyboard after language selection, you can send a message with no reply markup
    bot.send_message(message.chat.id, text2,reply_markup=telebot.types.ReplyKeyboardRemove())