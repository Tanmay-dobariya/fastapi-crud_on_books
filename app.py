from fastapi import Body
from fastapi import FastAPI

app = FastAPI()


BOOKS = []


@app.get("/books")
async def read_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {'error': 'Book not found'}


@app.get("/books/")
async def read_book_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}")
async def read_author_books(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(body=Body()):
    BOOKS.append(body)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break