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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_preset_widget(object):
    def setupUi(self, preset_widget):
        if not preset_widget.objectName():
            preset_widget.setObjectName(u"preset_widget")
        preset_widget.resize(1150, 724)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(preset_widget.sizePolicy().hasHeightForWidth())
        preset_widget.setSizePolicy(sizePolicy)
        preset_widget.setMinimumSize(QSize(1150, 724))
        preset_widget.setMaximumSize(QSize(1150, 724))
        preset_widget.setFocusPolicy(Qt.NoFocus)
        self.cancelButton = QPushButton(preset_widget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(840, 680, 141, 32))
        self.horizontalLayoutWidget = QWidget(preset_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1131, 661))
        self.gridLayout = QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupLayout = QVBoxLayout()
        self.groupLayout.setObjectName(u"groupLayout")
        self.groupLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(350, 16777215))

        self.groupLayout.addWidget(self.label)

        self.groupListView = QListView(self.horizontalLayoutWidget)
        self.groupListView.setObjectName(u"groupListView")
        self.groupListView.setMinimumSize(QSize(350, 0))
        self.groupListView.setMaximumSize(QSize(350, 16777215))

        self.groupLayout.addWidget(self.groupListView)


        self.gridLayout.addLayout(self.groupLayout, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.channelsLayout = QVBoxLayout()
        self.channelsLayout.setObjectName(u"channelsLayout")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.channelsLayout.addWidget(self.label_2)

        self.channelsListView = QListView(self.horizontalLayoutWidget)
        self.channelsListView.setObjectName(u"channelsListView")

        self.channelsLayout.addWidget(self.channelsListView)


        self.gridLayout.addLayout(self.channelsLayout, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.renameButton = QPushButton(preset_widget)
        self.renameButton.setObjectName(u"renameButton")
        self.renameButton.setGeometry(QRect(10, 680, 121, 32))
        self.deleteButton = QPushButton(preset_widget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(150, 680, 121, 32))
        self.loadButton = QPushButton(preset_widget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(1000, 680, 141, 32))
        self.loadButton.setAutoDefault(True)

        self.retranslateUi(preset_widget)

        self.loadButton.setDefault(True)


        QMetaObject.connectSlotsByName(preset_widget)
    # setupUi

    def retranslateUi(self, preset_widget):
        preset_widget.setWindowTitle(QCoreApplication.translate("preset_widget", u"\ud504\ub9ac\uc14b \ubaa9\ub85d", None))
        self.cancelButton.setText(QCoreApplication.translate("preset_widget", u"\ub2eb\uae30", None))
        self.label.setText(QCoreApplication.translate("preset_widget", u"\ud504\ub9ac\uc14b", None))
        self.label_2.setText(QCoreApplication.translate("preset_widget", u"\ucc44\ub110 \ubaa9\ub85d", None))
        self.renameButton.setText(QCoreApplication.translate("preset_widget", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.deleteButton.setText(QCoreApplication.translate("preset_widget", u"\uc0ad\uc81c", None))
        self.loadButton.setText(QCoreApplication.translate("preset_widget", u"\ud504\ub9ac\uc14b \ub85c\ub4dc", None))
    # retranslateUi

