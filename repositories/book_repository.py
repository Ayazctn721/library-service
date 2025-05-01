from db import get_db
from psycopg2.extras import RealDictCursor


class BookRepository:
    @staticmethod
    def get_all_books():
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM books")
            return cursor.fetchall()

    @staticmethod
    def get_book_by_id(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT * FROM books WHERE book_id = %s", (book_id,))
            return cursor.fetchone()

    @staticmethod
    def create_book(book):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "INSERT INTO books (book_id, title, author, publication_year, genre, read_status, rating, notes, uuid, created_at) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
                "RETURNING *",
                (book.book_id, book.title, book.author, book.publication_year, book.genre, book.read_status, book.rating, book.notes, book.uuid, book.created_at))
            connection.commit()
            return cursor.fetchone()

    @staticmethod
    def delete_book(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "DELETE FROM books WHERE book_id = %s RETURNING *;", (book_id,))
            deleted_book = cursor.fetchone()
            connection.commit()
            return deleted_book

    @staticmethod
    def update_book(book_id, book):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "UPDATE books SET book_id = %s, title = %s, author = %s, publication_year = %s, genre = %s, read_status = %s, rating = %s, notes = %s, uuid = %s, created_at = %s "
                "WHERE book_id = %s "
                "RETURNING *;",
                (book["book_id"], book["title"], book["author"], book["publication_year"], book["genre"], book["read_status"], book["rating"], book["notes"], book["uuid"], book["created_at"], book_id))
            update_book = cursor.fetchone()
            connection.commit()
            return update_book

    @staticmethod
    def get_read_status(read_status):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT * FROM books WHERE read_status = %s", (read_status,))
            return cursor.fetchall()
