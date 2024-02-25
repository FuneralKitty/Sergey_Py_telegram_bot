from src import randint,choice


class Math:
    def __init__(self, hardness):
        self.hardness = hardness
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

    def is_even_game(self):
        generated_num_for_question = self.x
        description = 'Answer "yes" if the number is even, otherwise answer "no".'

        def is_even():
            nonlocal generated_num_for_question
            return True if generated_num_for_question % 2 == 0 else False

        if is_even():
            operation = 'yes'
        else:
            operation = 'no'

        return generated_num_for_question, operation, description

    def generate_gcd_question(self):
        description = 'Find the greatest common divisor of given numbers.'
        first_gcd_num = self.x
        second_gcd_num = self.y
        answer = str(self.calculate_gcd(first_gcd_num, second_gcd_num))
        question = f'{first_gcd_num} {second_gcd_num}'

        return question, answer, description

    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def is_prime_game(self):
        result, prime_number = self.is_prime()
        description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
        if result is True:
            operation = 'yes'
        else:
            operation = 'no'

        return prime_number, operation, description

    def is_prime(self):
        prime_number = self.x
        n = 0

        for i in range(2, prime_number // 1):
            if prime_number % i == 0:
                n = n + 1
        if n <= 0:
            result = True
        else:
            result = False
        return result, prime_number

    def progression(self,length=10):
        description = 'What number is missing in the progression?'
        start = self.x  # Adjust the range as needed
        step = self.y  # Adjust the range as needed
        end = start + (length - 1) * step
        hidden_index = randint(0, length - 1)
        progression = list(range(start, end + step, step))
        hidden_value = progression[hidden_index]
        progression[hidden_index] = '..'
        progression_str = ' '.join(map(str, progression))
        return progression_str, str(hidden_value), description


