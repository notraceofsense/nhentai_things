from threading import *
from book import *
from download_thread import *
from queue import Queue
import os, net

class Book_Thread(Thread):
    def __init__(self, book: Book, path, workers):
        Thread.__init__(self)
        self.book = book
        self.path = path
        self.workers = workers
        self.cwd = os.path.join(path, self.book.id)
        self.pagecwd = os.path.join(self.cwd, "pages")
    
    def run(self):
        while True:
            self._debug_print(self.book.title.pretty)
            self._debug_print("Making directory...")
            self._mkdir()
        
            queue = Queue()

            for x in range(self.workers):
                t = Download_Thread(queue, self.book.id)
                t.daemon = True
                t.start()

            queue.put((self.book.images.cover.uri, self.cwd))
            queue.put((self.book.images.thumbnail.uri, self.cwd))

            for x in self.book.images.pages:
                queue.put((x.uri, self.pagecwd))
       
            queue.join()

            self._debug_print("Finished downloading.")

    def _debug_print(self, msg):
        print("{}: {}".format(str(self.book.id), msg))

    def _mkdir(self):
        os.mkdir(self.cwd)
        os.mkdir(self.pagecwd)
    
    @classmethod
    def from_book_id(cls, book_id, path, workers) -> 'Book_Thread':
        return cls(net.get_book(book_id), path, workers)