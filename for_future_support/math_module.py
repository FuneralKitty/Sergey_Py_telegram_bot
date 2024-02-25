from src.arithmetic import Math
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from constants import TOKEN,math_games,game_rounds
from telebot import TeleBot
bot = TeleBot(TOKEN)

def get_math(message):
    markup = ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, input_field_placeholder='input your language')
    text = "Выберите игру / Choose the game / Sceglie la giocca:"
    markup.add(*(KeyboardButton(game) for game in math_games))
    bot.send_message(message.chat.id, text, reply_markup=markup)

def get_the_game(message):
    match message.text:
        case 'калькулятор':
            return Math.calculator()
        case 'чётное/нечётное':
            return Math.is_even_game()
        case 'простое/сложное':
            return Math.is_prime()
        case 'прогрессия':
            return Math.progression()
        case 'НОД':
            return Math.generate_gcd_question()

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