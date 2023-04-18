from pydoc import html

from PySide6 import QtCore
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QDialog, QMessageBox, QTreeWidgetItem
from numpy import double

from asammdf.arloo.arloos import DEFAULT_TIME_ZONE
from asammdf.arloo.model.report_data import ReportData
from asammdf.arloo.ui.report_dialog import Ui_report_dialog

POUNDS_RATIO = 4.448


def to_number(value_str):
    return float(value_str)


def to_pound(value_si):
    value_yp = value_si / POUNDS_RATIO * 1000
    return value_yp


def is_float(value):
    if value is None:
        return False
    try:
        float(value)
        return True
    except:
        return False


class ReportDialog(Ui_report_dialog, QDialog):
    def __init__(self, parent, signal_summaries):
        super().__init__(parent)
        self._settings = QtCore.QSettings()
        self.setupUi(self)

        self._signal_summaries = signal_summaries
        for signal_summary in signal_summaries:
            sig_item = QTreeWidgetItem(self.summaries_widget)
            sig_item.setText(0, signal_summary.name)
            sig_item.setText(1, str(signal_summary.samples))
            sig_item.setText(2, str(signal_summary.minimum))
            sig_item.setText(3, str(signal_summary.maximum))
            sig_item.setText(4, str(signal_summary.average))

        self.report_data = None
        self.subjectEdit.setText(self._settings.value("report.subject"))
        self.vehicleNumberEdit.setText(self._settings.value("report.vehicle_number"))
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.authorEdit.setText(self._settings.value("report.author"))

    def accept(self) -> None:
        data = ReportData()
        # FIXME 타이틀 영역 추가하여 받아오도록 처리하자.
        data.subject = self.subjectEdit.text()
        data.vehicle_number = self.vehicleNumberEdit.text()
        data.date = self.dateEdit.dateTime().toPython().astimezone(DEFAULT_TIME_ZONE).strftime("%Y-%m-%d")
        data.author = self.authorEdit.text()
        data.work_order = self.workOrderEdit.text()
        data.description = self.descriptionEdit.toHtml()

        self.report_data = data
        self._settings.setValue("report.subject", data.subject)
        self._settings.setValue("report.vehicle_number", data.vehicle_number)
        self._settings.setValue("report.author", data.author)

        super().accept()

    def reject(self) -> None:
        super().reject()

    def updateAxis1Pound(self, stringValue):
        self.updateEdit(stringValue, self.axis1PoundEdit)

    def updateAxis2Pound(self, stringValue):
        self.updateEdit(stringValue, self.axis2PoundEdit)

    def updateAxis3Pound(self, stringValue):
        self.updateEdit(stringValue, self.axis3PoundEdit)

    def updateAxis4Pound(self, stringValue):
        self.updateEdit(stringValue, self.axis4PoundEdit)

    def updateEdit(self, stringValue, ypEdit):
        try:
            value_si = to_number(stringValue)
            value_yp = to_pound(value_si)
            ypEdit.setText(f"{value_yp:.1f}")
        except:
            ypEdit.setText("")
