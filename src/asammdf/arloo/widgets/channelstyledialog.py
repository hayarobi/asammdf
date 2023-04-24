from PySide6 import QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QDialog, QColorDialog

from asammdf.arloo.ui.channel_style import Ui_ChannelStyleDialog

ROLE_LINE_STYLE = 112

LINE_STYLES = (
    (QtCore.Qt.PenStyle.SolidLine,'실선'),
    (QtCore.Qt.PenStyle.DashLine, '대시'),
    (QtCore.Qt.PenStyle.DotLine, '점선'),
    (QtCore.Qt.PenStyle.DashDotLine,'대시점'),
    (QtCore.Qt.PenStyle.DashDotDotLine,'대시점점')
)


def line_style(style, name):
    item = QStandardItem(name)
    item.setData(style, ROLE_LINE_STYLE)
    return item


class ChannelStyleDialog(Ui_ChannelStyleDialog, QDialog):
    def __init__(self, signal):
        super(Ui_ChannelStyleDialog, self).__init__()
        self.setupUi(self)
        self._signal = signal
        self.style_info = {}

        self.setWindowTitle(self._signal.view_name)
        # 선 굵기
        for width in range(1,10):
            self.lineWidthBox.addItem(str(width))
        # 선 속성
        line_style_model = QStandardItemModel()
        for style in LINE_STYLES:
            line_style_model.appendRow(line_style(style[0], style[1]))
        self.lineStyleBox.setModel(line_style_model)
        # 선 색상
        self.line_color = signal.color
        self.lineColorButton.clicked.connect(self.open_color_selector)

    def open_color_selector(self):
        color = QColorDialog.getColor(self.line_color)
        if color.isValid():
            self.line_color = color

    def accept(self) -> None:
        self.style_info['width'] = int(self.lineWidthBox.currentText())
        self.style_info['style'] = self.lineStyleBox.currentData(ROLE_LINE_STYLE)
        self.style_info['color'] = self.line_color
        super().accept()



