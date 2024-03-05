class All_messages:
    def __init__(self, message, lang):
        self.version = 1.02
        self.dictionary = {'ru_description_start':
                               f'''Привет, {message.from_user.first_name}!
                               Я являюсь помощником первого уровня, а так-же
                               небольшой образовательной платформой для изучения итальянского,английского
                               математики и программирования. Я говорю на
                               русском, английском и итальянском. 
                               Выберите язык нашего общения!
                               Версия модели: {self.version}'''

                            }
                            'eng_description_start':


    def description(self, message):
        greeting_message = self.description_ru_start.format(message=message)