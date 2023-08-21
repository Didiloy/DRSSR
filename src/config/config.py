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

    @property
    def config_dir(self):
        return self._config_dir

    @property
    def data_dir(self):
        return self._data_dir
