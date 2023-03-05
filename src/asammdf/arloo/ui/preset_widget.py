# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preset_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_preset_widget(object):
    def setupUi(self, preset_widget):
        if not preset_widget.objectName():
            preset_widget.setObjectName(u"preset_widget")
        preset_widget.resize(764, 969)
        self.saveButton = QPushButton(preset_widget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(620, 920, 100, 32))
        self.itemListView = QListView(preset_widget)
        self.itemListView.setObjectName(u"itemListView")
        self.itemListView.setGeometry(QRect(10, 100, 711, 801))
        self.label = QLabel(preset_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 91, 16))
        self.presetNameEdit = QLineEdit(preset_widget)
        self.presetNameEdit.setObjectName(u"presetNameEdit")
        self.presetNameEdit.setGeometry(QRect(110, 70, 181, 21))
        self.cancelButton = QPushButton(preset_widget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(10, 920, 100, 32))
        self.loadButton = QPushButton(preset_widget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(520, 920, 100, 32))

        self.retranslateUi(preset_widget)

        self.saveButton.setDefault(False)
        self.loadButton.setDefault(False)


        QMetaObject.connectSlotsByName(preset_widget)
    # setupUi

    def retranslateUi(self, preset_widget):
        preset_widget.setWindowTitle(QCoreApplication.translate("preset_widget", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("preset_widget", u"Save", None))
        self.label.setText(QCoreApplication.translate("preset_widget", u"Preset Name", None))
        self.cancelButton.setText(QCoreApplication.translate("preset_widget", u"Cancel", None))
        self.loadButton.setText(QCoreApplication.translate("preset_widget", u"Load", None))
    # retranslateUi

