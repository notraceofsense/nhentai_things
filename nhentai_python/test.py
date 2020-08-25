import net, os
from book_thread import *

book = net.get_book(234638)

print(book.gallery_url)
print(book.images.cover.uri)
print(book.images.pages[5].uri)
print(book.title.pretty)

b = Book_Thread.from_book_id(234638, os.getcwd(), 8).start()