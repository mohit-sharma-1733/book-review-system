import sqlite3
from models import Book, Review
from typing import List, Optional

# Connect to SQLite database
conn = sqlite3.connect('book_review_system.db')
cursor = conn.cursor()

# Create tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        text TEXT,
        rating INTEGER,
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
''')

# Save changes
conn.commit()

# CRUD Operations

def add_book_db(book: Book):
    cursor.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
                   (book.title, book.author, book.publication_year))
    conn.commit()

def add_review_db(book_id: int, review: Review):
    cursor.execute("INSERT INTO reviews (book_id, text, rating) VALUES (?, ?, ?)",
                   (book_id, review.text, review.rating))
    conn.commit()

def get_books_db(author: Optional[str] = None, publication_year: Optional[int] = None) -> List[Book]:
    query = "SELECT * FROM books"
    if author:
        query += f" WHERE author = '{author}'"
    if publication_year:
        if author:
            query += " AND"
        else:
            query += " WHERE"
        query += f" publication_year = {publication_year}"
    cursor.execute(query)
    books_data = cursor.fetchall()
    books = [Book(id=row[0], title=row[1], author=row[2], publication_year=row[3]) for row in books_data]
    return books

def get_reviews_db(book_id: int) -> List[Review]:
    cursor.execute("SELECT * FROM reviews WHERE book_id = ?", (book_id,))
    reviews_data = cursor.fetchall()
    reviews = [Review(id=row[0], book_id=row[1], text=row[2], rating=row[3]) for row in reviews_data]
    return reviews
