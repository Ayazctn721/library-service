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
