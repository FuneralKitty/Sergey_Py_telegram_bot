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
        bot.send_message('Mistakes in programm')
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

def get_math(message,game=None):
    welcome_user(message)
    print(game)
    match game:
        case 'calc':
            global calc
        case 'prime':
            global prime
        case 'even':
            global even
        case 'progression':
            global progression
        case 'gcd':
            global gcd
    user_score = 0
    game_rounds = 3

    #Дописать программу проверить вход сообщений от пользователя
    while user_score < game_rounds:
        quest, operation = get_the_game(message)
        bot.send_message(message.from_user.id,f'Question: {quest}')
        user_answer = bot.get_message(chat_id).text
        if operation == answer:
            print('Correct!')
            user_score += 1
        else:
            print(f"'{answer}' is the wrong answer."
                    f"Correct answer was '{operation}'."
                    f"\nLet's try again ,{message.from_user.first_name}!")
            break
    if user_score == game_rounds:
        print(f'Congratulations, {message.from_user.first_name}!')


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
    if message.text in ['калькулятор','calculator','calcolartice']:
        b=Math().calculator()
        flag = 'calc'
        return b,flag
    if message.text in ['простое число','prime number','numero primo']:
        b = Math().is_prime()
        flag = 'prime'
        return b,flag
    if message.text in ['четное/нечетное','even/odd','pari/dispari']:
        b = Math().is_even_game()
        flag = 'even'
        return b, flag
    if message.text in ['прогрессия','progression','progressione']:
        b = Math().progression()
        flag = 'progression'
        return b, flag
    if message.text in ['наибольший общий делитель','greatest common divisor','massimo comune divisore']
        b = Math().generate_gcd_question()
        flag = 'gcd'
        return b, flag