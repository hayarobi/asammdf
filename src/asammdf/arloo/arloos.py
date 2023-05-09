from PySide6.QtCore import QTimeZone
from pytz import timezone
from datetime import datetime

# 한국
KST = timezone('Asia/Seoul')
DEFAULT_TIME_ZONE = KST
DEFAULT_Q_TIME_ZONE = QTimeZone(9*3600)
