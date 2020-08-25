from threading import *
import net

class Download_Thread(Thread):
    def __init__(self, queue, book_id):
        Thread.__init__(self)
        self.queue = queue
        self.book_id = book_id

    def run(self):
        while True:
            uri, path = self.queue.get()

            try:
                net.download.image(uri, path)
                self._debug_print("{} downloaded.".format(uri))
            finally:
                self.queue.task_done()

    def _debug_print(self, msg):
        print("{}: {}".format(str(self.book_id), msg))