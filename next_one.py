# import telebot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# from keyboard_constants import *
#
# bot = telebot.TeleBot(TOKEN)
#
#
# class StudyKeyboard:
#
#     def __init__(self):
#     def choose_language_keyboard(self, message):
#         markup = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True,input_field_placeholder='@@@@')
#         keys = ['russian', 'english', 'italian','Arithmetic','быстрая печать','exit', 'main menu']
#         text = "Добро пожаловать, выберите язык/Welcome, choose your language"
#         markup.add(*(KeyboardButton(i) for i in keys))
#         bot.send_message(message.chat.id, text, reply_markup=markup)
#         d = bot.message_handler(func=lambda message:True)
#         print(d)
#         return markup
#
#     def main_menu(self, message):
#         markup = ReplyKeyboardMarkup(row_width=2)
#         type_training = ['тренировка', 'главное меню', 'выйти']
#         markup.add(*(KeyboardButton(i) for i in type_training))
#         bot.send_message(message.chat.id, "Choose a category: ", reply_markup=markup)
#         return markup
#     def __del__(self):
#         print("Closing bot")
#     def new(self):
#         pass
#
#
#
#
# @bot.message_handler(commands=["start"])
# def start_message(message):
#     keyboard = StudyKeyboard()
#     keyboard.choose_language_keyboard(message)
#
# @bot.message_handler(func=lambda message: True)
# def all_messages(message):
#     languages = ['russian', 'english', 'italian']
#     keyboard = StudyKeyboard()
#     if message.text in languages:
#         keyboard.language = message.text
#         bot.send_message(message.chat.id, f"Keyboard language is being customized to: {keyboard.language}")
#     if message.text == "exit":
#         markup = telebot.types.ReplyKeyboardRemove()
#         bot.send_message(message.from_user.id, "Done with Keyboard", reply_markup=markup)
#     if message.text in ['main menu','главное меню']:
#         keyboard.main_menu(message)
#     if message.text == ['Arithmetic']:
#         bot.send_message(message.chat.id, f"Keyboard language is being customized to: {keyboard.language}")
