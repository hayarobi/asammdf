from asammdf.arloo.model.signal_summary import SignalSummary


class ReportData:
    def __init__(self):
        self.subject = None
        self.vehicle_number = None
        self.date = None
        self.author = None
        self.work_order = None
        self.graph_image = None
        self.ci_image = None
        self.events = []
        self.axis_1_si = 0.0
        self.axis_2_si = 0.0
        self.axis_3_si = 0.0
        self.axis_4_si = 0.0

    def add_event(self, event: SignalSummary):
        self.events.append(event)


