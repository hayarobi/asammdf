import logging

from PySide6.QtWidgets import QWidget
from qtpy import QtCore

from asammdf.arloo.model.summaydata import SummaryData
from asammdf.arloo.ui.summary_form import Ui_summaryForm
from asammdf.gui.widgets.tree import ChannelsTreeItem


class SummaryForm(Ui_summaryForm, QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(SummaryForm, self).__init__(parent, *args, **kwargs)
        # super(Ui_summaryForm, self).__init__()
        self.setupUi(self)
        self._settings = QtCore.QSettings()
        self.parent_plot = parent
        self.summary_data = SummaryData()
        self.summary_data.valueChangedSignal.connect(self.update_fields)

    def update_fields(self, event):
        self.channelNameLabel.setText(self.summary_data.channel_name())
        self.startTimeEdit.setText(str(self.summary_data.start_time))
        self.endTimeEdit.setText(str(self.summary_data.end_time))
        self.minimumEdit.setText(str(self.summary_data.minimum))
        self.maximumEdit.setText(str(self.summary_data.maximum))
        self.averageEdit.setText(str(self.summary_data.average))
        self.update()

    def channel_selection_row_changed(self, current, previous):
        selected_channel = None
        if not self.parent_plot.closed:
            if current and current.type() == ChannelsTreeItem.Channel:
                item = current
                uuid = item.uuid
                self.info_uuid = uuid
                selected_channel = item.signal

        self.summary_data.set_signal(selected_channel)

    def handle_set_start_time(self, start_time):
        self.summary_data.set_start_time(start_time)

    def handle_set_end_time(self, end_time):
        self.summary_data.set_end_time(end_time)
