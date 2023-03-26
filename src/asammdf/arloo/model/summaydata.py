from datetime import datetime

from PySide6.QtCore import Signal, QObject
from future.backports.datetime import timedelta

UNDEFINED = ''


class SummaryData(QObject):
    valueChangedSignal = Signal(object)

    def __init__(self, origin_time):
        super().__init__(None)
        self.signal = None
        self.start_time = UNDEFINED
        self.end_time = UNDEFINED
        self.origin_time = origin_time
        self._clear()

    def _clear(self):
        self.minimum = UNDEFINED
        self.maximum = UNDEFINED
        self.average = UNDEFINED

    def channel_name(self):
        if self.signal is None:
            return "select channel!"
        else:
            return self.signal.name

    def set_signal(self, signal, origin_time):
        self.signal = signal
        self.origin_time = origin_time
        self._calculate()

    def set_start_time(self, start_time):
        if start_time is None:
            self.start_time = UNDEFINED
        else:
            self.start_time = start_time
        self._calculate()

    def get_start_time(self):
        if self.signal is None or self.start_time == UNDEFINED:
            return UNDEFINED
        else:
            time = self.origin_time + timedelta(seconds=self.start_time)
            return time.strftime("%Y-%m-%d %H-%M-%S")

    def set_end_time(self, end_time):
        if end_time is None:
            self.end_time = UNDEFINED
        else:
            self.end_time = end_time
        self._calculate()

    def get_end_time(self):
        if self.signal is None or self.end_time == UNDEFINED:
            return UNDEFINED
        else:
            time = self.origin_time + timedelta(seconds=self.end_time)
            return time.strftime("%Y-%m-%d %H-%M-%S")

    def _calculate(self):
        if (self.signal is None or
                self.start_time == UNDEFINED or
                self.end_time == UNDEFINED):
            self._clear()
        else:
            values = self._collect_values(self.signal, self.start_time, self.end_time)
            if len(values) == 0:
                self._clear()
            else:
                minimum = None
                maximum = None
                sum = 0.0
                for val in values:
                    sum += val
                    if minimum is None or minimum > val:
                        minimum = val
                    if maximum is None or maximum < val:
                        maximum = val
                    self.minimum = minimum
                    self.maximum = maximum
                    self.average = sum / len(values)
        self.valueChangedSignal.emit(self)

    def _collect_values(self, signal, start_time, end_time):
        list = []
        for idx, x in enumerate(signal.timestamps):
            if start_time <= x <= end_time:
                list.append(signal.samples[idx])
        return list
