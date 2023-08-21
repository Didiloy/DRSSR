import logging
import sys
import gi

from src.config.config import Config
from src.application import DsrssrApplication

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version("Gio", "2.0")


def init_logging():
    logging.basicConfig(filename=f'{Config().data_dir}/dsrssr.log', level=logging.DEBUG)


def main():
    init_logging()
    logging.debug("Starting application")
    app = DsrssrApplication()
    app.run(sys.argv)
    logging.debug("Shutting down application")


if __name__ == "__main__":
    main()
