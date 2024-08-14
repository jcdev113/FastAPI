from fastapi import FastAPI

app = FastAPI()

Books = [
    {'title':'Title One','author': 'Author One','category': 'Science'},
    {'title':'Title Two','author': 'Author Two','category': 'Science'},
    {'title':'Title Three','author': 'Author Three','category': 'history'},
    {'title':'Title Four','author': 'Author Four','category': 'math'},
    {'title':'Title Five','author': 'Author Five','category': 'math'},
    {'title':'Title Six','author': 'Author Six','category': 'math'}
]

@app.get("/bookss/{book_param}")
async def read_all_book(book_param):
    return {'dynamic_para':book_param}

# Order matters
@app.get("/books/mybook")
async def read_all_books():
    return {'book_title':'My favorite one'}

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}

@app.get('/book/{book_title}')
async def read_book(book_title: str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book