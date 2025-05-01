from flask import g, current_app
import psycopg2
from models.book_model import Book

book1 = Book(
    book_id="B_001",
    title="Martin Eden",
    author="Jack London",
    publication_year=1801,
    genre="Adventure",
    read_status="read",
    rating=4,
    notes="The story of a man who is trying to escape the world"
)

book2 = Book(
    book_id="B_002",
    title="The Monk who sold his ferrari",
    author="Robin Sharma",
    publication_year=1990,
    genre="Fiction",
    read_status="to-read",
    rating=4,
    notes="The story of the man who sold his ferrari"
)

book_data = [book1, book2]

# connect to PostgreSQL database and  Python can connect to it and can add data, read data, update data, delete data from the database


# g is used to store temporary data specific to a request,
# while current_app provides access to the current Flask application instance, allowing you to interact with the application's configuration and settings.


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname="flask_postgres_db",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
