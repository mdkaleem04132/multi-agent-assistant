import mysql.connector
from mysql.connector import Error

def connect_db():
    """Connect to the MySQL database and return the connection object."""
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Change if your DB is remote
            user="root",            # Your MySQL username
            password="your_password",  # Your MySQL password
            database="multi_agent_ai"   # Your database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None