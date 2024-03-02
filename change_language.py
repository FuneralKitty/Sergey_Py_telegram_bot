from src.test_of_psql import update_user_params
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from constants import TOKEN
from src.json_formatter import DataManagement
bot = telebot.TeleBot(TOKEN)

def ask_language(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input your language',
                                 resize_keyboard=True)
    text = "Выберите ваш язык / Choose your language:"
    markup.add(*(KeyboardButton(language) for language in ['русский', 'english', 'italiano']))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def get_language(message):
    update_user_params(message, 'language',)
    user_language = message.text
    print(user_language)
    match user_language:
        case 'русский':
            text1, text2 = f'Выбран {message.text} язык: ', 'Продолжаем ...'
            bot.send_message(message.chat.id,  f'Выбран {message.text} язык: ')
            bot.send_message(message.chat.id, text=text2,
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        case 'english':
            bot.send_message(message.chat.id,  f'Chosen {message.text} language: ')
            bot.send_message(message.chat.id, text='Continue ...',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        case 'italiano':
            bot.send_message(message.chat.id,  f'Linguaggio scelto: {message.text}')
            bot.send_message(message.chat.id, text='Continua ...', reply_markup=telebot.types.ReplyKeyboardRemove())
        case _:
            bot.send_message(message.chat.id, f'Linguaggio scelto: {message.text}')
            bot.send_message(message.chat.id, text='Continua ...', reply_markup=telebot.types.ReplyKeyboardRemove())