import gi

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

    def __init__(self, title, active, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.label_title.set_text(title)
        print(title)
        self.switch_active_feed.set_active(active)

    def on_switch_active_feed_state_set(self, switch, state):
        print(switch.get_active())

    def on_button_delete_clicked(self, button):
        print("Delete clicked")

