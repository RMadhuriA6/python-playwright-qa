import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "test_data.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Sort(value VARCHAR(20), name VARCHAR(20));")
# cursor.execute("INSERT INTO Sort(value, name) VALUES('az', 'Name (A to Z)');")

cursor.execute("UPDATE Login_Credentials "
               "SET username = 'locked_out_user' "
               "WHERE result = 'Valid username with Empty password'"
               "OR result = 'Valid username with invalid password';")

cursor.execute("SELECT * FROM Login_Credentials WHERE username = 'standard_user' OR username = 'problem_user';")

# cursor.execute("SELECT * from Sort;")
sort_table = cursor.fetchall()
conn.commit()

for row in sort_table:
    print(row)
