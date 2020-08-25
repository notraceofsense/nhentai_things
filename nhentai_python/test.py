import book

book = book.Book.from_api(139040)

print(book.gallery_url)
print(book.images.cover.uri)
print(book.images.pages[5].uri)