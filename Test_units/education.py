from random import *
from constants import game_rounds
class Anya:
    def __init__(self):
        self.x = randint(0,100)
        self.y = randint(0,100)
    def make_random(self):
        return randint(0,100), randint(0,100)
    def calculator(self):
        operator = choice(['+', '-', '*', '/'])
        d = self.make_random()
        description = 'What is the result of the expression?'
        if operator == '+':
            operation = str(d[0] + d[1])
        elif operator == '-':
            operation = str(d[0] + d[1])
        elif operator == '*':
            operation = str(d[0] + d[1])
        elif operator == '/':
            operation = str(d[0] + d[1])
        quest = f'{d[0]} {operator} {d[1]}'
        return quest, operation, description
math = Anya()
print(math.calculator())
print(math.calculator())
print(math.calculator())

def start_game():
    user_score = 0
    operation, result, description = math = Anya().calculator()
    bot.send_message(message.chat.id, description)
    while user_score < game_rounds:
        operation, result = Anya().calculator()
        print('Question:', operation)
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