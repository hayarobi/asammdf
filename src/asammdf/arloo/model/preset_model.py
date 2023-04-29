import logging
from typing import Optional

from PySide6 import QtCore
from PySide6.QtCore import QStringListModel

PRESET_SETTING_V1 = "onePreset"
PRESET_SETTING_V2 = "presets"
PRESET_SETTING_NAMES = "presetNames"

class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


_settings = None

logger = logging.getLogger("arloo.preset")
logger.setLevel(logging.DEBUG)

def init_preset():
    global _settings
    _settings = QtCore.QSettings()
    # preset_list = _settings.value(PRESET_SETTING_NAMES, [])
    _settings.beginGroup(PRESET_SETTING_V2)

    logger.debug("reading preset config from file %s",_settings.fileName())
    presets_map = {}
    size = _settings.beginReadArray(PRESET_SETTING_V2)
    for i in range(0, size):
        _settings.setArrayIndex(i)
        preset_name = _settings.value("name")
        strlist = _settings.value("channels", [])
        if not strlist:
            strlist = []
        channels = QStringListModel()
        channels.setStringList(strlist)
        presets_map[preset_name] = channels
    _settings.endArray()
    PresetModel.instance().init_with(presets_map)


def _sync_settings(preset_model):
    global _settings
    _settings.beginWriteArray(PRESET_SETTING_V2)
    i = 0
    p_map = preset_model.preset_map
    for key, val in p_map.items():
        _settings.setArrayIndex(i)
        _settings.setValue("name", key)
        _settings.setValue("channels", val.stringList())
        i += 1
    _settings.endArray()
    _settings.sync()


class PresetModel(SingletonInstance):
    def __init__(self):
        self.preset_map = {}
        self.list = QStringListModel([])

    def init_with(self, initial_preset):
        self.preset_map.clear()
        for key, val in initial_preset.items():
            self.set_preset_channels(key, val, False)

    def find_preset(self, preset_name):
        return preset_name in self.preset_map

    def get_channel_list(self, preset_name):
        return self.preset_map.get(preset_name)

    def set_preset_channels(self, preset_name, selected_items, sync=True):
        if isinstance(selected_items, QStringListModel):
            channel_list = selected_items
        else:
            channel_list = QStringListModel([])
            channel_list.setStringList(selected_items)
        self.preset_map[preset_name] = channel_list
        if sync:
            _sync_settings(self)

    def rename_preset(self, preset_name, new_name):
        self.preset_map[new_name] = self.preset_map[preset_name]
        del self.preset_map[preset_name]
        _sync_settings(self)

    def delete_preset(self, preset_name):
        del self.preset_map[preset_name]
        _sync_settings(self)

    def updateItem(self, preset_name, selected_items):
        channel_list = self.get_channel_list()
        channel_list.setStringList(selected_items)
        self.preset_map[preset_name] = channel_list
