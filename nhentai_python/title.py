class Title(object):
    def __init__(self, english, japanese, pretty):
        self.english = english
        self.japanese = japanese
        self.pretty = pretty

    @classmethod
    def from_json(cls, json) -> 'Title':
        cls(json['english'], json['japanese'], json['pretty'])
