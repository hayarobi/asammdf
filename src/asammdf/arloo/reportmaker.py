import base64

from PySide6.QtCore import QFile, QByteArray, QBuffer, QIODevice

from asammdf.arloo.reportdialog import ReportDialog
from asammdf.arloo.reportresultdialog import ReportResultDialog


class ReportMaker:
    def __init__(self, plot):
        self.plot_widget = plot

    def make_report(self):
        image_bytes = self.get_plot_image()
        base64_utf8_str = base64.b64encode(image_bytes.data()).decode('utf-8')
        dataurl = f'data:image/png;base64,{base64_utf8_str}'

        stream = QFile(':/everCI.png')
        if stream.open(QFile.ReadOnly):
            base64_utf8_str = base64.b64encode(stream.readAll().data()).decode('utf-8')
            ci_dataurl = f'data:image/png;base64,{base64_utf8_str}'
            stream.close()
        else:
            print(stream.errorString())
        dialog = ReportDialog(self.plot_widget)
        result = dialog.exec()
        if result:
            report_data = dialog.report_data
            report_data.graph_image = dataurl
            report_data.ci_image = ci_dataurl
            result_dialog = ReportResultDialog(self.plot_widget, report_data)
            result_dialog.show()

    def get_plot_image(self):
        # generate something to export
        plt = self.plot_widget.plot
        image_bytes = QByteArray()
        buffer = QBuffer(image_bytes)
        buffer.open(QIODevice.WriteOnly)
        plt.grab().save(buffer, "PNG")  # writes pixmap into bytes in PNG format
        return image_bytes

