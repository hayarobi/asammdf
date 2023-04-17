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
        self.start_time = None
        self.end_time = None
        self.description = None
        self.summaries = []

    def add_summary(self, event: SignalSummary):
        self.summaries.append(event)


