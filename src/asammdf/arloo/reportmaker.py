import base64
from datetime import timedelta

from PySide6.QtCore import QFile, QByteArray, QBuffer, QIODevice

from asammdf.arloo.model.signal_summary import START_NOT_SELECTED, SignalSummary
from asammdf.arloo.model.summaydata import SummaryData
from asammdf.arloo.reportdialog import ReportDialog
from asammdf.arloo.reportresultdialog import ReportResultDialog


class ReportMaker:
    # 재활용을 하는 객체이다.
    def __init__(self, plot, summry_data:SummaryData):
        self.plot_widget = plot
        self.summary_data = summry_data
        self.ci_dataurl = self.get_ci_iamge_dataurl()
        self.graph_dataurl = None
        self.signal_summaries = None

    def make_report(self):
        start_time = self.summary_data.get_start_time()
        if start_time is None:
            # FIXME 코드스멜 시그널 선택을 명시적으로 하지 않아도 시작과 종료 시각은 따로 있을 수 있다.
            self.start_time = self.summary_data.origin_time
        end_time = self.summary_data.get_end_time()
        self.graph_dataurl = self.get_plot_graph_dataurl()
        if end_time is None:
            # FIXME 코드스멜 시그널 선택을 명시적으로 하지 않아도 시작과 종료 시각은 따로 있을 수 있다.
            self.end_time = self.summary_data.origin_time + timedelta(seconds=1000000)
        self.signal_summaries = self.get_signal_summaries(self.summary_data.start_delta
                                                     , self.summary_data.end_delta)

        dialog = ReportDialog(self.plot_widget, self)
        result = dialog.exec()
        # if result:
        #     report_data = dialog.report_data
        #     report_data.graph_image = self.graph_dataurl
        #     report_data.ci_image = self.ci_dataurl
        #     report_data.start_time = start_time
        #     report_data.end_time = end_time
        #     report_data.summaries = signal_summaries
        #     result_dialog = ReportResultDialog(self.plot_widget, report_data)
        #     result_dialog.show()

    def get_ci_iamge_dataurl(self):
        stream = QFile(':/everCI.png')
        if stream.open(QFile.ReadOnly):
            base64_utf8_str = base64.b64encode(stream.readAll().data()).decode('utf-8')
            ci_dataurl = f'data:image/png;base64,{base64_utf8_str}'
            stream.close()
        else:
            print(stream.errorString())
        return ci_dataurl

    def get_plot_graph_dataurl(self):
        # generate something to export
        plt = self.plot_widget.plot
        image_bytes = QByteArray()
        buffer = QBuffer(image_bytes)
        buffer.open(QIODevice.WriteOnly)
        plt.grab().save(buffer, "PNG")  # writes pixmap into bytes in PNG format
        base64_utf8_str = base64.b64encode(image_bytes.data()).decode('utf-8')
        dataurl = f'data:image/png;base64,{base64_utf8_str}'

        return dataurl

    def get_signal_summaries(self, start_delta, end_delta):
        summaries = []
        plt = self.plot_widget.plot
        for sig in plt.signals:
            signal_summary = SignalSummary(sig, sig.name, start_delta, end_delta)
            summaries.append(signal_summary)
        return summaries



