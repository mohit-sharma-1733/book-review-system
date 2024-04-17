from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int]
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    id: Optional[int]
    book_id: Optional[int]
    text: str
    rating: int
