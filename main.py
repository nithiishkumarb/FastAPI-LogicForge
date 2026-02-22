from fastapi import Body, FastAPI

app=FastAPI()

books=[
    {"title":"Title one", "Author":"Author one", "publish":"Publisher one",'category':"Science"},
    {"title":"Title Two", "Author":"Author Two", "publish":"Publisher Two",'category':"Science"},
    {"title":"Title Three", "Author":"Author Two", "publish":"Publisher Three",'category':"Science"},
    {"title":"Title Four", "Author":"Author Four", "publish":"Publisher Four",'category':"maths"},
    {"title":"Title Five", "Author":"Author Two", "publish":"Publisher Five",'category':"maths"}
]

@app.get("/books")
async def read_all_books():
    return books

@app.get('/books/get_author')
async def get_author_books(author:str):
    return [book for book in books if book.get('Author').casefold()==author.casefold()]

@app.get("/books/{book_title}")
async def read_book(book_title):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book
        

@app.get("/books/")
async def read_book_by_category(category:str):
    books_by_category=[]
    for book in books:
        if book.get("category").casefold() == category.casefold():
            books_by_category.append(book)
    return books_by_category


@app.get("/books/{author}/")
async def read_book_by_category(author:str,category:str):
    books_by_category=[]
    for book in books:  
        if book.get("category").casefold() == category.casefold() and book.get("Author").casefold() == author.casefold():
            books_by_category.append(book)
    return books_by_category

@app.post('/book')
async def add_new_book(new_book=Body()):
    books.append(new_book)

@app.put("/book")
async def update_book(new_book=Body()):
    for i, book in enumerate(books):
        if book.get("title").casefold() == new_book.get("title").casefold():
            books[i] = new_book
            return {"message": "Book updated successfully"}
    
    return {"message": "Book not found"}

@app.delete("/book/{book_title}")
async def delete_book(book_title:str):
    for i, book in enumerate(books):
        if book.get("title").casefold()== book_title.casefold():
            books.pop(i)
            break
    return {"message":"Book deleted successfully"}

@app.get("")
async def root():
    return {"message":"Welcome to LogicForge"}