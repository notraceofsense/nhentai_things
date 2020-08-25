from threading import *
import net

class Download_Thread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            uri, path = self.queue.get()

            try:
                net.download.image(uri, path)
                print("{} downloaded.".format(uri))
            finally:
                self.queue.task_done()
