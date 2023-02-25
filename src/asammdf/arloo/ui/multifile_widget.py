# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multifile_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MultiFileWidget(object):
    def setupUi(self, MultiFileWidget):
        if not MultiFileWidget.objectName():
            MultiFileWidget.setObjectName(u"MultiFileWidget")
        MultiFileWidget.resize(717, 387)
        self.verticalLayoutWidget = QWidget(MultiFileWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 691, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mdfListView = QListView(self.verticalLayoutWidget)
        self.mdfListView.setObjectName(u"mdfListView")

        self.verticalLayout.addWidget(self.mdfListView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.extractButton = QPushButton(MultiFileWidget)
        self.extractButton.setObjectName(u"extractButton")
        self.extractButton.setGeometry(QRect(10, 350, 111, 32))
        self.extractButton.setAutoDefault(True)
        self.addButton = QPushButton(MultiFileWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(598, 350, 101, 32))
        self.addButton.setAutoDefault(True)
        self.removeButton = QPushButton(MultiFileWidget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(480, 350, 101, 32))
        self.removeButton.setAutoDefault(True)

        self.retranslateUi(MultiFileWidget)

        QMetaObject.connectSlotsByName(MultiFileWidget)
    # setupUi

    def retranslateUi(self, MultiFileWidget):
        MultiFileWidget.setWindowTitle(QCoreApplication.translate("MultiFileWidget", u"MDFFiles", None))
        self.extractButton.setText(QCoreApplication.translate("MultiFileWidget", u"Extract", None))
        self.addButton.setText(QCoreApplication.translate("MultiFileWidget", u"Add File", None))
        self.removeButton.setText(QCoreApplication.translate("MultiFileWidget", u"Remove File", None))
    # retranslateUi

