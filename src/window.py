import time

import gi

from src.add_feed import AddFeed
from src.list_item import ListItem
from src.manage_feed import ManageFeed
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
    label_number_articles = Gtk.Template.Child()
    progress_bar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.set_title("DRSSR")
        self.button_add_feeds.connect('clicked', self.on_button_add_feeds_clicked)
        self.button_manage_feeds.connect('clicked', self.on_button_manage_feeds_clicked)
        self.button_refresh_feeds.connect('clicked', self.on_button_refresh_feeds_clicked)

    def on_button_add_feeds_clicked(self, button):
        add_feed = AddFeed(self)
        add_feed.show()

    def on_button_manage_feeds_clicked(self, button):
        manage_feed = ManageFeed()
        manage_feed.show()

    def on_button_refresh_feeds_clicked(self, button):
        # Remove all the items from the listbox, there is surely a better way to do this but I could not find it
        while self.listbox.get_last_child() is not None:
            self.listbox.remove(self.listbox.get_last_child())
        rss_parser = RssParser.get_instance()
        feed = rss_parser.parse()
        for i in range(0, len(feed)):
            self.listbox.append(ListItem(feed[i].title,
                                         feed[i].description,
                                         time.strftime("%d/%m/%Y", feed[i].published_parsed)))
        self.label_number_articles.set_text(f"{len(feed)} articles")
            