import datetime
import logging

from PySide6.QtWidgets import QWidget, QMessageBox
from qtpy import QtCore

from asammdf.arloo.model.summaydata import SummaryData
from asammdf.arloo.ui.summary_form import Ui_summaryForm
from asammdf.gui.widgets.tree import ChannelsTreeItem


def time_to_str(time: datetime):
    if time is None:
        return "_"
    else:
        return time.strftime("%Y-%m-%d %H:%M:%S")


class SummaryForm(Ui_summaryForm, QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(SummaryForm, self).__init__(parent, *args, **kwargs)
        # super(Ui_summaryForm, self).__init__()
        self.setupUi(self)
        self._settings = QtCore.QSettings()
        self.parent_plot = parent
        self.summary_data = SummaryData(self.parent_plot.origin)
        self.summary_data.valueChangedSignal.connect(self.update_fields)

    def update_fields(self, event):
        self.channelNameLabel.setText(self.summary_data.channel_name())
        self.startTimeEdit.setText(time_to_str(self.summary_data.get_start_time()))
        self.endTimeEdit.setText(time_to_str(self.summary_data.get_end_time()))
        self.minimumEdit.setText(str(self.summary_data.minimum()))
        self.maximumEdit.setText(str(self.summary_data.maximum()))
        self.averageEdit.setText(str(self.summary_data.average()))
        self.update()

    def channel_selection_row_changed(self, current, previous):
        selected_channel = None
        if not self.parent_plot.closed:
            if current and current.type() == ChannelsTreeItem.Channel:
                item = current
                uuid = item.uuid
                self.info_uuid = uuid
                selected_channel = item.signal

        self.summary_data.set_signal(selected_channel, self.parent_plot.origin)

    def handle_set_start_time(self, start_time):
        if not self.summary_data.set_start_delta(start_time):
            QMessageBox.critical(
                self,
                "시작 시각 설정 실패",
                "시작 시각이 종료 시각보다 늦습니다.",
            )

    def handle_set_end_time(self, end_time):
        if not self.summary_data.set_end_delta(end_time):
            QMessageBox.critical(
                self,
                "종료 시각 설정 실패",
                "종료 시각이 시작 시각보다 빠릅니다.",
            )

