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
    QDialogButtonBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_report_dialog(object):
    def setupUi(self, report_dialog):
        if not report_dialog.objectName():
            report_dialog.setObjectName(u"report_dialog")
        report_dialog.resize(444, 708)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(report_dialog.sizePolicy().hasHeightForWidth())
        report_dialog.setSizePolicy(sizePolicy)
        self.buttonBox = QDialogButtonBox(report_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 660, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(report_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 411, 641))
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
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 12, 29), QTime(0, 0, 0)))

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

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.descriptionEdit = QTextEdit(self.verticalLayoutWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout.addWidget(self.descriptionEdit)

        self.summaries_widget = QTreeWidget(self.verticalLayoutWidget)
        self.summaries_widget.setObjectName(u"summaries_widget")
        self.summaries_widget.setColumnCount(5)

        self.verticalLayout.addWidget(self.summaries_widget)


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
        self.label_4.setText(QCoreApplication.translate("report_dialog", u" \uc124\uba85", None))
        ___qtreewidgetitem = self.summaries_widget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("report_dialog", u"\ud3c9\uade0", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("report_dialog", u"\ucd5c\ub300\uac12", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("report_dialog", u"\ucd5c\uc18c\uac12", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("report_dialog", u"\uc0d8\ud50c\uc218", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("report_dialog", u"\uc774\ub984", None));
    # retranslateUi

