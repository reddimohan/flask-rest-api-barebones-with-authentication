from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('Books', description='')

from flask import request

new_book_parser = api.parser()
new_book_parser.add_argument('book_name', type=str, help='Book name', location='form')
new_book_parser.add_argument('author', type=str, help='Name of the Book author', location='form')
new_book_parser.add_argument('genres', type=str, help='Type of book', location='form')
new_book_parser.add_argument('year', type=str, help='year of publication', location='form')
@api.route('/book/new')
class NewBook(Resource):
    """docstring for NewBook."""

    def __init__(self, arg):
        super(NewBook, self).__init__()
        self.arg = arg

    @api.doc(parser= new_book_parser)
    def post(self):
        pass


book_parser = api.parser()
book_parser.add_argument('book_id', type=str, help='book_id', location='form')
@api.route('/book/<int:book_id>')
class Book(Resource):
    """docstring for Book."""

    def __init__(self, arg):
        super(Book, self).__init__()
        self.arg = arg

    @api.doc(parser= book_parser)
    def put(self):
        pass

    def get(self):
        print("Get Books")
        pass

    def delete(self):
        pass
