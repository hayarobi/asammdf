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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_report_dialog(object):
    def setupUi(self, report_dialog):
        if not report_dialog.objectName():
            report_dialog.setObjectName(u"report_dialog")
        report_dialog.setWindowModality(Qt.NonModal)
        report_dialog.resize(938, 708)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(report_dialog.sizePolicy().hasHeightForWidth())
        report_dialog.setSizePolicy(sizePolicy)
        report_dialog.setMinimumSize(QSize(938, 708))
        report_dialog.setMaximumSize(QSize(938, 708))
        report_dialog.setSizeGripEnabled(False)
        report_dialog.setModal(True)
        self.verticalLayoutWidget = QWidget(report_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 411, 631))
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
        self.dateEdit.setDateTime(QDateTime(QDate(2022, 12, 26), QTime(18, 0, 0)))

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

        self.verticalLayoutWidget_2 = QWidget(report_dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(460, 10, 454, 640))
        self.previewLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(report_dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 650, 891, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(20, 0, 20, 0)
        self.closeButton = QPushButton(self.horizontalLayoutWidget)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout_5.addWidget(self.closeButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.printButton = QPushButton(self.horizontalLayoutWidget)
        self.printButton.setObjectName(u"printButton")

        self.horizontalLayout_5.addWidget(self.printButton)

        self.saveButton = QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.saveButton)


        self.retranslateUi(report_dialog)

        self.saveButton.setDefault(False)


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
        self.closeButton.setText(QCoreApplication.translate("report_dialog", u"\ub2eb\uae30", None))
        self.printButton.setText(QCoreApplication.translate("report_dialog", u"\uc778\uc1c4", None))
        self.saveButton.setText(QCoreApplication.translate("report_dialog", u"PDF\uc800\uc7a5", None))
    # retranslateUi

