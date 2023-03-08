import os

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QRect, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QDialog
from jinja2 import Environment, PackageLoader, select_autoescape, Template

from asammdf.arloo.ui.report_result_dialog import Ui_report_result_dialog


class ReportResultDialog(Ui_report_result_dialog, QDialog):
    def __init__(self, parent, report_data):
        super().__init__(parent)
        self._settings = QtCore.QSettings()
        self.setupUi(self)

        parent_geometry = self.geometry()
        webview_geometry = QRect(20, 20, parent_geometry.width() - 40, parent_geometry.height() - 120)
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(webview_geometry)

        self.saveButton.clicked.connect(self.save)
        self.closeButton.clicked.connect(self.reject)

        self.report_data = report_data

        env = Environment(
            loader=PackageLoader("asammdf.arloo"),
            autoescape=select_autoescape()
        )
        # self.web_view.setHtml(report_data.description)
        dumb_htmlfile = "dumb_report.html"
        template = env.get_template(dumb_htmlfile)
        rendered = template.render(title=report_data.title, author=report_data.author, created_date=report_data.date,
                                   graph_image="./graph_1.png")
        self.web_view.setHtml(rendered)

    def save(self) -> None:
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

    def reject(self) -> None:
        super().reject()
