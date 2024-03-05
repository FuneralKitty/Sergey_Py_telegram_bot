from src import randint, choice

class Math:
    def __init__(self):
        print('created')

    def calculator(self,hardness, language=None):
        operator = choice(['+', '-', '*']) #временно удалено деление
        to_message, evaluated = self.make_calculator_with_difficulties(hardness, operator)
        return to_message, evaluated
    def is_prime_game(self,hardness):
        to_message = self.is_prime_difficulties(hardness)
        result = self.is_prime(to_message)
        if result:
            result = ['Yes/Да/Si','Yes','yes','да','si','Si']
        if not result:
            result = ['No/Нет', 'No', 'no', 'нет','Нет']
        return to_message, result

    def make_calculator_with_difficulties(self, hardness, operator):
        '''Возвращает str и int формат для калькулятора'''
        if hardness in ['легко','low','facile']:
            a, b = 1, 100
            values = [str(randint(a, b)) for _ in range(3)]
            result_in_str = f'{operator}'.join(values)
            result_in_int = eval(result_in_str)
            return result_in_str, result_in_int
        if hardness in ['cложно', 'medium', 'media']:
            if operator == '*' or operator == '//':
                a, b = 15, 150
                values = [str(randint(a, b)) for _ in range(4)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int
            if operator == '+' or operator == '-':
                a, b = 100, 1000
                values = [str(randint(a, b)) for _ in range(4)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int
        if hardness in ['тяжело', 'hard', 'difficile']:
            if operator == '*' or operator == '//':
                a, b = 100, 500
                values = [str(randint(a, b)) for _ in range(4)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int
            if operator == '+' or operator == '-':
                a, b = 1000, 15000
                values = [str(randint(a, b)) for _ in range(4)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int
        if hardness in ['максимальная','max','massimo']:
            if operator == '*' or operator == '//':
                a, b = 400, 10000
                values = [str(randint(a, b)) for _ in range(4)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int
            if operator == '+' or operator == '-':
                a, b = 1000, 1000000
                values = [str(randint(a, b)) for _ in range(8)]
                result_in_str = f'{operator}'.join(values)
                result_in_int = eval(result_in_str)
                return result_in_str, result_in_int

    def is_even_game(self, hardness):
        difficulty_ranges = {
            'легко': (10, 50),
            'low': (10, 50),
            'facile': (10, 50),
            'cложно': (51, 150),
            'medium': (51, 150),
            'media': (51, 150),
            'тяжело': (100, 500),
            'hard': (100, 500),
            'difficile': (100, 500),
            'максимальная': (500, 1500),
            'max': (500, 1500),
            'massimo': (500, 1500)
        }

        if hardness in difficulty_ranges:
            a, b = difficulty_ranges[hardness]
            generated_num_for_question = randint(a, b)
            is_even = generated_num_for_question % 2 == 0
            answer = ['si', 'да', 'yes'] if is_even else ['no', 'нет']
            return generated_num_for_question, answer
        else:
            raise ValueError('Invalid hardness level')


    def generate_gcd_question(self,hardness):
        a, b = None, None
        if hardness in ['легко','low','facile']:
                a,b = 10,100
        if hardness in ['cложно', 'medium', 'media']:
                a, b = 50, 200
        if hardness in ['тяжело', 'hard', 'difficile']:
                a, b = 200, 450
        if hardness in ['максимальная', 'max', 'massimo']:
                a, b = 451, 3888
        answer = int(self.calculate_gcd(a,b))
        question = f'{a} {b}'

        return question, answer

    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def is_prime_difficulties(self, hardness):
        difficulties = {
            'легко': (1, 100),
            'low': (1, 100),
            'facile': (1, 100),
            'cложно': (100, 888),
            'medium': (100, 888),
            'media': (100, 888),
            'тяжело': (999, 10000),
            'hard': (999, 10000),
            'difficile': (999, 10000),
            'максимальная': (10001, 99999),
            'max': (10001, 99999),
            'massimo': (10001, 99999)
        }
        if hardness in difficulties:
            a = randint(*difficulties[hardness])
            return a
        else:
            # Handle unexpected values of hardness
            raise ValueError(f"Unexpected value of hardness: {hardness}")

    def is_prime(self,a):
        if a < 2:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    def progression(self, hardness, length=10):
        difficulty_ranges = {
            'легко': (1, 10, 1, 10),
            'low': (1, 10, 1, 10),
            'facile': (1, 10, 1, 10),
            'cложно': (1, 150, 50, 300),
            'medium': (1, 150, 50, 300),
            'media': (1, 150, 50, 300),
            'тяжело': (1000, 5000, 100, 1000),
            'hard': (1000, 5000, 100, 1000),
            'difficile': (1000, 5000, 100, 1000),
            'максимальная': (1000, 10000, 1000, 9999),
            'max': (1000, 10000, 1000, 9999),
            'massimo': (1000, 10000, 1000, 9999)
        }

        if hardness in difficulty_ranges:
            start_min, start_max, step_min, step_max = difficulty_ranges[hardness]
            start = randint(start_min, start_max)
            step = randint(step_min, step_max)

            if hardness in ['тяжело', 'hard', 'difficile', 'максимальная', 'max', 'massimo']:
                length = 15 if 'тяжело' in hardness else 20
        else:
            raise ValueError('Invalid hardness level')

        end = start + (length - 1) * step
        hidden_index = randint(0, length - 1)
        progression = list(range(start, end + step, step))
        hidden_value = progression[hidden_index]
        progression[hidden_index] = '..'
        progression_str = ' '.join(map(str, progression))

        return progression_str, int(hidden_value)

    def get_description(self,language: str, function: str=None):
        '''Get different descriptions in different languages
           for different functions'''
        if function == 'calculator':
            match language:
                case 'русский':
                    return (f'''Добро пожаловать в тренировочный модуль!
                        Сложность зависит напрямую от выбранной вами ранее
                        Для смены сложности: Нажмите Menu (в настройках бота), далее /hardness и выбираете
                        нужную вам сложность. Результаты математических операций полностью завязаны на реальной математике
                        если число должно быть отрицательным, как и в обычной математике пишите минус перед ним, пример: 50 - 55,
                        ответ: -5. При делении округляйте до 2 десятичных знаков: 88/1/61 1.44 (26229508196722 < опускаете)'''
                            )

                case 'english':
                    return '''Welcome to the training module!
                            The difficulty depends directly on the one you have previously chosen.
                            To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose
                            the difficulty you need. Mathematical operations are completely real; if the number should be negative,
                            just like in regular math, write a minus before it, for example: 50 - 55, answer: -5.
                            When dividing, round to 2 decimal places: 88/1/61 1.44 (26229508196722 < omit)'''

                case 'italiano':
                    return '''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno. Le operazioni matematiche sono completamente reali; se il numero deve essere negativo,
                            proprio come nella matematica normale, scrivi un meno davanti, ad esempio: 50 - 55, risposta: -5.
                            Quando si divide, arrotondare a 2 decimali: 88/1/61 1.44 (26229508196722 < omettere)'''
        if function == 'is_even_game':
            match language:
                case 'русский':
                    return f'''Добро пожаловать в тренировочный модуль!
                            Сложность зависит напрямую от выбранной вами ранее
                            Для смены сложности: Нажмите Menu (в настройках бота), далее /hardness и выбираете
                            нужную вам сложность.Ответьте "да", если число четное, в противном случае ответьте "нет"(без кавычек)'''
                case 'english':
                    return f'''Welcome to the training module!
                            The difficulty depends directly on the one you have previously chosen.
                            To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose
                            the difficulty you need. Answer "yes" if the number is even, otherwise answer "no" '''

                case 'italiano':
                    return f'''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno. Rispondi "sì" se il numero è pari, altrimenti rispondi "no".'''

        if function == 'generate_gcd_question':
            match language:
                case 'русский':
                    return f'''Добро пожаловать в тренировочный модуль!
                                Сложность зависит напрямую от выбранной вами ранее.
                                Чтобы изменить сложность: перейдите в Меню (в настройках бота), затем выберите /hardness и укажите желаемую сложность.
                                Найдите наибольший общий делитель заданных чисел.'''
                case 'english':
                    return f'''Welcome to the training module!
                                The difficulty depends directly on the one you have previously chosen.
                                To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose the difficulty you need.
                                Find the greatest common divisor of given numbers.'''
                case 'italiano':
                    return f'''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno.Trova il massimo comune divisore dei numeri dati.'''
        if function == 'is_prime_game':
            match language:
                case 'русский':
                    return f'''Добро пожаловать в тренировочный модуль!
                                Сложность зависит напрямую от выбранной вами ранее.
                                Чтобы изменить сложность: перейдите в Меню (в настройках бота), затем выберите /hardness и укажите желаемую сложность.
                                Ответьте да/yes/si если число простое. Иначе отвечайте нет/no.'''
                case 'english':
                    return f'''Welcome to the training module!
                                The difficulty depends directly on the one you have previously chosen.
                                To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose the difficulty you need.
                                Answer yes/si/да if the number is prime. Otherwise, answer no.
                                '''
                case 'italiano':
                    return f'''Benvenuto nel modulo di allenamento!
                                La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                                Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli la difficoltà desiderata.
                                Rispondi sì/yes/да se il numero è primo. Altrimenti, rispondi no.
                                '''
        if function == 'progression':
            match language:
                case 'русский':
                    return f'''Добро пожаловать в тренировочный модуль!
                                Сложность зависит напрямую от выбранной вами ранее.
                                Чтобы изменить сложность: перейдите в Меню (в настройках бота), затем выберите /hardness и укажите желаемую сложность.
                                Какое число пропущено в прогрессии?'''
                case 'english':
                    return f'''Welcome to the training module!
                                The difficulty depends directly on the one you have previously chosen.
                                To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose the difficulty you need.
                                What number is missing in the progression?'''
                case 'italiano':
                    return f'''Benvenuto nel modulo di allenamento!
                                La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                                Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli la difficoltà desiderata.
                                Quale numero manca nella progressione?'''
