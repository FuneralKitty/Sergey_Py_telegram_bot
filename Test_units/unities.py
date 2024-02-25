import json

with open('jjj.json', 'r') as f:
    date = json.load(f)

print(type(date))  # Выводим тип переменной date
new_date = {123123: 'language'}
new = date+new_date
# Ваши дальнейшие действия с переменной date

with open('jjj.json', 'w') as f:
    json.dump(date, f, indent=3)