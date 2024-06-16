import psycopg2
from config import Config

def get_db_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=Config.DATABASE_NAME,
            user=Config.DATABASE_USER,
            password=Config.DATABASE_PASSWORD,
            host=Config.DATABASE_HOST,
            port=Config.DATABASE_PORT
        )
        print("Connection to the database successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")

    return connection
