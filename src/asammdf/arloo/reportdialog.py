from pydoc import html

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QDateTime, QTimer
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QDialog, QMessageBox, QTreeWidgetItem
from jinja2 import Environment, PackageLoader, select_autoescape
from numpy import double

from asammdf.arloo.arloos import DEFAULT_TIME_ZONE
from asammdf.arloo.model.report_data import ReportData
from asammdf.arloo.printhandler import PrintHandler
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
    def __init__(self, parent, data_provider):
        super().__init__(parent)

        self._settings = QtCore.QSettings()
        self.setupUi(self)
        self._data_provider = data_provider

        self._signal_summaries = data_provider.signal_summaries
        for signal_summary in self._signal_summaries:
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

        # preview 영역 구성
        self.web_view = QWebEngineView(self.verticalLayoutWidget_2)
        self.previewLayout.addWidget(self.web_view)
        self.web_view.setZoomFactor(0.75)
        # self.web_view.setHtml("<html><body></body></html>")
        self.init_webview()

        # 입력값 변경 감지부
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_preview)
        self.subjectEdit.textEdited.connect(self.update_render_timer)
        self.vehicleNumberEdit.textEdited.connect(self.update_render_timer)
        self.authorEdit.textEdited.connect(self.update_render_timer)
        self.dateEdit.dateChanged.connect(self.update_render_timer)
        self.descriptionEdit.textChanged.connect(self.update_render_timer)

        self.saveButton.clicked.connect(self.save_to_pdf)
        self.closeButton.clicked.connect(self.reject)
        self.printButton.clicked.connect(self.printPage)

    def init_webview(self):
        env = Environment(
            loader=PackageLoader("asammdf.arloo"),
            autoescape=select_autoescape()
        )
        # self.web_view.setHtml(report_data.description)
        report_template = "report_tmpl.html"
        self.preview_template = env.get_template(report_template)
        # 최초 preview를 보여주는 용도
        self.update_preview()

    def update_render_timer(self):
        self.timer.start()

    def update_preview(self,*args,**kwargs):
        report_data = self.refresh_report_data()
        rendered = self.preview_template.render(data=report_data,
                                   graph_image=report_data.graph_image,
                                   ci_image=report_data.ci_image
                                   )
        self.web_view.setHtml(rendered)

    def accept(self) -> None:
        self.refresh_report_data()

        super().accept()

    def refresh_report_data(self):
        data = ReportData()
        data.subject = self.subjectEdit.text()
        data.vehicle_number = self.vehicleNumberEdit.text()
        data.start_time = self._data_provider.start_time
        data.end_time = self._data_provider.end_time
        data.summaries = self._data_provider.signal_summaries
        data.date = self.dateEdit.dateTime().toPython().astimezone(DEFAULT_TIME_ZONE).strftime("%Y-%m-%d")
        data.author = self.authorEdit.text()
        data.work_order = self.workOrderEdit.text()
        data.description = self.descriptionEdit.toHtml()
        data.ci_image = self._data_provider.ci_dataurl
        data.graph_image = self._data_provider.graph_dataurl
        self.report_data = data
        return self.report_data

    def save_to_settings(self):
        self._settings.setValue("report.subject", self.report_data.subject)
        self._settings.setValue("report.vehicle_number", self.report_data.vehicle_number)
        self._settings.setValue("report.author", self.report_data.author)

    def reject(self) -> None:
        super().reject()

    def save_to_pdf(self) -> None:
        filter = "PDF files (*.pdf)"
        suffix = ".pdf"

        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Select report file to Save",
            None,
            f"{filter};;All files (*.*)",
            filter,
        )
        if not file_name:
            return
        self.web_view.page().printToPdf(file_name)
        self.save_to_settings()
        # self.close()

    def reject(self) -> None:
        super().reject()

    def printPage(self) -> None:
        self.refresh_report_data()
        handler = PrintHandler(self)
        handler.setView(self.web_view)
        handler.print_preview()
        self.save_to_settings()
