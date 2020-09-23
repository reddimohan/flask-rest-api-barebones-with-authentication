from flask_restplus import Namespace, Resource, fields

api = Namespace("Books", description="Books related APIs")
from flask import request
from flask_jwt_extended import jwt_required

from core.utils import Utils
from main.services.book_service import BookService

book_model = api.model(
    "BookModel",
    {
        "book_name": fields.String(description="Book name", required=True),
        "author": fields.String(description="Name of the author", required=True),
        "genres": fields.String(description="Type of book", required=True),
        "year": fields.String(description="year of publication", required=True),
    },
)


@api.route("/book")
class NewBook(Resource):
    """docstring for NewBook."""

    def __init__(self, arg):
        super(NewBook, self).__init__(arg)
        self.utils = Utils()
        self.book_service = BookService()

    @jwt_required
    @api.expect(book_model)
    def post(self):
        """ Save new book object into database """
        if "book_name" not in request.json or request.json["book_name"] == "":
            return api.abort(
                400, "Book name should not be empty.", status="error", status_code=400
            )
        if "author" not in request.json or request.json["author"] == "":
            return api.abort(
                400, "Autor name should not be empty.", status="error", status_code=400
            )
        if "genres" not in request.json or request.json["genres"] == "":
            return api.abort(
                400, "Book genre should not be empty.", status="error", status_code=400
            )
        if "year" not in request.json or request.json["year"] == "":
            return api.abort(
                400, "year should not be empty.", status="error", status_code=400
            )

        res, msg, code = self.book_service.add(request.json)

        return {
            "status": self.utils.http_status(code),
            "res": res,
            "message": msg,
        }, code

    @jwt_required
    @api.doc(parser=None)
    def get(self):
        """ Get list of books """
        books = self.book_service.books_list()
        return {"status": "success", "res": books}, 200


update_book_model = api.model(
    "BookUpdateModel",
    {
        "book_name": fields.String(description="Book name"),
        "author": fields.String(description="Name of the author"),
        "genres": fields.String(description="Type of book"),
        "year": fields.String(description="year of publication"),
    },
)


@api.route("/book/<string:book_id>")
class Book(Resource):
    """docstring for Book."""

    def __init__(self, arg):
        super(Book, self).__init__(arg)
        self.book_service = BookService()

    # @jwt_required
    @api.expect(update_book_model)
    def put(self, book_id):
        """ Update book based on book_id. 5e86d84da011b26c2082e0c9 """
        if not book_id:
            api.abort(400, "book_id is missing.", status="error")

        status, obj, msg, code = self.book_service.update_book(book_id, request.json)

        return {"status": status, "data": obj, "message": msg}, code

    @jwt_required
    def get(self, book_id):
        """ Get book object based on book_id """
        book = self.book_service.get_book(book_id)

        return {"status": "success", "res": book}, 200

    @jwt_required
    def delete(self, book_id):
        """ Delete a book object based on ID. """
        if not book_id:
            api.abort(400, f"book_id is required.", status="error")

        res, msg = self.book_service.delete_book(book_id)

        if res:
            return {"status": "success", "data": res, "message": msg}, 200
        else:
            return api.abort(400, msg, status="error")


# class NullableString(fields.String):
#     __schema_type__ = ['string', 'null']
#     __schema_example__ = 'nullable string'
