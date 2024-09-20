import psycopg2
from psycopg2 import sql

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="hotel_management",
            user="abdirahman",
            password="37571598a",
            host="localhost"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
