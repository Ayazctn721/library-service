from db import book_data


def validate_book_data(data):
    error = {}

    # validate if the data is complete and has the required fields
    if not data.get("book_id"):  # data is a dictionary
        error["book_id"] = "Book ID is required fields"

    if not data.get("author"):  # data is a dictionary
        error["author"] = "Author is required fields"

    if not data.get("title"):  # data is a dictionary
        error["title"] = "Title is required fields"

    # make sure the data types are correct
    # sku book_id -> string, name -> string, title -> string

    if data.get("title") and not isinstance(data.get("book_id"), str):
        error["book_id"] = "Book ID must be a string"

    if data.get("title") and not isinstance(data.get("author"), str):
        error["author"] = "Author must be a string"

    if data.get("title") and not isinstance(data.get("title"), str):
        error["title"] = "Title must be a string"

    if data.get("title") and isinstance(data.get("book_id"), str) and not data.get("book_id").startswith("B_"):
        error["book_id"] = "Book ID must start with B_"

    # check if the book already exists
    for book in book_data:
        if book.book_id == data.get("book_id"):
            error["book_id"] = "Book ID already exists"

    return error
