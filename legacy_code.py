from flask import Flask, jsonify, render_template, request

app = None  # it does not complain

# data source
books = [
    {"book_id": "B_001", "title": "Martin Eden", "author": "Jack London", "publication_year ": 1901, "genre": "Adventure",
        "read_status": "read", "rating": 4, "notes": "The story of a man who is trying to escape the world"},
    {"book_id": "B_002", "title": "The Monk who sold his ferrari", "author": "Robin Sharma", "publication_year ": 1990,
        "genre": "Fiction", "read_status": "to-read", "rating": 4, "notes": "The story of the man who sold his ferrari"},
    {"book_id": "B_003", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year ": 1988, "genre": "Fiction",
        "read_status": "to-read", "rating": 4, "notes": "The story of the man who sold his ferrari"},
    {"book_id": "B_004", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year ": 1988, "genre": "Realism",
        "read_status": "read", "rating": 4, "notes": "The story of the man who sold his ferrari"},
    {"book_id": "B_005", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year ": 1988, "genre": "Fiction",
        "read_status": "to-read", "rating": 4, "notes": "The story of the man who sold his ferrari"},
    {"book_id": "B_006", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year ": 1988, "genre": "Romance",
        "read_status": "reading", "rating": 4, "notes": "The story of the man who sold his ferrari"},
]


@app.route("/")
def home():
    """
    Home page of the app. Renders the index.html file.
    """
    return render_template("index.html")


@app.route("/api/books", methods=["GET"])
def get_books():
    """
    Returns a list of all the books in the library.
    """
    return jsonify(books)


@app.route("/api/books/<string:book_id>", methods=["GET"])
def get_book(book_id):
    """
    Returns the details of a specific book based on its book_id.
    if the book is not found, returns a 404 error
    """
    print(f"Data recieved as book_id: {book_id}")
    for book in books:
        if book_id == book.get("book_id"):
            return jsonify(book), 200

    return jsonify({"error": f"The book with book_id {book_id} not found"}), 404


@app.route("/api/books", methods=["POST"])
def add_book():
    """
    1. Adds a new book to the library.
    2. Based on the book_id, if the book already exists, returns a 400 error
    3. Condition to check if all the required fields are present
    4. For loop to check if the book already exists

    """
    new_book = request.json

    if not new_book:
        return jsonify({"error": "No data provided"}), 400

    if "book_id" not in new_book or "author" not in new_book or "title" not in new_book:
        return jsonify({"error": "Missing required fields"}), 400

    for book in books:
        if new_book.get("book_id") == book.get("book_id"):
            return jsonify({"error": f"The book with book_id {new_book.get('book_id')} already exists"}), 400

    books.append(new_book)
    return jsonify({"success": f"Successfully added book with book_id: {new_book.get('book_id')}", "books": books}), 201


@app.route("/api/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    """
    1. Updates the details of a specific book based on its book_id.
    2. If the book is not found, returns a 400 error
    """
    book_update = None  # variable to hold the updated book
    for book in books:
        if book_id == book.get("book_id"):
            book_update = book
            break

    if book_update:
        new_book = request.json
        book_update.update(new_book)
        return jsonify({"success": f"Successfully updated book with book_id: {book_id}", "books": books})

    return jsonify({"error": f"The book with book_id {book_id} not found"}), 400


@app.route("/api/books/<string:book_id>", methods=["DELETE"])
def delete_book(book_id):
    """
    1. Deletes a specific book based on its book_id.
    2. If the book is not found, returns a 400 error.
    """
    book_delete = None
    for book in books:
        if book_id == book.get("book_id"):
            book_delete = book

    if book_delete:
        books.remove(book_delete)
        return jsonify({"success": f"Successfully deleted book with book_id: {book_id}.", "books": books})

    return jsonify({"error": f"The book with book_id {book_id} not found"}), 400


@app.route("/api/books/stats", methods=["GET"])
def get_stats():
    """
    Returns statistics about the books, including total number of books,
    how many are read, genre counts, and average rating.
    """
    if len(books) == 0:
        return jsonify({"error": "No books found"}), 400

    total_books = len(books)
    total_read = sum(1 for book in books if book["read_status"] == "read")
    genre_counts = {}
    for book in books:
        genre = book["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    average_rating = sum(book["rating"] for book in books) / total_books

    return jsonify({
        "total_books": total_books,
        "total_read": total_read,
        "books_count_by_genre": genre_counts,
        "average_rating": average_rating
    }), 200
