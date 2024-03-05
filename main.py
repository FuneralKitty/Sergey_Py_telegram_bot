from constants import *
from change_language import *
from change_hardness import *
from Anya_bot_class import Anya
from math_games import *
from src.database import *


#Создание баз данных

create_user_table()
create_notification_table()


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
def ask_for_math(message):
    welcome_user(message)
    ask_math(message)
    bot.register_next_step_handler(message, starter)


def starter(message):
    print('passed 2')
    print(message.text)
    bot.send_message(message.from_user.id, 'Бот активирован начинаем математику!')
    flag, for_user_quest, answer, description = get_the_game(message)
    print(flag, for_user_quest, answer, description)
    try:
        bot.send_message(message.from_user.id, description)
        bot.send_message(message.from_user.id, answer)
        bot.send_message(message.from_user.id, for_user_quest)
        if flag == 'prime' or flag == 'even':
            yes_or_no_math_markup(message)
            bot.register_next_step_handler(message, process_math_step, answer=answer, flag=flag)
        else:
            bot.register_next_step_handler(message, process_math_step, answer, flag=flag)
    except Exception as e:
        bot.send_message(message.from_user.id, 'Something went wrong, maybe you tried to switch the command')
        print(e)


def process_math_step(message, answer, flag=None):
    if message.text.lower() == 'off':
        bot.send_message(message.from_user.id, 'Bot is Deactivated')
        return
    print('message: ', message.text.lower(), 'correct message:', answer)
    if flag == 'prime' or flag == 'even':
        try:
            if message.text.lower() in answer:
                bot.send_message(message.from_user.id, 'Вы правы!')
            else:
                bot.send_message(message.from_user.id, 'Вы неправильно ответили.')
        except ValueError:
            bot.send_message(message.from_user.id, 'Value is incorrect, write Yes/no')
    else:
        try:
            user_answer = int(message.text.strip())
            if user_answer == int(answer):
                bot.send_message(message.from_user.id, 'Вы правы!')
            else:
                bot.send_message(message.from_user.id, 'Вы неправильно ответили.')
        except ValueError:
            bot.send_message(message.from_user.id, 'Value is incorrect, you must write only integers!')
    mess = int(message.from_user.id)
    flag, for_user_quest, answer, description = get_the_game(mess=mess, mode=flag)
    if flag == 'prime' or flag == 'even':
        yes_or_no_math_markup(message)
        bot.send_message(message.from_user.id, for_user_quest)
        bot.send_message(message.from_user.id, answer)
        bot.register_next_step_handler(message, process_math_step, answer=answer, flag=flag)
    else:
        bot.send_message(message.chat.id, for_user_quest)
        bot.send_message(message.from_user.id, answer)
        bot.register_next_step_handler(message, process_math_step, answer=answer, flag=flag)




@bot.message_handler(func=lambda message: message.text.lower() in hello_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_hello(message))

@bot.message_handler(func=lambda message: message.text.lower() in bye_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_goodbye(message))

bot.polling(none_stop=True)