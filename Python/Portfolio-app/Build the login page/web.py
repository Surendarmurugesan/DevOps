#
# Design the login form: Create an HTML or CSS template for the login form, including input fields for the username and password.
#
# Create a database: Set up a database to store user information, including usernames, passwords, and other relevant details.
#
# Validate user input: Use Python to validate the user's input and ensure that it meets the required format and criteria.
#
# Check the database for a matching username and password: Use Python to query the database for a matching username and password.
# If a match is found, proceed to the next step. If no match is found, display an error message.
#
# Redirect the user to the desired page: If the login is successful, use Python to redirect the user
# to the desired page or display a welcome message.

# Import required modules
import mysql.connector
from mysql.connector import Error

# Connect to the database
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='database_name',
                                         user='username',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)


# Validate the user input
def validate_login(username, password):
    if username == '' or password == '':
        return "Please enter both a username and password."
    elif len(password) < 8:
        return "Password must be at least 8 characters long."
    else:
        return "Valid"


# Check the database for a matching username and password
def check_login(username, password):
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


# Redirect the user to the desired page
def login_success(username):
    print("Welcome, {}!".format(username))
    # Redirect to desired page


# Main function to handle the login process
def login(username, password):
    validation_result = validate_login(username, password)
    if validation_result == "Valid":
        if check_login(username, password):
            login_success(username)
        else:
            print("Invalid username or password.")
    else:
        print(validation_result)


# Test the login function
login('suren', 'admin123')
