from flask import Blueprint, request, jsonify
from services.book_service import BookService
# Blueprint allows us creat multiple different routes
# Helps split your code into smaller, manageable parts
# Makes your project more readable and easier to maintain

#! Controller: take HTTP request, interact with services, provide meaningful responses

book_bp = Blueprint('books', __name__, url_prefix='/api')
# created a blueprint named book_bp and put inside /books endpoint


@book_bp.route('/books', methods=['GET'])
def get_books():
    books = BookService.get_all_books()
    return jsonify([book.to_dict() for book in books])
# flask does not know how to convert a python object to json
# to_dict(): it lets that object posible to be convert to JSON


@book_bp.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404


@book_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if not data:
        return jsonify({"error": "data cannot be empty"}), 400
    books = BookService.create_book(data)

    if not isinstance(books, list):
        return jsonify(books), 400

    response = {
        "success": "Successfully added book",
        "books": [book.to_dict() for book in books]
    }

    return jsonify(response)


@book_bp.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    result, books = BookService.delete_book(book_id)
    if not result:
        return jsonify({"error": "Book not found"}), 404
    responce = {
        "success": f"Successfully deleted book with book_id: {book_id}",
        "books": [book.to_dict() for book in books]
    }
    return jsonify(responce)
