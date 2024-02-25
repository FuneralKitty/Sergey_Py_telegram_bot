import json

class DataManagement:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.get_json_data()

    def get_json_data(self):
        """Получение данных из JSON"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as data_file:
                return json.load(data_file)
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return {}


    def dump_json_data(self, message, key):
        """
        Обновление языка пользователя в файле JSON.
        """
        user_id = message.from_user.id
        new_value = message.text.lower()

        if user_id in self.data:
            self.data[user_id][key] = new_value
        else:
            self.data[user_id] = {key: new_value}

        try:
            with open(self.data_path, 'w', encoding='utf-8') as data_file:
                json.dump(self.data, data_file, indent=2)
            print('True')
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")
