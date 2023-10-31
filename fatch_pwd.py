import mysql.connector
import bcrypt

# Function to create a database connection
def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123root",
        database="connection"
    )

# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert user data into the database
    connection = create_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    data = (username, hashed_password)

    cursor.execute(insert_query, data)
    connection.commit()

    print("User registered successfully.")
    cursor.close()
    connection.close()

# Function to authenticate a user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Retrieve user data from the database
    connection = create_db_connection()
    cursor = connection.cursor()

    select_query = "SELECT username, password FROM users WHERE username = %s"
    data = (username,)

    cursor.execute(select_query, data)
    user_data = cursor.fetchone()

    if user_data:
        stored_username, stored_password = user_data

        # Check if the entered password matches the stored hashed password
        # stored_password = b'$2b$12$zDJO8gZM9EFC88OC3aKXdeLR0gVXTgoEheP.hsGeeKCDTRWfg9S.O'
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful. Welcome,", username)
        else:
            print("Incorrect password. Access denied.")
    else:
        print("User not found. Access denied.")

    cursor.close()
    connection.close()

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")

    choice = input("Select an option: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
