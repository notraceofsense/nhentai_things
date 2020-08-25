from images import *
from title import *
import urllib

class Book(object):
    def __init__(self, id, media_id, title, gallery_url, thumbnail_url, images):
        self.id = id
        self.media_id = media_id
        self.title = title
        self.gallery_url = gallery_url
        self.thumbnail_url = thumbnail_url
        self.images = images

    @classmethod
    def from_json(cls, json) -> 'Book':
        id = json['id']
        media_id = json['media_id']
        title = Title.from_json(json['title'])
        gallery_url = urllib.parse.urljoin("https://i.nhentai.net/galleries/", str(media_id))
        thumbnail_url = urllib.parse.urljoin("https://t.nhentai.net/galleries/", str(media_id))
        images = Images.from_json(json['images'], gallery_url, thumbnail_url)
        return cls(id, media_id, title, gallery_url, thumbnail_url, images)
