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

def get_user_data_by_param(user_id, param):
    cur, conn = establish_connection()

    if param == 'language':
        cur.execute("SELECT language FROM person WHERE user_id = %s", (user_id,))
    elif param == 'hardness':
        cur.execute("SELECT hardness FROM person WHERE user_id = %s", (user_id,))

    user_data = cur.fetchone()
    conn.commit()

    if user_data:
        return user_data[0]
    else:
        return None
