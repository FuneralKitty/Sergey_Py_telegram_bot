from src import randint, choice

class Math:
    def __init__(self):
        print('created')

    def calculator(self,hardness, language=None):
        operator = choice(['+', '-', '*', '/'])
        description = self.get_description(language, function='calculator')
        to_message, evaluated = self.make_calculator_with_difficulties(hardness, operator)
        return description, to_message, evaluated

    def get_description(self,language, function=None):
        '''Get different descriptions in different languages
           for different functions'''
        if function == 'calculator':
            match language:
                case 'russian':
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

                case 'italian':
                    return '''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno. Le operazioni matematiche sono completamente reali; se il numero deve essere negativo,
                            proprio come nella matematica normale, scrivi un meno davanti, ad esempio: 50 - 55, risposta: -5.
                            Quando si divide, arrotondare a 2 decimali: 88/1/61 1.44 (26229508196722 < omettere)'''
        if function == 'is_even_game':
            match language:
                case 'russian':
                    return f'''Добро пожаловать в тренировочный модуль!
                            Сложность зависит напрямую от выбранной вами ранее
                            Для смены сложности: Нажмите Menu (в настройках бота), далее /hardness и выбираете
                            нужную вам сложность.Ответьте "да", если число четное, в противном случае ответьте "нет"(без кавычек)'''
                case 'english':
                    return f'''Welcome to the training module!
                            The difficulty depends directly on the one you have previously chosen.
                            To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose
                            the difficulty you need. Answer "yes" if the number is even, otherwise answer "no" '''

                case 'italian':
                    return f'''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno. Rispondi "sì" se il numero è pari, altrimenti rispondi "no".'''

        if function == 'generate_gcd_question':
            match language:
                case 'russian':
                    return f'''Добро пожаловать в тренировочный модуль!
                                Сложность зависит напрямую от выбранной вами ранее.
                                Чтобы изменить сложность: перейдите в Меню (в настройках бота), затем выберите /hardness и укажите желаемую сложность.
                                Найдите наибольший общий делитель заданных чисел.'''
                case 'english':
                    return f'''Welcome to the training module!
                                The difficulty depends directly on the one you have previously chosen.
                                To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose the difficulty you need.
                                Find the greatest common divisor of given numbers.'''
                case 'italian':
                    return f'''Benvenuto nel modulo di allenamento!
                            La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                            Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli
                            la difficoltà di cui hai bisogno.Trova il massimo comune divisore dei numeri dati.'''
        if function == 'is_prime_game':
            match language:
                case 'russian':
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
                case 'italian':
                    return f'''Benvenuto nel modulo di allenamento!
                                La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                                Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli la difficoltà desiderata.
                                Rispondi sì/yes/да se il numero è primo. Altrimenti, rispondi no.
                                '''
        if function == 'progression':
            match language:
                case 'russian':
                    return f'''Добро пожаловать в тренировочный модуль!
                                Сложность зависит напрямую от выбранной вами ранее.
                                Чтобы изменить сложность: перейдите в Меню (в настройках бота), затем выберите /hardness и укажите желаемую сложность.
                                Какое число пропущено в прогрессии?'''
                case 'english':
                    return f'''Welcome to the training module!
                                The difficulty depends directly on the one you have previously chosen.
                                To change the difficulty: Click on Menu (in the bot settings), then /hardness and choose the difficulty you need.
                                What number is missing in the progression?'''
                case 'italian':
                    return f'''Benvenuto nel modulo di allenamento!
                                La difficoltà dipende direttamente da quella che hai scelto in precedenza.
                                Per cambiare la difficoltà: Clicca su Menu (nelle impostazioni del bot), poi /hardness e scegli la difficoltà desiderata.
                                Quale numero manca nella progressione?'''

    def make_calculator_with_difficulties(self,hardness, operator):
        '''Возвращает str и int формат для калькулятора'''
        match hardness:
            case 'low':
                a, b = 1, 100
                values = [str(randint(a, b)) for _ in range(3)]
            case 'medium':
                if operator == '*' or operator == '//':
                    a, b = 15, 150
                    values = [str(randint(a, b)) for _ in range(4)]
                if operator == '+' or operator == '-':
                    a, b = 100, 1000
                    values = [str(randint(a, b)) for _ in range(4)]
            case 'hard':
                if operator == '*' or operator == '//':
                    a, b = 100, 500
                    values = [str(randint(a, b)) for _ in range(4)]
                if operator == '+' or operator == '-':
                    a, b = 1000, 15000
                    values = [str(randint(a, b)) for _ in range(4)]
            case 'max':
                if operator == '*' or operator == '//':
                    a, b = 400, 10000
                    values = [str(randint(a, b)) for _ in range(4)]
                if operator == '+' or operator == '-':
                    a, b = 1000, 1000000
                    values = [str(randint(a, b)) for _ in range(8)]
        result_in_str = f'{operator}'.join(values)
        result_in_int = eval(result_in_str)
        return result_in_str, result_in_int

    def is_even_game(self,hardness):
        match hardness:
            case 'low':
                a,b = 10,50
            case 'medium':
                a, b = 51, 150
            case 'hard':
                a, b = 100, 500
            case 'max':
                a, b = 500, 1500
        generated_num_for_question = randint(a, b)
        answer = 'yes' if generated_num_for_question % 2 == 0 else 'no'
        '''при считывании ответа сделать проверку на ['si','да','yes'] '''
        return generated_num_for_question, answer


    def generate_gcd_question(self,hardness):
        match hardness:
            case 'low':
                a,b = 10,100
            case 'medium':
                a, b = 50, 200
            case 'hard':
                a, b = 200, 450
            case 'max':
                a, b = 451, 3888
        answer = str(self.calculate_gcd(a,b))
        question = f'{a} {b}'

        return question, answer

    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def is_prime_game(self,hardness):
        match hardness:
            case 'low':
                a = randint(1,100)
            case 'medium':
                a = randint(100,888)
            case 'hard':
                a = randint(999, 10000)
            case 'max':
                a = randint(10001, 99999)
        result, prime_number = self.is_prime(a)
        '''answers'''
        if result:
            operation = 'yes'
        else:
            operation = 'no'

        return prime_number, operation

    def is_prime(self,a):
        prime_number = a
        n = 0
        for i in range(2, prime_number // 1):
            if prime_number % i == 0:
                n = n + 1
        if n <= 0:
            result = True
        else:
            result = False
        return result, prime_number


    def progression(self,hardness,length=10):
        match hardness:
            case 'low':
                start = randint(1, 10)
                step = randint(1, 10)
            case 'medium':
                start = randint(1, 150)
                step = randint(50, 300)
            case 'hard':
                start = randint(1000, 5000)
                step = randint(100, 1000)
                length = 15
            case 'max':
                start = randint(1000, 10000)
                step = randint(1000, 9999)
                length = 20
            case _:
                raise ValueError('Invalid hardness level')

        end = start + (length - 1) * step
        hidden_index = randint(0, length - 1)
        progression = list(range(start, end + step, step))
        hidden_value = progression[hidden_index]
        progression[hidden_index] = '..'
        progression_str = ' '.join(map(str, progression))

        return progression_str, str(hidden_value)

