import psycopg2
import telebot
from constants import TOKEN
import datetime

bot = telebot.TeleBot(TOKEN)

def establish_connection():
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='postgres',
            user='postgres',
            password='msivg249q1a',
            port=5432
        )
        cur = conn.cursor()
        return cur, conn
    except psycopg2.Error as e:
        print("Error:", e)

# Creating a new table in the database
def create_user_table():
    cur, conn = establish_connection()
    cur.execute("""CREATE TABLE IF NOT EXISTS person (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255),
        user_id BIGINT,
        language VARCHAR(255),
        hardness VARCHAR(255),
        win_count INT
    )""")
    cur.close()
    conn.commit()
create_user_table()
# Function to insert data into the database
def insert_into_database(user_id, user_name, language, hardness, win_count):
    cur, conn = establish_connection()
    cur.execute("INSERT INTO person (user_id, user_name, language, hardness, win_count) VALUES (%s, %s, %s, %s, %s)",
                (user_id, user_name, language, hardness, win_count))
    conn.commit()
def update_user_params(message, param):
    user_id = message.from_user.id
    cur, conn = establish_connection()
    new_value = message.text
    if param == 'language':
        cur.execute("UPDATE person SET language = %s WHERE user_id = %s",
                    (new_value, user_id))
        conn.commit()
    elif param == 'hardness':
        cur.execute("UPDATE person SET hardness = %s WHERE user_id = %s",
                    (new_value, user_id))
        conn.commit()
    elif param == 'win_count':
        cur.execute("UPDATE person SET win_count = %s WHERE user_id = %s",
                    (new_value, user_id))
        conn.commit()
# Function to check if a user already exists in the database
def check_existing_user(user_id):
    cur, conn = establish_connection()
    cur.execute("SELECT id FROM person WHERE user_id = %s", (user_id,))
    existing_user = cur.fetchone()
    conn.commit()
    return existing_user

# Handler for /start command
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message(message.chat.id, "Привет! Отправь мне сообщение, чтобы узнать время его получения.")
#
# # Handler for all incoming text messages
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     message_date = datetime.datetime.fromtimestamp(message.date)
#     formatted_date = message_date.strftime("%Y-%m-%d %H:%M:%S")
#     bot.send_message(message.chat.id, f"Ваше сообщение было получено {formatted_date}.")
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     language = 'russian'  # Example value, change as needed
#     hardness = 'low'  # Example value, change as needed
#     win_count = 0  # Example value, change as needed
#     existing_user = check_existing_user(user_id)
#     if not existing_user:
#         insert_into_database(user_id, user_name, language, hardness, win_count)
#         bot.send_message(message.chat.id, "Данные пользователя добавлены в базу данных.")
#     else:
#         bot.send_message(message.chat.id, "Пользователь уже существует в базе данных.")
#     print('True')
#     update_user_params(message,'language','english')
# bot.polling(none_stop=True)