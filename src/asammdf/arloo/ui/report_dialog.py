# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_report_dialog(object):
    def setupUi(self, report_dialog):
        if not report_dialog.objectName():
            report_dialog.setObjectName(u"report_dialog")
        report_dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(report_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(report_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 361, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.label)

        self.titleEdit = QLineEdit(self.verticalLayoutWidget)
        self.titleEdit.setObjectName(u"titleEdit")

        self.horizontalLayout.addWidget(self.titleEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.dateEdit = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(15, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.authorEdit = QLineEdit(self.verticalLayoutWidget)
        self.authorEdit.setObjectName(u"authorEdit")

        self.horizontalLayout_4.addWidget(self.authorEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.descriptionEdit = QTextEdit(self.verticalLayoutWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.horizontalLayout_5.addWidget(self.descriptionEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(report_dialog)
        self.buttonBox.accepted.connect(report_dialog.accept)
        self.buttonBox.rejected.connect(report_dialog.reject)

        QMetaObject.connectSlotsByName(report_dialog)
    # setupUi

    def retranslateUi(self, report_dialog):
        report_dialog.setWindowTitle(QCoreApplication.translate("report_dialog", u"Reporting", None))
        self.label.setText(QCoreApplication.translate("report_dialog", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("report_dialog", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("report_dialog", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("report_dialog", u"Description", None))
    # retranslateUi

