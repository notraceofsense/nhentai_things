import requests, os, urllib
from book import *

def get_book(book_id):
    return Book.from_json(requests.get(get_json_uri(book_id)).json())

def get_json_uri(book_id):
    return urllib.parse.urljoin("https://nhentai.net/api/gallery/", str(book_id))

class download:
    def image(uri, path):

        filename = uri.split('/')[-1]

        with open(os.path.join(path, filename), 'xb') as fd:
            fd.write(requests.get(uri, allow_redirects=True).content)