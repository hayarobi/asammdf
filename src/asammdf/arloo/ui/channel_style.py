# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channel_style.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ChannelStyleDialog(object):
    def setupUi(self, ChannelStyleDialog):
        if not ChannelStyleDialog.objectName():
            ChannelStyleDialog.setObjectName(u"ChannelStyleDialog")
        ChannelStyleDialog.resize(320, 240)
        self.verticalLayoutWidget = QWidget(ChannelStyleDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 301, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineStyleBox = QComboBox(self.verticalLayoutWidget)
        self.lineStyleBox.setObjectName(u"lineStyleBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineStyleBox)

        self.lineColorButton = QPushButton(self.verticalLayoutWidget)
        self.lineColorButton.setObjectName(u"lineColorButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineColorButton)

        self.lineWidthBox = QComboBox(self.verticalLayoutWidget)
        self.lineWidthBox.setObjectName(u"lineWidthBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineWidthBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ChannelStyleDialog)
        self.buttonBox.accepted.connect(ChannelStyleDialog.accept)
        self.buttonBox.rejected.connect(ChannelStyleDialog.reject)

        QMetaObject.connectSlotsByName(ChannelStyleDialog)
    # setupUi

    def retranslateUi(self, ChannelStyleDialog):
        ChannelStyleDialog.setWindowTitle(QCoreApplication.translate("ChannelStyleDialog", u"channel_name", None))
        self.label.setText(QCoreApplication.translate("ChannelStyleDialog", u"\uc120 \uad75\uae30", None))
        self.label_2.setText(QCoreApplication.translate("ChannelStyleDialog", u"\uc120 \ubaa8\uc591", None))
        self.lineColorButton.setText(QCoreApplication.translate("ChannelStyleDialog", u"\uc0c9\uc0c1 \uc120\ud0dd", None))
    # retranslateUi

