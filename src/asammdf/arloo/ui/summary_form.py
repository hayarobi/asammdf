# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'summary_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_summaryForm(object):
    def setupUi(self, summaryForm):
        if not summaryForm.objectName():
            summaryForm.setObjectName(u"summaryForm")
        summaryForm.resize(349, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(summaryForm.sizePolicy().hasHeightForWidth())
        summaryForm.setSizePolicy(sizePolicy)
        summaryForm.setMinimumSize(QSize(0, 280))
        summaryForm.setMaximumSize(QSize(16777215, 280))
        self.verticalLayoutWidget = QWidget(summaryForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 331, 270))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.channelNameLabel = QLabel(self.verticalLayoutWidget)
        self.channelNameLabel.setObjectName(u"channelNameLabel")

        self.verticalLayout.addWidget(self.channelNameLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.startTimeEdit = QLineEdit(self.verticalLayoutWidget)
        self.startTimeEdit.setObjectName(u"startTimeEdit")
        self.startTimeEdit.setEnabled(False)

        self.verticalLayout_2.addWidget(self.startTimeEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.endTimeEdit = QLineEdit(self.verticalLayoutWidget)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        self.endTimeEdit.setEnabled(False)

        self.verticalLayout_4.addWidget(self.endTimeEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.minimumEdit = QLineEdit(self.verticalLayoutWidget)
        self.minimumEdit.setObjectName(u"minimumEdit")
        self.minimumEdit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.minimumEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.maximumEdit = QLineEdit(self.verticalLayoutWidget)
        self.maximumEdit.setObjectName(u"maximumEdit")
        self.maximumEdit.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.maximumEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.averageEdit = QLineEdit(self.verticalLayoutWidget)
        self.averageEdit.setObjectName(u"averageEdit")
        self.averageEdit.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.averageEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reportButton = QPushButton(self.verticalLayoutWidget)
        self.reportButton.setObjectName(u"reportButton")

        self.horizontalLayout_5.addWidget(self.reportButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.exportButton = QPushButton(self.verticalLayoutWidget)
        self.exportButton.setObjectName(u"exportButton")

        self.horizontalLayout_5.addWidget(self.exportButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(summaryForm)

        QMetaObject.connectSlotsByName(summaryForm)
    # setupUi

    def retranslateUi(self, summaryForm):
        summaryForm.setWindowTitle(QCoreApplication.translate("summaryForm", u"Form", None))
        self.channelNameLabel.setText(QCoreApplication.translate("summaryForm", u"_", None))
        self.label.setText(QCoreApplication.translate("summaryForm", u"StartTime", None))
        self.label_2.setText(QCoreApplication.translate("summaryForm", u"EndTime", None))
        self.label_3.setText(QCoreApplication.translate("summaryForm", u"Min", None))
        self.label_4.setText(QCoreApplication.translate("summaryForm", u"Max", None))
        self.label_5.setText(QCoreApplication.translate("summaryForm", u"Average", None))
        self.reportButton.setText(QCoreApplication.translate("summaryForm", u"\ub9ac\ud3ec\ud2b8", None))
        self.exportButton.setText(QCoreApplication.translate("summaryForm", u"CSV \ub0b4\ubcf4\ub0b4\uae30", None))
    # retranslateUi

