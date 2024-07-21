from flask import Blueprint, jsonify, request
from src.services.user_service import get_user, list_books, add_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/books', methods=['GET'])
def get_users():
    books = list_books()
    return jsonify(books)


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify({'error': 'Invalid data'}), 400
    user = add_user(username, email)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201
