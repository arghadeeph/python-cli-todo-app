import mysql.connector


# Connect to MySQL database

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  # Change this!
        database="todo"
    )
    return conn
