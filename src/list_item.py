import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


@Gtk.Template(filename='./data/ui/list_item.ui')
class ListItem(Gtk.ListBoxRow):
    __gtype_name__ = 'list_item'
    label_feed_title = Gtk.Template.Child("label_feed_title")
    label_feed_description = Gtk.Template.Child()
    label_feed_date = Gtk.Template.Child()
    feed_avatar = Gtk.Template.Child()

    def __init__(self, title, description, date, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.label_feed_title.set_text(title)
        self.label_feed_description.set_text(description)
        self.label_feed_date.set_text(date)
        self.feed_avatar = Adw.Avatar.new(50, description[0], False)
        # self.feed_avatar.set_text(description)
