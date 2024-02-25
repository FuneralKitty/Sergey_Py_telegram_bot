import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from constants import TOKEN
from src.json_formatter import DataManagement
bot = telebot.TeleBot(TOKEN)

def ask_language(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input your language')
    languages = ['русский', 'английский', 'итальянский']
    text = "Выберите ваш язык / Choose your language:"
    markup.add(*(KeyboardButton(language) for language in languages))
    bot.send_message(message.chat.id, text, reply_markup=markup)

def get_language(message):
    d = DataManagement('All_data/users.json')
    d.dump_json_data(message,key='language')
    bot.send_message(message.chat.id, f"Ваш язык установлен на: {message.text}")
    # If you want to clear the keyboard after language selection, you can send a message with no reply markup
    bot.send_message(message.chat.id, "Теперь вы можете продолжить.",
                     reply_markup=telebot.types.ReplyKeyboardRemove())