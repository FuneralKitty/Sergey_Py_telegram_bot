from constants import hardness, hello_keywords, bye_keywords,math_games
from change_language import *
from change_hardness import *
import telebot
import re
from Anya_bot_class import Anya
import change_hardness

@bot.message_handler(commands=["start", "change_language"])
def ask_for_lang(message):
    global language_flag
    ask_language(message)
    language_flag = True

@bot.message_handler(func=lambda message: message.text.lower() in ['русский', 'английский', 'итальянский'])
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

@bot.message_handler(func=lambda message: message.text.lower() in hardness)
def start_message_language(message):
    global hardness_flag
    # Check if the message was sent as a command
    if hardness_flag:
        get_hardness(message)
        hardness_flag = False












# @bot.message_handler(func=lambda message: message.text.lower() in hardness_constants)
# def hardness(message):
#     markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, input_field_placeholder='input your language')
#     languages = ['русский', 'английский', 'итальянский']
#     text = "Выберите ваш язык / Choose your language:"
#     markup.add(*(KeyboardButton(language) for language in languages))
#     bot.send_message(message.chat.id, text, reply_markup=markup)
#     try:
#         with open('users.json') as f:
#             users_data = json.load(f)
#     except FileNotFoundError:
#         users_data = {}

# @bot.message_handler(commands=["math", "математика"])
# def start_game(message):
#     global hardness
#     if not hardness:
#         bot.send_message(message.chat)
#         hardness = hardness()
#         print(message.text)


# @bot.message_handler(commands=["hardness"])
# def ask_for_lang(message):
#     global hardness_flag
#     get_hardness_choice(message)
#     hardness_flag = True
#
# @bot.message_handler(func=lambda message: message.text.lower() in hardness_constants)
# def start_message_language(message):
#     global hardness_flag
#     # Check if the message was sent as a command
#     if hardness_flag:
#         hardness(message)
#         hardness_flag = False











#     game_type = message.text.lower()
#     math_game = Math(hardness=(1, 10))  # Пример передачи уровня сложности
#
#     match game_type:
#         case 'калькулятор':
#             quest, operation, description = math_game.calculator()
#             return quest, operation, description
#         case 'чётное/нечётное':
#             quest, operation, description = math_game.is_even_game()
#             return quest, operation, description
#         case 'простое/сложное':
#             prime_number, operation, description = math_game.is_prime_game()
#             return quest, operation, description
#         case 'прогрессия':
#             quest, operation, description = math_game.progression()
#             return quest, operation, description
#         case 'НОД':
#             quest, operation, description = math_game.generate_gcd_question()
#             return quest, operation, description
#     bot.send_message(message.chat.id, f"{description}\n{quest}")
# @bot.message_handler(func=lambda message: message.text.lower() in math_games)
# def start_message_math(message):
#     global math_flag
#     if math_flag:
#          pass
# from brain_games.games.engine import start_game
# from brain_games.games.brain_calculation import play_game, description
#
#
# def main():
#     start_game(play_game, description)
bot.polling()