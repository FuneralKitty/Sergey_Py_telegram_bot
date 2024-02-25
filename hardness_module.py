import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from constants import TOKEN
bot = telebot.TeleBot(TOKEN)

try:
    with open('users.json') as f:
        users_data = json.load(f)
except FileNotFoundError:
    users_data = {}

def get_hardness_choice(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='Выберите сложность')
    hardness = ['легко', 'сложно', 'тяжело', 'DOOM']
    text = "Выберите ваш язык / Choose your language:"
    markup.add(*(KeyboardButton(hard) for hard in hardness))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def save_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=2)


def change_json(message):
    user_id = str(message.chat.id)
    language = message.text.lower()
    # Проверяем, существует ли уже пользователь в базе данных

    if user_id in users_data:
        # Если существует, обновляем язык пользователя
        users_data[user_id]['language'] = language
    else:
        # Если нет, создаем новую запись
        users_data[user_id] = {'language': language}

    save_data(users_data)  # Сохраняем обновленные данные
    bot.send_message(message.chat.id, f"Выбранный язык: {language}")

    # If you want to clear the keyboard after language selection, you can send a message with no reply markup
    bot.send_message(message.chat.id, "Теперь вы можете продолжить.",
                     reply_markup=telebot.types.ReplyKeyboardRemove())
