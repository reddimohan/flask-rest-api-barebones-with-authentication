from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('Books', description='Books related APIs')
from flask import request
from main.services.book_service import BookService
from core.utils import Utils


new_book_model = api.model('NewBookModel', {
    'book_name': fields.String(description="Book name", required=True),
    'author': fields.String(description="Name of the author", required=True),
    'genres': fields.String(description="Type of book", required=True),
    'year': fields.String(description="year of publication", required=True)
})

@api.route('/book')
class NewBook(Resource):
    """docstring for NewBook."""

    def __init__(self, arg):
        super(NewBook, self).__init__(arg)
        self.utils = Utils()
        self.book_service = BookService()

    @api.expect(new_book_model)
    def post(self):
        """ Save new book object into database """
        if 'year' not in request.json:
            return api.abort(400, 'year should not be empty.', status='error', status_code= 400)
        
        res, msg, code = self.book_service.add(request.json)

        return {'status': self.utils.http_status(code), 'res': res, 'message': msg}, code
    
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
