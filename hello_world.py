class Anya:
    age = 18
    nationality = "North America"
    hobbies = ['voleball','soccer','tenis']
    def __init__(self,name,age,nationality,hobbies):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.hobbies = hobbies
    def say_hello(self):
        return f'Hello, my name is {self.name} and I`m here to help u'

    def arithmetic(self,first_num: int,second_num: int,operation:  'str'):
        result1 = 'Operation result is: '
        result2 = 'Вы передали следующие значения: '
        try:
            if operation != any(['+','-','*','/']):
                raise ValueError
        finally:
            if operation == '+':
                return (f'{result1}{first_num + second_num}',f'{result2}{first_num},{second_num},операция - сложение ')
            if operation == '-':
                return (f'Operation result is: {first_num - second_num}',f'Вы передали следующие значения: {first_num},{second_num}, операция - вычетание')
            if operation == '/':
                return (f'Operation result is: {first_num / second_num}',f'Вы передали следующие значения: {first_num},{second_num}, операция - деление')
            if operation == '*':
                return (f'Operation result is: {first_num * second_num}',f'Вы передали следующие значения: {first_num},{second_num}, операция - умножение')


b = Anya('Anya',18,'North America',['soccer','tenis'])
print(b.say_hello())
result = b.arithmetic(12,13,'+')
print(f'''{result[0]}
{result[1]}''')
