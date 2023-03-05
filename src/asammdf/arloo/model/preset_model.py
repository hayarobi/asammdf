from typing import Optional

from PySide6.QtCore import QStringListModel


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


class PresetModel(SingletonInstance):
    def __init__(self):
        self.list = QStringListModel(["row1", "row2"])
        # settings = QSettings()
        # settings.value()

    def updateItem(self, selected_items):
        self.list.setStringList(selected_items)

