from PySide6 import QtCore
from PySide6.QtWidgets import QDialog

from asammdf.arloo.model.preset_model import PresetModel
from asammdf.arloo.ui.report_dialog import Ui_report_dialog


class ReportDialog(Ui_report_dialog, QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self._settings = QtCore.QSettings()

    def accept(self) -> None:
        super().accept()

    def reject(self) -> None:
        super().reject()


