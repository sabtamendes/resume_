from src.respositories.user_repository import get_book_by_id, get_all_books, create_user

async def get_user(book_id):
    return await get_book_by_id(book_id)

def list_books():
    books = get_all_books()
    book_list = [{'title': book.title, 'author': book.author} for book in books]
    return book_list
def add_user(username, email):
    return create_user(username, email)
