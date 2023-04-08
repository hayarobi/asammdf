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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_report_dialog(object):
    def setupUi(self, report_dialog):
        if not report_dialog.objectName():
            report_dialog.setObjectName(u"report_dialog")
        report_dialog.resize(400, 621)
        self.buttonBox = QDialogButtonBox(report_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 570, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(report_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 362, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_3.addWidget(self.label_12)

        self.subjectEdit = QLineEdit(self.verticalLayoutWidget)
        self.subjectEdit.setObjectName(u"subjectEdit")

        self.horizontalLayout_3.addWidget(self.subjectEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.label)

        self.vehicleNumberEdit = QLineEdit(self.verticalLayoutWidget)
        self.vehicleNumberEdit.setObjectName(u"vehicleNumberEdit")

        self.horizontalLayout.addWidget(self.vehicleNumberEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.dateEdit = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 12, 29), QTime(18, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.authorEdit = QLineEdit(self.verticalLayoutWidget)
        self.authorEdit.setObjectName(u"authorEdit")

        self.horizontalLayout_4.addWidget(self.authorEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, 0, 5)
        self.workOrderLabel = QLabel(self.verticalLayoutWidget)
        self.workOrderLabel.setObjectName(u"workOrderLabel")
        self.workOrderLabel.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_6.addWidget(self.workOrderLabel)

        self.workOrderEdit = QLineEdit(self.verticalLayoutWidget)
        self.workOrderEdit.setObjectName(u"workOrderEdit")

        self.horizontalLayout_6.addWidget(self.workOrderEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, 0, 5)
        self.workOrderLabel_2 = QLabel(self.verticalLayoutWidget)
        self.workOrderLabel_2.setObjectName(u"workOrderLabel_2")

        self.horizontalLayout_7.addWidget(self.workOrderLabel_2)

        self.axis1Edit = QLineEdit(self.verticalLayoutWidget)
        self.axis1Edit.setObjectName(u"axis1Edit")

        self.horizontalLayout_7.addWidget(self.axis1Edit)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.axis1PoundEdit = QLineEdit(self.verticalLayoutWidget)
        self.axis1PoundEdit.setObjectName(u"axis1PoundEdit")
        self.axis1PoundEdit.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.axis1PoundEdit)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 5, 0, 5)
        self.workOrderLabel_3 = QLabel(self.verticalLayoutWidget)
        self.workOrderLabel_3.setObjectName(u"workOrderLabel_3")

        self.horizontalLayout_8.addWidget(self.workOrderLabel_3)

        self.axis2Edit = QLineEdit(self.verticalLayoutWidget)
        self.axis2Edit.setObjectName(u"axis2Edit")

        self.horizontalLayout_8.addWidget(self.axis2Edit)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.axis2PoundEdit = QLineEdit(self.verticalLayoutWidget)
        self.axis2PoundEdit.setObjectName(u"axis2PoundEdit")
        self.axis2PoundEdit.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.axis2PoundEdit)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, 0, 5)
        self.workOrderLabel_4 = QLabel(self.verticalLayoutWidget)
        self.workOrderLabel_4.setObjectName(u"workOrderLabel_4")

        self.horizontalLayout_9.addWidget(self.workOrderLabel_4)

        self.axis3Edit = QLineEdit(self.verticalLayoutWidget)
        self.axis3Edit.setObjectName(u"axis3Edit")

        self.horizontalLayout_9.addWidget(self.axis3Edit)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.axis3PoundEdit = QLineEdit(self.verticalLayoutWidget)
        self.axis3PoundEdit.setObjectName(u"axis3PoundEdit")
        self.axis3PoundEdit.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.axis3PoundEdit)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 5, 0, 5)
        self.workOrderLabel_5 = QLabel(self.verticalLayoutWidget)
        self.workOrderLabel_5.setObjectName(u"workOrderLabel_5")

        self.horizontalLayout_10.addWidget(self.workOrderLabel_5)

        self.axis4Edit = QLineEdit(self.verticalLayoutWidget)
        self.axis4Edit.setObjectName(u"axis4Edit")

        self.horizontalLayout_10.addWidget(self.axis4Edit)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.axis4PoundEdit = QLineEdit(self.verticalLayoutWidget)
        self.axis4PoundEdit.setObjectName(u"axis4PoundEdit")
        self.axis4PoundEdit.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.axis4PoundEdit)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.retranslateUi(report_dialog)
        self.buttonBox.accepted.connect(report_dialog.accept)
        self.buttonBox.rejected.connect(report_dialog.reject)

        QMetaObject.connectSlotsByName(report_dialog)
    # setupUi

    def retranslateUi(self, report_dialog):
        report_dialog.setWindowTitle(QCoreApplication.translate("report_dialog", u"\ub9ac\ud3ec\ud2b8", None))
        self.label_12.setText(QCoreApplication.translate("report_dialog", u"\uc8fc\uc81c", None))
        self.label.setText(QCoreApplication.translate("report_dialog", u"\ucc28\ub7c9\ubc88\ud638", None))
        self.label_2.setText(QCoreApplication.translate("report_dialog", u"\uc791\uc5c5\uc77c", None))
        self.label_3.setText(QCoreApplication.translate("report_dialog", u"\uc791\uc5c5\uc790", None))
        self.workOrderLabel.setText(QCoreApplication.translate("report_dialog", u"\uc7a5\uc560\uc77c\uc2dc ", None))
        self.workOrderLabel_2.setText(QCoreApplication.translate("report_dialog", u"Axis 1", None))
        self.label_4.setText(QCoreApplication.translate("report_dialog", u"kN", None))
        self.label_8.setText(QCoreApplication.translate("report_dialog", u"lbs", None))
        self.workOrderLabel_3.setText(QCoreApplication.translate("report_dialog", u"Axis 2", None))
        self.label_5.setText(QCoreApplication.translate("report_dialog", u"kN", None))
        self.label_9.setText(QCoreApplication.translate("report_dialog", u"lbs", None))
        self.workOrderLabel_4.setText(QCoreApplication.translate("report_dialog", u"Axis 3", None))
        self.label_6.setText(QCoreApplication.translate("report_dialog", u"kN", None))
        self.label_10.setText(QCoreApplication.translate("report_dialog", u"lbs", None))
        self.workOrderLabel_5.setText(QCoreApplication.translate("report_dialog", u"Axis 4", None))
        self.label_7.setText(QCoreApplication.translate("report_dialog", u"kN", None))
        self.label_11.setText(QCoreApplication.translate("report_dialog", u"lbs", None))
    # retranslateUi

