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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_MultiFileWidget(object):
    def setupUi(self, MultiFileWidget):
        if not MultiFileWidget.objectName():
            MultiFileWidget.setObjectName(u"MultiFileWidget")
        MultiFileWidget.resize(1024, 459)
        MultiFileWidget.setMinimumSize(QSize(1024, 0))
        self.verticalLayoutWidget = QWidget(MultiFileWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1001, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mdfListView = QTableView(self.verticalLayoutWidget)
        self.mdfListView.setObjectName(u"mdfListView")

        self.verticalLayout.addWidget(self.mdfListView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mergeSaveButton = QPushButton(self.verticalLayoutWidget)
        self.mergeSaveButton.setObjectName(u"mergeSaveButton")
        self.mergeSaveButton.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.mergeSaveButton)

        self.batchConvertButton = QPushButton(self.verticalLayoutWidget)
        self.batchConvertButton.setObjectName(u"batchConvertButton")
        self.batchConvertButton.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.batchConvertButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.removeButton = QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.removeButton)

        self.addButton = QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.addButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MultiFileWidget)

        QMetaObject.connectSlotsByName(MultiFileWidget)
    # setupUi

    def retranslateUi(self, MultiFileWidget):
        MultiFileWidget.setWindowTitle(QCoreApplication.translate("MultiFileWidget", u"MDFFiles", None))
        self.mergeSaveButton.setText(QCoreApplication.translate("MultiFileWidget", u"\ubcd1\ud569 \uc800\uc7a5", None))
        self.batchConvertButton.setText(QCoreApplication.translate("MultiFileWidget", u"\uac1c\ubcc4 \uc77c\uad04 \uc800\uc7a5", None))
        self.removeButton.setText(QCoreApplication.translate("MultiFileWidget", u"\ud30c\uc77c \uc0ad\uc81c", None))
        self.addButton.setText(QCoreApplication.translate("MultiFileWidget", u"\ud30c\uc77c \ucd94\uac00", None))
    # retranslateUi

