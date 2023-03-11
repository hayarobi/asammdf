from PySide6.QtCore import QObject, QPointF, QEventLoop
from PySide6.QtGui import QFont, QPainter
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PySide6.QtWidgets import QDialog


class PrintHandler(QObject):
    def  __init__(self, parent):
        super().__init__(parent)
        self.view = None;
        self.printer = QPrinter()
        self.printer.setResolution(72)
        self._waitForResult = QEventLoop()
        self._inPrintPreview = False;

    def setView(self, view):
        assert not self.view
        self.view = view
        view.printRequested.connect(self.printPreview)
        view.printFinished.connect(self.printFinished)

    def print(self):
        dialog = QPrintDialog(self.printer, self.view)
        if dialog.exec() != QDialog.Accepted :
            return
        self.printDocument(self.printer)

    def printDocument(self, printer):
        self.view.print(printer)
        self._waitForResult.exec()

    def printFinished(self, success):
        if not success:
            painter = QPainter()
            if painter.begin(self.printer) :
                font = painter.font()
                font.setPixelSize(20)
                painter.setFont(font)
                painter.drawText(QPointF(10,25), "Could not generate print preview.")
                painter.end()
        self._waitForResult.quit()

    def printPreview(self):
        if self.view is None:
            return
        if self._inPrintPreview:
            return
        self._inPrintPreview = True
        preview = QPrintPreviewDialog(self.printer, self.view)
        preview.paintRequested.connect(self.printDocument)
        preview.exec()
        self._inPrintPreview = False
