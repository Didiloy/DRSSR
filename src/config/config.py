import sys

import platformdirs
import os


class Config:
    def __init__(self):
        self._config_dir = platformdirs.user_config_dir('DRSSR', 'com.github.didiloy')
        if not os.path.exists(self._config_dir):
            os.makedirs(self._config_dir)

        self._data_dir = platformdirs.user_data_dir('DRSSR', 'com.github.didiloy')
        if not os.path.exists(self._data_dir):
            os.makedirs(self._data_dir)

        if not os.path.isfile(f'{self._data_dir}/feeds.json'):
            with open(f'{self._data_dir}/feeds.json', 'w') as f:
                f.write('{"feeds": []}')
        self._feeds_file = f'{self._data_dir}/feeds.json'

    @property
    def config_dir(self):
        return self._config_dir

    @property
    def data_dir(self):
        return self._data_dir

    @property
    def feeds_file(self):
        return self._feeds_file

    @staticmethod
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
