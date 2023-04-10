
UNDEFINED = ''
START_NOT_SELECTED = -10.0
END_NOT_SELECTED = 10000000000.0


class SignalSummary:
    def __init__(self, signal=None, name=None, start_time=START_NOT_SELECTED, end_time=END_NOT_SELECTED):
        self.name = name
        self.signal = signal
        self.start_time = start_time
        self.end_time = end_time

        # 파이썬은 무조건 이리 정의해야하나? _clear_values() 함수와 내용이 중복된다.
        self.samples = 0
        self.first_value = UNDEFINED
        self.last_value = UNDEFINED
        self.minimum = UNDEFINED
        self.maximum = UNDEFINED
        self.average = UNDEFINED

        self._calculate()

    def set_time_range(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self._calculate()

    def _calculate(self):
        if self.signal is None:
            return
        # if (self.start_time == START_NOT_SELECTED or
        #         self.end_time == END_NOT_SELECTED):
        #     self._clear_values()
        #     return

        values = self._collect_values(self.signal, self.start_time, self.end_time)
        if len(values) == 0:
            self._clear_values()
        else:
            self.samples = len(values)
            minimum = None
            maximum = None
            self.first_value = values[0]
            self.last_value = values[self.samples - 1]
            value_sum = 0.0
            for val in values:
                value_sum += val
                if minimum is None or minimum > val:
                    minimum = val
                if maximum is None or maximum < val:
                    maximum = val
                self.minimum = minimum
                self.maximum = maximum
            self.average = value_sum / len(values)

    def _clear_values(self):
        self.samples = 0
        self.first_value = UNDEFINED
        self.last_value = UNDEFINED
        self.minimum = UNDEFINED
        self.maximum = UNDEFINED
        self.average = UNDEFINED

    def _collect_values(self, signal, start_time, end_time):
        list = []
        for idx, x in enumerate(signal.timestamps):
            if start_time <= x <= end_time:
                list.append(signal.samples[idx])
        return list
