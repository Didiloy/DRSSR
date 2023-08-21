import time

import gi

from src.list_item import ListItem
from src.rss.rss_parser import RssParser

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename='./data/ui/window.ui')
class DrssrWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'DrssrWindow'

    button_add_feeds = Gtk.Template.Child("button_add_feeds")
    button_manage_feeds = Gtk.Template.Child()
    button_refresh_feeds = Gtk.Template.Child()
    listbox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.set_title("DRSSR")
        self.button_add_feeds.connect('clicked', self.on_button_add_feeds_clicked)
        self.button_manage_feeds.connect('clicked', self.on_button_manage_feeds_clicked)
        self.button_refresh_feeds.connect('clicked', self.on_button_refresh_feeds_clicked)

    def on_button_add_feeds_clicked(self, button):
        pass

    def on_button_manage_feeds_clicked(self, button):
        rss_parser = RssParser()
        print(rss_parser.feeds)
        rss_parser.save_feeds()

    def on_button_refresh_feeds_clicked(self, button):
        rss_parser = RssParser()
        feed = rss_parser.parse()
        for i in range(0, len(feed)):
            self.listbox.append(ListItem(feed[i].title,
                                         feed[i].description,
                                         time.strftime("%d/%m/%Y", feed[i].published_parsed)))
            