from src.json_formatter import DataManagement
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import TOKEN, hardness

bot = telebot.TeleBot(TOKEN)

def ask_hardness(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input hardness u prefer')
    text = "Выберите ваш язык / Choose your language:"
    markup.add(*(KeyboardButton(hard) for hard in hardness))
    bot.send_message(message.chat.id, text, reply_markup=markup)

def get_hardness(message):
    d = DataManagement('All_data/users.json')
    d.dump_json_data(message,key='hardness')
    bot.send_message(message.chat.id, f"Сложность установлена на: {message.text}")
    # If you want to clear the keyboard after language selection, you can send a message with no reply markup
    bot.send_message(message.chat.id, "Продолжаем ...",reply_markup=telebot.types.ReplyKeyboardRemove())