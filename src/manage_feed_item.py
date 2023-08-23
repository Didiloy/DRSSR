import gi

from src.config import logging
from src.rss.feed import Feed
from src.rss.rss_parser import RssParser

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename='./data/ui/manage_feed_item.ui')
class ManageFeedItem(Gtk.ListBoxRow):
    __gtype_name__ = 'manage_feed_item'
    label_title = Gtk.Template.Child()
    button_delete_feed = Gtk.Template.Child()
    switch_active_feed = Gtk.Template.Child()

    def __init__(self, feed: Feed, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.feed = feed
        self.label_title.set_text(self.feed.title)
        self.switch_active_feed.set_active(self.feed.active)
        self.switch_active_feed.connect("state-set", self.on_switch_active_feed_state_set)
        self.button_delete_feed.connect("clicked", self.on_button_delete_clicked)

    def on_switch_active_feed_state_set(self, switch, state):
        self.feed.active = switch.get_active()
        RssParser.get_instance().save_feeds()

    def on_button_delete_clicked(self, button):
        logging.log(f"Deleting feed: {self.feed.title}")
        RssParser.get_instance().feeds.remove(self.feed)
        RssParser.get_instance().save_feeds()
        self.set_visible(False)
