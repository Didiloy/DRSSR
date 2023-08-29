import gi

from src.rss.feed import Feed
from src.rss.rss_parser import RssParser
from src.config.config import Config

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename=Config.resource_path('./data/ui/add_feed.ui'))
class AddFeed(Gtk.Dialog):
    __gtype_name__ = 'add_feed'
    button_add_feed = Gtk.Template.Child()
    button_cancel = Gtk.Template.Child()
    entry_url = Gtk.Template.Child()

    def __init__(self, main_window, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.set_transient_for(main_window)
        self.button_add_feed.connect('clicked', self.on_button_add_feed_clicked)
        self.button_cancel.connect('clicked', self.on_button_cancel_clicked)
        self.entry_url.grab_focus_without_selecting()

    def on_button_add_feed_clicked(self, button):
        if self.entry_url.get_text() == "":
            self.on_button_add_feed_error()
        else:
            # Parse the feed to get the name
            parsed_feed = RssParser.get_instance().parse_feed(self.entry_url.get_text())
            if parsed_feed is None:
                self.on_button_add_feed_error()
                return
            # Add the feed to the list
            feed = Feed(parsed_feed.feed.title, self.entry_url.get_text(), True)
            RssParser.get_instance().add_feed(feed)
            self.destroy()

    def on_button_add_feed_error(self):
        self.entry_url.set_placeholder_text("Please enter a valid URL")
        Gtk.Widget.add_css_class(self.entry_url, "error")

    def on_button_cancel_clicked(self, button):
        self.destroy()
