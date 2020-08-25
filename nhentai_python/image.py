class Image(object):
    def __init__(self, width, height, type, uri):
        self.width = width
        self.height = height
        self.type = type
        self.uri = uri

    @classmethod
    def from_json(cls, json, url) -> 'Image':
        t = cls.get_image_type(json['t'])
        return cls(width=int(json['w']), height=int(json['h']), type=t, uri=url + t)

    def get_image_type(s):
        c = {
            "j": "jpg",
            "p": "png",
            "g": "gif"
        }
        return c.get(s)