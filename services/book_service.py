from db import book_data
from utils.validation import validate_book_data
from models.book_model import Book
#! service = responsible for business logic, it interacts with models  and repositories


class BookService:
    @staticmethod
    def get_all_books():
        return book_data

    @staticmethod
    def get_book_by_id(book_id: str):
        for book in book_data:  # book_data is a list
            if book.book_id == book_id:
                return book
        return None

    @staticmethod
    def create_book(data: dict):
        error = validate_book_data(data)
        if error:
            return error

        new_book = Book(
            book_id=data.get("book_id"),
            title=data.get("title"),
            author=data.get("author"),
            publication_year=data.get("publication_year"),
            genre=data.get("genre"),
            read_status=data.get("read_status"),
            rating=data.get("rating"),
            notes=data.get("notes"),
        )

        # add the book to the database
        book_data.append(new_book)
        return book_data

    @staticmethod
    def delete_book(book_id):
        for book in book_data:
            if book.book_id == book_id:
                book_data.remove(book)
                return True, book_data

        return False, None
