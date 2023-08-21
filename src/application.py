import gi

from src.window import DrssrWindow

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")

from gi.repository import Gtk, Gio, Adw


class DrssrApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.github.didiloy.drssr',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = DrssrWindow(application=self)
        win.present()
