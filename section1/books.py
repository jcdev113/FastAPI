from fastapi import FastAPI

app = FastAPI()

Books = [
    {'title':'Title One','author': 'Author One','category': 'Science'},
    {'title':'Title Two','author': 'Author Two','category': 'Science'},
    {'title':'Title Three','author': 'Author Three','category': 'math'},
    {'title':'Title Four','author': 'Author Four','category': 'history'},
    {'title':'Title Five','author': 'Author Five','category': 'math'},
    {'title':'Title Six','author': 'Author Six','category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return Books