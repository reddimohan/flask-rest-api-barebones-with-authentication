from bson.objectid import ObjectId

from main.db import MongoDB


class BookService:
    """ doc string for BookService """

    def __init__(self):
        super(BookService, self).__init__()
        self.collection = "books"
        self.mongo = MongoDB()

    def add(self, book_obj):
        book = self.mongo.find(self.collection, {"book_name": book_obj["book_name"]})
        if not book:
            return (
                self.mongo.save(self.collection, book_obj),
                "Successfully created.",
                200,
            )
        else:
            return ("ok", "Book already added to the library.", 400)

    def books_list(self):
        return self.mongo.find(self.collection)

    def delete_book(self, book_id):
        return self.mongo.delete(self.collection, book_id)

    def update_book(self, book_id, book_obj):
        condition = {"$set": book_obj}
        res, update_count = self.mongo.update(self.collection, book_id, condition)

        if res:
            return ("success", res, "ok", 200)
        return ("error", "", "Something went wrong.", 400)

    def get_book(self, book_id):
        condition = {"_id": ObjectId(book_id)}
        return self.mongo.find(self.collection, condition)
