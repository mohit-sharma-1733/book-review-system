# FastAPI Book Review System

This is a FastAPI-based API for a hypothetical book review system.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-book-review-system.git
Install dependencies:

pip install -r requirements.txt

Usage
Start the FastAPI application:

uvicorn main:app --reload

Navigate to http://127.0.0.1:8000/docs in your browser to access the Swagger UI documentation and test the API endpoints.

Endpoints
POST /books/: Add a new book.
POST /books/{book_id}/reviews/: Submit a review for a book.
GET /books/: Retrieve all books with optional filters by author or publication year.
GET /books/{book_id}/reviews/: Retrieve all reviews for a specific book.
