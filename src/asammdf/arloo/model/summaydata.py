from PySide6.QtCore import Signal, QObject
from future.backports.datetime import timedelta

from asammdf.arloo.model.signal_summary import SignalSummary, UNDEFINED, START_NOT_SELECTED, END_NOT_SELECTED

DUMMY_SIGNAL_SUMMARY = SignalSummary(None, "select channel!")
class SummaryData(QObject):
    valueChangedSignal = Signal(object)

    def __init__(self, origin_time):
        super().__init__(None)
        self.signal = DUMMY_SIGNAL_SUMMARY
        self.start_delta = START_NOT_SELECTED
        self.end_delta = END_NOT_SELECTED
        self.origin_time = origin_time

    def _clear(self):
        self.signal = DUMMY_SIGNAL_SUMMARY

    def channel_name(self):
        return self.signal.name

    def minimum(self):
        return self.signal.minimum

    def maximum(self):
        return self.signal.maximum

    def average(self):
        return self.signal.average

    def set_signal(self, signal, origin_time):
        self.origin_time = origin_time
        self.signal = SignalSummary(signal, signal.name, self.start_delta, self.end_delta)
        self.valueChangedSignal.emit(self)

    def set_start_delta(self, start_delta):
        if start_delta is None:
            self.start_delta = START_NOT_SELECTED
        else:
            if start_delta >= self.end_delta:
                return False
            self.start_delta = start_delta
        if self.signal is not None:
            self.signal.set_time_range(self.start_delta, self.end_delta)
            self.valueChangedSignal.emit(self)
        return True

    def get_start_time(self):
        if self.start_delta == START_NOT_SELECTED:
            return None
        else:
            time = self.origin_time + timedelta(seconds=self.start_delta)
            return time

    def set_end_delta(self, end_delta):
        if end_delta is None:
            self.end_delta = END_NOT_SELECTED
        else:
            if end_delta <= self.start_delta:
                return False
            self.end_delta = end_delta
        if self.signal is not None:
            self.signal.set_time_range(self.start_delta, self.end_delta)
            self.valueChangedSignal.emit(self)
        return True

    def get_end_time(self):
        """
        :return: datatime 값 혹은 None을 리턴한다.
        """
        if self.end_delta == END_NOT_SELECTED:
            return None
        else:
            time = self.origin_time + timedelta(seconds=self.end_delta)
            return time