class Feed:
    def __init__(self, title, url, active):
        self.url = url
        self.active = active
        self.title = title

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "active": self.active
        }

    def __str__(self):
        return f"Feed: {self.title} : {self.url} Active: {self.active}"

    @staticmethod
    def from_dict(dict_feed):
        return Feed(dict_feed['title'], dict_feed['url'], dict_feed['active'])
