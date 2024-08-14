from typing import Optional 

from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

### Define Classes
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config ={
        "json_schema_extra": {
            "example":{
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029
            }
        }
    }

### Define Data
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 3, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 2, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 4, 2025)
]

### Define Functions
def find_book_id(book: Book):

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book


@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


"""
Assignment


Add a new field to Book and BookRequest called 

published_date: int (for example, published_date: int = 2012). 

So, this book as published on the year of 2012.

Enhance each Book to now have a published_date

Then create a new GET Request method to filter by published_date

"""

@app.get('/books/publish/', status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999,lt=2031)):
    results = []
    for book in BOOKS:
        if book.published_date == published_date:
            results.append(book)
    return results


@app.post('/books/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = book
            book_changed = True
    
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_delete = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_delete = True
            break

    if not book_delete:
        raise HTTPException(status_code=404, detail='Item not found')
