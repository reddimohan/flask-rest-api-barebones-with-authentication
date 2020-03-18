from core.utils import Utils

from main.db import MongoDB

class BookService():
    """ doc string for BookService """
    def __init__(self):
        super(BookService, self).__init__()
        self.collection = 'books'
        self.mongo = MongoDB()
    
    def add(self, book_obj):
        book = self.mongo.find(self.collection, {'book_name': book_obj['book_name']})
        if not book:
            return (self.mongo.save(self.collection, book_obj), 'Successfully created.', 200)
        else:
            return ('', 'Book already added to the library.', 400)