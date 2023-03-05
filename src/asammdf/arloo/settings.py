from PySide6.QtCore import QSettings, QJsonArray


def init_settings():
    global settings
    settings = QSettings("CANViewer", "ARS Looper")
    settings.value("favorites",QJsonArray())
