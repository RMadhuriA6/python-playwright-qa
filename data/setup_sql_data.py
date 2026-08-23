import sqlite3

conn = sqlite3.connect("test_data.db")

cursor = conn.cursor()

# cursor.execute("CREATE TABLE Orders(order_id VARCHAR, username VARCHAR(50), status VARCHAR(15), amount DECIMAL(10,2));")
# cursor.execute("INSERT INTO Orders(order_id, username, status, amount) VALUES('A5', 'Madhuri', 'Shipping', 600.00);")
# cursor.execute("INSERT INTO Orders(order_id, username, status, amount) VALUES('A6', 'Ravi', 'Cancelled', 29.50);")
# cursor.execute("INSERT INTO Orders(order_id, username, status, amount) VALUES('A7', 'Teja', 'Payment Done', 156.22);")
# cursor.execute("INSERT INTO Orders(order_id, username, status, amount) VALUES('A8', 'Lakshmi', 'Cancelled', 14.46);")
# cursor.execute("INSERT INTO Orders(order_id, username, status, amount) VALUES('A9', 'Lakshmi', 'delivered', 02.50);")
#
# cursor.execute("CREATE TABLE Users(user_id VARCHAR, username VARCHAR(50));")
# cursor.execute("INSERT INTO Users(user_id, username) VALUES('U1', 'Madhuri');")
# cursor.execute("INSERT INTO Users(user_id, username) VALUES('U2', 'Teja');")
# cursor.execute("INSERT INTO Users(user_id, username) VALUES('U3', 'Ravi');")
# cursor.execute("INSERT INTO Users(user_id, username) VALUES('U4', 'Lakshmi');")
cursor.execute("SELECT Orders.order_id, Users.username, Orders.status, Orders.amount "
               "FROM Users "
               "LEFT JOIN Orders "
               "WHERE Users.username = Orders.username;")

Order_Status = cursor.fetchall()
conn.commit()
for row in Order_Status:
    print(row)
