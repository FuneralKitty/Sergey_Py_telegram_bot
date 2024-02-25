import random
class Anya:
    age = 18
    name = 'Anya'
    instance = None
    hobbies = {'badminton','drawing','languages','math','programming'}
    def __new__(cls, *args, **kwargs):
        if Anya.instance is None:
            Anya.instance = super.__new__(cls)
            print("Anya was born")
    def __init__(self):
        pass
    @staticmethod
    def say_hello(message):
        user_name = message.from_user.first_name
        x = random.choice(['Hello', 'Hi', 'Привет', 'Добрый день'])
        return f'{x}, {user_name} my name is {Anya.name} and I`m here to help u'
    @staticmethod
    def say_goodbye(message):
        user_name = message.from_user.first_name
        x = random.choice(['bye', 'Goodbye', 'Ciao', 'пока'])
        return f'{x}, {user_name}'























# class Fast_Writer:
#     def __init__(self,text,level):
#         self.text = text
#         if 0 <= level <= 8:
#             self.level = 'newer'
#         if 8 < level <= 12:
#             self.level = 'middle'
#         if 12 < level <= 18:
#             self.level = 'oldboy'
#     def get_text(self,length: int, lang: str ='ru') -> str:
#         start = random.randint(0,)
#         end = start + length
#         status = 0
#         if lang == 'ru':
#             try:
#                 with open(self.text,'r') as f:
#                     text = f.read()
#                     print(text)
#                     return text[start:end]
#
#             except FileNotFoundError as f:
#                 status = 400
#                 raise FileNotFoundError(f'Search for file! Error: {f}')
#             finally:
#                 return status
#     def make_test(self):
#         lvl = self.level
#         if lvl == 'newer':
#             text = self.get_text(20)
#             return text
#         if lvl == 'middle':
#             text = self.get_text(35)
#             return text
#         if lvl == 'oldboy':
#             text = self.get_text(60)
#             return text[:60]
#
#
#
#
#
#
#
#
#
# import os
# import json
#
# # Пример использования
# class Text_Redactor:
#     def make_path(self) -> str:
#         d = Path().absolute()/'Textes'/self.lang
#         with open(d,'r',encoding='utf-8') as f:
#             d = json.load(f)
#             return d
#      # def write_to_json(self,):
#     """сделать функцию для админского дополнения файлов по пути"""
#      #     d =
#     def __init__(self, text: list, author: str, genre: str, language: str) -> None:
#          match language:
#              case 'ru':
#                  self.lang = 'ru.json'
#              case 'eng':
#                  self.lang = 'eng.json'
#              case 'ital':
#                  self.lang = 'ital.json'
#          self.text = text
#          self.author = author
#          self.genre = genre
#     def greeting_ru(self, name):
#         """в качестве name будем использовать считку имени пользователя через телебот"""
#         match self.lang:
#             case 'ru.json':
#                 return f'Привет, {name}!'
#             case 'eng.json':
#                 return f'Hello, {name}!'
#             case 'ital.json':
#                 return f'Ciao caro, {name}!'
#
#     @staticmethod
#     def count_time():
#         d = time()
#         sleep(10)
#         v = time()
#         print(int(v - d))
#
#
# print(Text_Redactor(1,2,3,'ru').make_path())
# Text_Redactor.count_time()