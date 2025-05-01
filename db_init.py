from app import create_app
from db import get_db, close_db


def create_tables():
    app = create_app()

    with app.app_context():
        connection = get_db()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                book_id VARCHAR(255) UNIQUE NOT NULL,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                publication_year INTEGER NOT NULL,
                genre VARCHAR(255) NOT NULL,
                read_status VARCHAR(255) NOT NULL,
                rating INTEGER NOT NULL,
                notes TEXT,
                uuid UUID NOT NULL,
                created_at TIMESTAMP 
            )

                    """)
        connection.commit()
        cursor.close()
        close_db()


if __name__ == '__main__':
    create_tables()
    print("Tables created successfully")
