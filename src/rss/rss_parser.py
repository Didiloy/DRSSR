import feedparser
from src.config import logging


class RssParser:
    def __init__(self):
        pass

    def parse(self, url):
        logging.log(f"Fetching feed from {url}")
        feed = feedparser.parse(url)
        print(feed)
        return feed
