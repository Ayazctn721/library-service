from uuid import uuid4
# unique identifier
from datetime import datetime

#! Model: representing the data structure/entities


class Book:
    def __init__(self, book_id, title, author, publication_year, genre, read_status, rating, notes=""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status
        self.rating = rating
        self.notes = notes
        # we convert to string bc it is not a string initially
        self.uuid = str(uuid4())
        self.creared_at = datetime.now()

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "genre": self.genre,
            "read_status": self.read_status,
            "rating": self.rating,
            "notes": self.notes,
            "uuid": self.uuid,
            "created_at": self.creared_at
        }
