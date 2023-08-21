from typing import List

import feedparser
from src.config import logging
from src.config.config import Config
import json

from src.rss.feed import Feed


class RssParser:
    def __init__(self):
        self._feeds: List[Feed] = []
        self._load_saved_feeds()

    @property
    def feeds(self):
        return self._feeds

    def _parse(self, url):
        logging.log(f"Fetching feed from {url}")
        feed = feedparser.parse(url)
        logging.log(f"Feed fetched: {feed.feed.title}")
        return feed

    def parse(self):
        parsed_feeds_entries = []
        for feed in self._feeds:
            if feed.active:
                parsed_feeds_entries.append(self._parse(feed.url).entries)

        return self.sort(parsed_feeds_entries)

    def sort(self, parsed_feeds_entries):
        sorted_entries = []
        for entries in parsed_feeds_entries:
            for entry in entries:
                sorted_entries.append(entry)

        sorted_entries.sort(key=lambda x: x.published_parsed, reverse=True)
        return sorted_entries

    def _load_saved_feeds(self):
        logging.log("Loading feeds file")
        with open(Config().feeds_file) as feeds_file:
            file_contents = feeds_file.read()
            try:
                dict_feeds = json.loads(file_contents)
                for feed in dict_feeds['feeds']:
                    self._feeds.append(Feed.from_dict(feed))
                logging.log("Feeds file loaded")
            except json.decoder.JSONDecodeError:
                logging.log("Error while loading feeds file. Using empty list.")
                self._feeds = []

    def save_feeds(self):
        logging.log("Saving feeds file to: " + Config().feeds_file)
        with open(Config().feeds_file, 'w', encoding='utf-8') as f:
            feeds_string = [f.to_dict() for f in self._feeds]
            print(feeds_string)
            dict_feeds = {"feeds": feeds_string}
            json.dump(dict_feeds, f, ensure_ascii=False, indent=4)
        logging.log("Feeds file saved")
