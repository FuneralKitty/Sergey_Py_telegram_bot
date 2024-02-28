from constants import *
from change_language import *
from change_hardness import *
from Anya_bot_class import Anya
from math_games import *
@bot.message_handler(commands=["start", "change_language"])
def ask_for_lang(message):
    global language_flag
    ask_language(message)
    language_flag = True

@bot.message_handler(func=lambda message: message.text.lower() in ['русский','english', 'italiano'])
def start_message_language(message):
    global language_flag
    # Check if the message was sent as a command
    if language_flag:
        get_language(message)
        language_flag = False

@bot.message_handler(func=lambda message: message.text.lower() in hello_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_hello(message))
@bot.message_handler(func=lambda message: message.text.lower() in bye_keywords)
def hello_message(message):
    bot.send_message(message.chat.id,Anya.say_goodbye(message))


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


@bot.message_handler(commands=["math"]) #начало всех игр
def ask_for_lang(message):
    global math_flag
    ask_math(message)
    math_flag = True
@bot.message_handler(func=lambda message: message.text.lower() in all_math_functions_messages) #in constants получение названия игры
def start_message_language(message):
    global math_flag
    if math_flag:
        flag = get_the_game(message)
        math_flag = False
        global next_math_flag
@bot.message_handler(func=lambda message: message.text.lower()) #take responses для игры
def math_answers(message):
    global next_math_flag
    welcome_user(message)

    # user_score = 0
    # game_rounds = 3
    #
    # while user_score < game_rounds:
    #     get_math(message,game=next_math_flag)

bot.polling()
