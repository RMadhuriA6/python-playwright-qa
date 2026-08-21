import sqlite3
import pytest


def get_order_status(username):
    conn = sqlite3.connect("test_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders WHERE username = ?;", (username,))
    order_status = cursor.fetchall()
    for row in order_status:
        print()
        print(row)


@pytest.mark.parametrize("username",[("Madhuri"), ("Ravi"), ("Teja"), ("Lakshmi")])
def test_sql_status(username):
    get_order_status(username)