# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_result_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_report_result_dialog(object):
    def setupUi(self, report_result_dialog):
        if not report_result_dialog.objectName():
            report_result_dialog.setObjectName(u"report_result_dialog")
        report_result_dialog.resize(1041, 1129)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(report_result_dialog.sizePolicy().hasHeightForWidth())
        report_result_dialog.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget = QWidget(report_result_dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 1070, 1011, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.closeButton = QPushButton(self.horizontalLayoutWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.closeButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.printButton = QPushButton(self.horizontalLayoutWidget)
        self.printButton.setObjectName(u"printButton")

        self.horizontalLayout.addWidget(self.printButton)

        self.saveButton = QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)


        self.retranslateUi(report_result_dialog)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(report_result_dialog)
    # setupUi

    def retranslateUi(self, report_result_dialog):
        report_result_dialog.setWindowTitle(QCoreApplication.translate("report_result_dialog", u"Report", None))
        self.closeButton.setText(QCoreApplication.translate("report_result_dialog", u"Close", None))
        self.printButton.setText(QCoreApplication.translate("report_result_dialog", u"Print", None))
        self.saveButton.setText(QCoreApplication.translate("report_result_dialog", u"Save", None))
    # retranslateUi

