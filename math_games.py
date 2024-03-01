import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from constants import TOKEN
from src.json_formatter import DataManagement
from src.arithmetic import Math
bot = telebot.TeleBot(TOKEN)

all_math_functions = {
    'русский': ['калькулятор', 'простое число', 'четное/нечетное', 'прогрессия', 'наибольший общий делитель'],
    'english': ['calculator', 'prime number', 'even/odd', 'progression', 'greatest common divisor'],
    'italiano': ['calcolatrice', 'numero primo', 'pari/dispari', 'progressione', 'massimo comune divisore']
}
def ask_math(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input your language')
    text = 'Выберите игру'
    try:
        with open('All_data/users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError as f:
        bot.send_message('Mistakes in programm',f)
    user_language = data[str(message.from_user.id)]['language']
    match user_language:
        case 'русский':
            math_functions = all_math_functions['русский']
        case 'english':
            math_functions = all_math_functions['english']
        case 'italiano':
            math_functions = all_math_functions['italiano']
    markup.add(*(KeyboardButton(language) for language in math_functions))
    bot.send_message(message.chat.id, text, reply_markup=markup)


def welcome_user(message):
    with open('All_data/users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    user_language = data[str(message.from_user.id)]['language']
    match user_language:
        case 'русский':
            text = f'Добро пожаловать в математические игры, {message.from_user.first_name}!'
        case 'english':
            text = f'Welcome to the math games, {message.from_user.first_name}!'
        case 'italiano':
            text = f'Benvenuto ai giochi matematici, {message.from_user.first_name}!'
    bot.send_message(message.from_user.id, text=text)


def get_the_game(message):
    with open('All_data/users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        hardness = data[str(message.from_user.id)]['hardness']
        language = data[str(message.from_user.id)]['language']
        print(hardness, language)
    if message.text in ['калькулятор','calculator','calcolatrice']:
        flag = 'calculator'
        b = Math()
        for_user,answer = b.calculator(hardness=hardness)
        description = b.get_description(language, 'calculator')
        return flag,for_user,answer,description
    if message.text in ['простое число','prime number','numero primo']:
        flag = 'prime'
        b = Math()
        for_user, answer = b.is_prime_game(hardness=hardness)
        description = b.get_description(language,'is_prime_game')
        print(flag,for_user,answer,description)
        return flag,for_user,answer,description
    if message.text in ['четное/нечетное','even/odd','pari/dispari']:
        flag = 'even'
        b = Math()
        for_user, answer = b.is_even_game(hardness=hardness)
        description = b.get_description(language, 'is_even_game')
        return flag,for_user,answer,description
    if message.text in ['прогрессия','progression','progressione']:
        flag = 'progression'
        b = Math()
        for_user, answer = b.progression(hardness=hardness)
        description = b.get_description(language, 'progression')
        return flag,for_user,answer, description
    if message.text in ['наибольший общий делитель','greatest common divisor','massimo comune divisore']:
        flag = 'gcd'
        b = Math()
        for_user, answer = b.generate_gcd_question(hardness=hardness)
        description = b.get_description(language, 'generate_gcd_question')
        return flag,for_user,answer,description
    else:
        print('Someting went wrong in Get_The_Game, math games')

def yes_or_no_math_markup(message):
    markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='Сделайте правильный выбор',
                                         resize_keyboard=True)
    italian = ['si','no']
    english = ['yes', 'no']
    russian = ['да','нет']
    with open('All_data/users.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Получение языка пользователя из данных
    user_language = data.get(str(message.from_user.id), {}).get('language')
    match user_language:
        case 'русский':
            user_lang = russian
        case 'english':
            user_lang = english
        case 'italiano':
            user_lang = italian
    markup.add(*(KeyboardButton(language) for language in user_lang))
    bot.send_message(message.chat.id,'Even or Odd', reply_markup=markup)