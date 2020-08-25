import threading, requests

class Book_Thread(threading.Thread):
    def __init__(self, threadID, name, book_id):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.book_id = book_id

    def run(self):
        api_url = "https://nhentai.net/api/gallery/{}".format(self.book_id)

        debug_print("Getting metadata from nhentai...")
        book_json


    def debug_print(message):
        print("{}: {}".format(self.book_id, message))
