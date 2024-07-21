from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'Book'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp())
    magicCode = db.Column(db.Text, nullable=True)
    professor = db.Column(db.Text, nullable=True)
