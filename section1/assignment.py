from fastapi import Body, FastAPI

app = FastAPI()

Books = [
    {'title':'Title One','author': 'Author One','category': 'Science'},
    {'title':'Title Two','author': 'Author Two','category': 'Science'},
    {'title':'Title Three','author': 'Author Three','category': 'history'},
    {'title':'Title Four','author': 'Author Four','category': 'math'},
    {'title':'Title Five','author': 'Author Five','category': 'math'},
    {'title':'Title Six','author': 'Author Two','category': 'math'}
]
# {"title":"Title Seven","author": "Author Two","category": "math"}

@app.get("/books")
async def read_all_books():
    return Books


@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author, category: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# import Body from fastapi
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    Books.append(new_book)

# update book data
@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == \
            updated_book.get('title').casefold():
            Books[i] = updated_book

# delete a book
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == \
            book_title.casefold():
            Books.pop(i)
            break


"""
Assignment

1. Create a new API Endpoint that can fetch all 
   books from a specific author using either 
   Path Parameters or Query Parameters.

"""

@app.get('/books/byauthor/{book_author}')
async def fetch_books_by_author(book_author: str):
    books_to_return = []
    for book in Books:
        if book.get('author').casefold() == \
            book_author.casefold():
            books_to_return.append(book)
    return books_to_return