from threading import Thread
from book import *
from queue import Queue
import os, net

class Book_Thread(Thread):
    def __init__(self, book: Book, path, json, queue):
        Thread.__init__(self)
        self.book = book
        self.path = path
        self.json = json
        self.queue = queue
        self.cwd = os.path.join(path, str(self.book.id))
        self.pagecwd = os.path.join(self.cwd, "pages")
    
    def run(self):
        self._debug_print(self.book.title.pretty)
        self._debug_print("Making directory...")
        self._mkdir()

        if(self.json):
            self.queue.put((net.get_json_uri(self.book.id), self.cwd))

        self.queue.put((self.book.images.cover.uri, self.cwd))
        self.queue.put((self.book.images.thumbnail.uri, self.cwd))

        for x in self.book.images.pages:
            self.queue.put((x.uri, self.pagecwd))

    def _debug_print(self, msg):
        print("{}: {}".format(str(self.book.id), msg))

    def _mkdir(self):
        os.mkdir(self.cwd)
        os.mkdir(self.pagecwd)
    
    @classmethod
    def from_book_id(cls, book_id, path, json, queue) -> 'Book_Thread':
        return cls(net.get_book(book_id), path, json, queue)