from fastapi import FastAPI, BackgroundTasks,HTTPException
from database import add_book_db, add_review_db, get_books_db, get_reviews_db
from utils import send_email
from models import Book , Review
from typing import List,Optional
app = FastAPI()

# Endpoints
@app.post("/books/", status_code=201)
def add_book(book: Book):
    add_book_db(book)
    return {"message": "Book added successfully"}

@app.post("/books/{book_id}/reviews/", status_code=201)
def submit_review(book_id: int, review: Review, background_tasks: BackgroundTasks):
    book = get_books_db(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    add_review_db(book_id, review)
    # Send confirmation email in the background
    background_tasks.add_task(send_email, email="example@example.com", message="Your review has been submitted!")
    return {"message": "Review submitted successfully"}

@app.get("/books/", response_model=List[Book])
def get_books(author: Optional[str] = None, publication_year: Optional[int] = None):
    books = get_books_db(author, publication_year)
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    return books

@app.get("/books/{book_id}/reviews/", response_model=List[Review])
def get_reviews(book_id: int):
    book = get_books_db(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    reviews = get_reviews_db(book_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this book")
    return reviews