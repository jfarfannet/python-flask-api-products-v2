import pymysql
from contextlib import contextmanager

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Replace with your MySQL password
    'database': 'db01',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Database connection context manager
@contextmanager
def get_db_connection():
    connection = pymysql.connect(**DB_CONFIG)
    try:
        yield connection
    finally:
        connection.close()

# Initialize database
def init_db():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            # Create products table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    description TEXT,
                    price DECIMAL(10,2) NOT NULL,
                    stock INT NOT NULL
                )
            """)
            # Create clients table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombres VARCHAR(255) NOT NULL,
                    apellidos VARCHAR(255) NOT NULL,
                    correo VARCHAR(255) NOT NULL UNIQUE
                )
            """)
            conn.commit()