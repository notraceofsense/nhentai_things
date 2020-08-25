from image import *

class Images(object):
    def __init__(self, cover, thumbnail):
        self.cover = cover
        self.thumbnail = thumbnail
        self.pages = []

    @classmethod
    def from_json(cls, json, gallery_url, thumbnail_url) -> 'Images':
        cover = Image.from_json(json['cover'], thumbnail_url + "/cover.")
        thumbnail = Image.from_json(json['thumbnail'], thumbnail_url + "/thumb.")
        n = cls(cover, thumbnail)
        for i, x in enumerate(json['pages']):
            n.pages.append(Image.from_json(x, gallery_url + "/{}.".format(i + 1)))

        return n
