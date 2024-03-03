from constants import *
from change_language import *
from change_hardness import *
from Anya_bot_class import Anya
from math_games import *
from src.arithmetic import Math
from src.database import *
@bot.message_handler(commands=["start", "change_language"])
def ask_for_lang(message):
    global language_flag
    language_flag = True
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    language = 'russian'  # Example value, change as needed
    hardness = 'low'  # Example value, change as needed
    win_count = 0  # Example value, change as needed
    existing_user = check_existing_user(user_id)
    if not existing_user:
        insert_into_database(user_id, user_name, language, hardness, win_count)
        bot.send_message(message.chat.id, "Данные пользователя добавлены в базу данных.")
    else:
        bot.send_message(message.chat.id, "Пользователь уже существует в базе данных.")
    print('True')
    ask_language(message)


@bot.message_handler(func=lambda message: message.text.lower() in ['русский','english', 'italiano'])
def start_message_language(message):
    global language_flag
    # Check if the message was sent as a command
    if language_flag:
        get_language(message)
        language_flag = False


@bot.message_handler(commands=["hardness"])
def ask_for_lang(message):
    global hardness_flag
    ask_hardness(message)
    hardness_flag = True

@bot.message_handler(func=lambda message: message.text.lower() in all_hardness)
def start_message_language(message):
    global hardness_flag
    # Check if the message was sent as a command
    if hardness_flag:
        get_hardness(message)
        hardness_flag = False


@bot.message_handler(commands=["math"])  # начало всех игр
def ask_for_lang(message):
    global math_flag
    ask_math(message)
    math_flag = True
    bot.register_next_step_handler(message, start_message)

def start_message(message):
    global math_flag
    print('start message')
    welcome_user(message)
    global flag
    if math_flag:
        try:
            flag, for_user_quest, answer, description = get_the_game(message)
            bot.send_message(message.from_user.id, answer)
            math_flag = False
            bot.send_message(message.from_user.id, description)
            bot.send_message(message.from_user.id, for_user_quest)
            if flag == 'prime' or flag == 'even':
                yes_or_no_math_markup(message)
            bot.register_next_step_handler(message, process_math_step, answer, flag = flag)
        except Exception as e:
            bot.send_message(message.from_user,'Something went wront, maybe u tried to switch the command')
def process_math_step(message, correct_answer,flag=None):
    print('process_math_step activated')
    global math_flag
    print('message: ', message.text.lower(), 'correct message:', correct_answer)
    if flag == 'prime' or flag == 'even':
        try:
            if message.text.lower() in correct_answer:
                bot.send_message(message.from_user.id, 'Вы правы! Для выбора следующей игры нажмите /math')
                math_flag = True
                bot.register_next_step_handler(message, ask_for_lang)
            else:
                bot.send_message(message.from_user.id, 'Вы неправильно ответили.')
                math_flag = True
                bot.send_message(message.from_user.id, 'Для выбора игры нажмите /math')
        except ValueError as e:
            bot.send_message(message.from_user, 'Value is incorrect, write Yes/no')
            bot.register_next_step_handler()
    if flag == 'gcd' or flag == 'progression' or flag == 'calculator':
        try:
            user_answer = int(message.text.strip())
            print(user_answer)
            if user_answer == correct_answer:
               bot.send_message(message.from_user.id, 'Вы правы! Для выбора следующей игры нажмите /math')
               math_flag = True
               bot.register_next_step_handler(message,ask_for_lang)
            else:
               bot.send_message(message.from_user.id, 'Вы неправильно ответили.')
               math_flag = True
               bot.send_message(message.from_user.id, 'Для выбора игры нажмите /math')
        except ValueError as e:
                bot.send_message(message.from_user.id,'Value is incorrect, U must write only integers!')
                bot.register_next_step_handler(message,ask_for_lang)


@bot.message_handler(func=lambda message: message.text.lower() in hello_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_hello(message))

@bot.message_handler(func=lambda message: message.text.lower() in bye_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_goodbye(message))

bot.polling(none_stop=True)