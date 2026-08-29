import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.db")


def get_login_data_for_login():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, result FROM Login_Credentials;")
    return cursor.fetchall()


def get_login_data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password "
                   "FROM Login_Credentials WHERE username = 'standard_user' OR username = 'problem_user';")
    return cursor.fetchall()


def get_sort_data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Sort;")
    name = cursor.fetchall()
    name_list = [t[0] for t in name]
    return name_list
