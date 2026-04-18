# db.py
import sqlite3

def get_connection():
    # check_same_thread=False is required for Streamlit's multi-threaded nature
    return sqlite3.connect("data.db", check_same_thread=False)

conn = get_connection()
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, input TEXT, result TEXT)")
conn.commit()

def create_default_user():
    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", ("admin", "admin123"))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def check_login(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()

def save_history(username, input_data, result):
    cursor.execute("INSERT INTO history (username, input, result) VALUES (?, ?, ?)", (username, input_data, result))
    conn.commit()

def get_history(username):
    cursor.execute("SELECT input, result FROM history WHERE username=? ORDER BY id DESC LIMIT 10", (username,))
    return cursor.fetchall()    