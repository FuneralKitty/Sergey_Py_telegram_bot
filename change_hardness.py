
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import *
import json
from src.database import *
bot = telebot.TeleBot(TOKEN)


def ask_hardness(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input hardness u prefer')
    text = "Выберите сложность / Choose difficulty level:"
    # Получение языка пользователя из данных
    user_id = message.from_user.id
    user_language = get_user_data_by_param(user_id, param='language')

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
    bot.send_message(message.chat.id, str(message.text))
    if message.text in ['легко', 'facile', 'low']:
        message.text = 'low'
    elif message.text in ['сложно', 'media', 'medium']:
        message.text = 'medium'
    elif message.text in ['тяжело', 'difficile', 'difficult']:
        message.text = 'difficile'
    print(type(message.text))
    user_id = message.from_user.id
    update_user_params(message, param='hardness')
    # Получение языка пользователя из данных
    user_language = get_user_data_by_param(user_id, 'language')

    # Определение сложности в зависимости от языка пользователя
    if user_language:
        hardness_text = ''
        if user_language == 'русский':
            hardness_text = 'Сложность установлена на:'
        elif user_language == 'english':
            hardness_text = 'Difficulty set to:'
        elif user_language == 'italiano':
            hardness_text = 'Difficoltà impostata su:'

        if hardness_text:
            bot.send_message(message.chat.id, f"{hardness_text} {message.text}")
            # Если вы хотите очистить клавиатуру после выбора языка, можно отправить сообщение без разметки ответа
            bot.send_message(message.chat.id, 'Continue...', reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(message.chat.id, "Unsupported language.")
    else:
        bot.send_message(message.chat.id, "Language not found in database.")


