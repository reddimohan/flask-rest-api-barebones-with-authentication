from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('Books', description='Books related APIs')
from flask import request
from main.services.book_service import BookService


new_book_parser = api.parser()
new_book_parser.add_argument('book_name', type=str, help='Book name', location='form')
new_book_parser.add_argument('author', type=str, help='Name of the Book author', location='form')
new_book_parser.add_argument('genres', type=str, help='Type of book', location='form')
new_book_parser.add_argument('year', type=str, help='year of publication', location='form')

@api.route('/book')
class NewBook(Resource):
    """docstring for NewBook."""

    def __init__(self, arg):
        super(NewBook, self).__init__(arg)

    @api.doc(parser= new_book_parser)
    def post(self):
        """ Save new book object into database """
        if 'year' not in request.form:
            return api.abort(400, 'year should not be empty.', status='error', status_code= 400)
        
        return request.form
    
    @api.doc(parser= None)
    def get(self):
        """ Get list of books """
        return "Args"



# book_parser = api.parser()
# book_parser.add_argument('book_id', type=int, location='form')
@api.route('/book/<book_id>')
class Book(Resource):
    """docstring for Book."""

    def __init__(self, arg):
        super(Book, self).__init__()
        self.arg = arg

    def put(self, book_id):
        """ Update book based on ID """
        return book_id

    def get(self, book_id):
        """ Get book object based on ID """
        return book_id

    def delete(self, book_id):
        """ Delete a book object based on ID. """
        return book_id
