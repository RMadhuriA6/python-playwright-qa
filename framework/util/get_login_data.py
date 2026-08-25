import sqlite3


def get_login_data():
    conn = sqlite3.connect("framework/data/login_test_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, result FROM Login_Credentials;")
    return cursor.fetchall()
