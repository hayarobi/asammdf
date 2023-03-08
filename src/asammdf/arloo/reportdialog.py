from PySide6 import QtCore
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QDialog

from asammdf.arloo.model.report_data import ReportData
from asammdf.arloo.ui.report_dialog import Ui_report_dialog


class ReportDialog(Ui_report_dialog, QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self._settings = QtCore.QSettings()
        self.setupUi(self)
        self.report_data = None
        self.titleEdit.setText(self._settings.value("report.title"))
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.authorEdit.setText(self._settings.value("report.author"))


    def accept(self) -> None:
        data = ReportData()
        data.title = self.titleEdit.text()
        data.date = self.dateEdit.dateTime().toPython()
        data.author = self.authorEdit.text()
        data.description = self.descriptionEdit.document().toHtml()
        self.report_data = data
        self._settings.setValue("report.title", data.title)
        self._settings.setValue("report.author", data.author)

        super().accept()

    def reject(self) -> None:
        super().reject()


