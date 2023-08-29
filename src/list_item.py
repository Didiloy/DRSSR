import gi
import webbrowser
from src.config.config import Config

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename=Config.resource_path('./data/ui/list_item.ui'))
class ListItem(Gtk.ListBoxRow):
    __gtype_name__ = 'list_item'
    label_feed_title = Gtk.Template.Child("label_feed_title")
    label_feed_description = Gtk.Template.Child()
    label_feed_date = Gtk.Template.Child()
    button_open_in_browser = Gtk.Template.Child()
    label_feed_author = Gtk.Template.Child()

    def __init__(self, title, description, date, url, author, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.label_feed_title.set_text(title)
        self.label_feed_description.set_text(description)
        self.label_feed_date.set_text(f"<i>{date}</i>")
        self.label_feed_date.set_use_markup(True)
        self.label_feed_author.set_text(f"<i>{author}</i>")
        self.label_feed_author.set_use_markup(True)
        self.button_open_in_browser.connect("clicked", self.on_button_open_in_browser_clicked)
        self.url = url

    def on_button_open_in_browser_clicked(self, button):
        webbrowser.open(self.url, 2)
