from src.models.user_model import Book, db

def get_book_by_id(book_id):
    return Book.query.get(book_id)

def get_all_books():
    return Book.query.all()

def create_user(username, email):
    user = Book(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
