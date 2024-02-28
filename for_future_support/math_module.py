from src.arithmetic import Math
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import TOKEN,math_games,game_rounds
from telebot import TeleBot
bot = TeleBot(TOKEN)


def start_game():
    bot.send_message('Welcome there, stranger!')
    user_score = 0
    b = get_the_game
    bot.send_message()
    while user_score < game_rounds:
        quest, operation = get_the_game()
        print('Question:', quest)
        answer = input('Your answer: ')

        if operation == answer:
            print('Correct!')
            user_score += 1
        else:
            print(f"'{answer}' is the wrong answer."
                    f"Correct answer was '{operation}'."
                    f"\nLet's try again, " + user_name + "!")
            break

    if user_score == game_rounds:
        print('Congratulations, ' + user_name + '!')