from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox

from asammdf.arloo.model.preset_model import PresetModel
from asammdf.arloo.ui.preset_widget import Ui_preset_widget
from asammdf.gui.widgets.mdi_area import WithMDIArea


class PresetWidget(WithMDIArea, Ui_preset_widget, QWidget):
    loadClickedSignal = Signal(object, list[str])
    saveClickedSignal = Signal(object, list[str])

    def __init__(self, parent):
        super(Ui_preset_widget, self).__init__()
        self.setupUi(self)
        self._settings = QtCore.QSettings()

        # 단일 저장만 가능한 현 시점에서는 일부 항목은 가린다.
        self.presetNameEdit.setVisible(False)
        self.label.setVisible(False)
        self.itemListView.setModel(PresetModel.instance().list)
        self.cancelButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.save_preset)
        self.loadButton.clicked.connect(self.load_preset)

        # save와 load버튼는 상황에 맞게 열기
        self.saveButton.setVisible(False)
        self.loadButton.setVisible(False)

        # active
        initial_preset = self._settings.value("onePreset", [])
        PresetModel.instance().updateItem(initial_preset)

    def setSelected(self, selected_items):
        PresetModel.instance().updateItem(selected_items)

    def showSave(self):
        self.saveButton.setEnabled(True)
        self.saveButton.setVisible(True)
        self.loadButton.setEnabled(False)
        self.loadButton.setVisible(False)

        self.saveButton.setFocus()
        self.show()

    def showLoad(self):
        # FIXME model을 singleton으로 정의하는 게 맞는 구조인지 생각해보자.
        initial_preset = self._settings.value("onePreset", [])
        PresetModel.instance().updateItem(initial_preset)
        self.saveButton.setEnabled(False)
        self.saveButton.setVisible(False)
        self.loadButton.setEnabled(True)
        self.loadButton.setVisible(True)

        self.loadButton.setFocus()
        self.show()

    def save_preset(self):
        self._settings.setValue("onePreset", PresetModel.instance().list.stringList())
        dialogBox = QMessageBox.information(self, 'save', 'now saving',
                                    QMessageBox.Ok)
        self._settings.sync()
        self.loadClickedSignal.emit(PresetModel.instance().list.stringList())
        self.close()

    def load_preset(self):
        self.loadClickedSignal.emit(PresetModel.instance().list.stringList())
        self.close();
