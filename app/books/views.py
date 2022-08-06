from flask import Blueprint, render_template
from .dao.books_dao import BooksDAO

books_blueprint = Blueprint('books_blueprint', __name__)

books_dao = BooksDAO('./data/books.json')


@books_blueprint.route('/books/')
def books_page():
    books = books_dao.get_all()
    return render_template('books_index.html', books=books)
