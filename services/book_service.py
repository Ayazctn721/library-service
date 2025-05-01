from db import book_data
from utils.validation import validate_book_data
from models.book_model import Book
#! service = responsible for business logic, it interacts with models  and repositories
from repositories.book_repository import BookRepository


class BookService:
    @staticmethod
    def get_all_books():

        books = BookRepository.get_all_books()  # list of dictionaries
        if not books:
            return []
        return [Book(**b) for b in books]

    @staticmethod
    def get_book_by_id(book_id: str):
        book = BookRepository.get_book_by_id(book_id)
        return Book(**book) if book else None

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

        created_book = BookRepository.create_book(new_book)
        books = BookRepository.get_all_books()
        return [Book(**b) for b in books]

    @staticmethod
    def delete_book(book_id: str):
        deleted_book = BookRepository.delete_book(book_id)
        books = BookRepository.get_all_books()
        return True, [Book(**b) for b in books]

    @staticmethod
    def update_book(book_id: str, data: dict):
        updated_book = BookRepository.update_book(book_id, data)
        books = BookRepository.get_all_books()
        return Book(**updated_book), [Book(**b) for b in books]
