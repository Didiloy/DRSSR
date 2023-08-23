import gi

from src.manage_feed_item import ManageFeedItem
from src.rss.rss_parser import RssParser

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename='./data/ui/manage_feed.ui')
class ManageFeed(Adw.Window):
    __gtype_name__ = 'manage_feed'
    listbox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        feeds = RssParser.get_instance().feeds
        for i in range(0, len(feeds)):
            self.listbox.append(ManageFeedItem(feeds[i]))
        self.connect("destroy", self.on_destroy)

    def on_destroy(self, window):
        self.destroy()
