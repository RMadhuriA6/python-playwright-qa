import sqlite3

conn = sqlite3.connect("login_test_data.db")

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Login_Credentials(username VARCHAR(20), password VARCHAR(20), result VARCHAR(75));")
# cursor.execute("INSERT INTO Login_Credentials(username, password, result) VALUES('user', 'secret0', 'Invalid username with invalid password');")
# cursor.execute("UPDATE Login_Credentials SET result = 'Locked out user' WHERE username = 'locked_out_user';")

cursor.execute("SELECT * from Login_Credentials;")

login_table = cursor.fetchall()
conn.commit()
for row in login_table:
    print(row)

print(('Empty username with valid password' or 'Both fields Empty'))
