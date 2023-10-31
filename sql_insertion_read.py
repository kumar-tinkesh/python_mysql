import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "mysql@123root",
    "database": "randomdata1",
}
connection = mysql.connector.connect(**db_config)

cursor = connection.cursor()

# name = input("Enter your name: ")
# email = input("Enter your email: ")

# insert_query = "INSERT INTO user_data (name, email) VALUES (%s, %s)"

# cursor.execute(insert_query, (name, email))

cursor.execute("SELECT * FROM user_data")

data = cursor.fetchall()

for i in data:
    print(i)

connection.commit()

cursor.close()
connection.close()

