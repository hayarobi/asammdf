from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QMessageBox

from asammdf.arloo.model.preset_model import PresetModel, PRESET_SETTING_V2
from asammdf.arloo.ui.preset_widget import Ui_preset_widget
from asammdf.gui.widgets.mdi_area import WithMDIArea

ROLE_CHANNEL_LIST = 11


class PresetWidget(WithMDIArea, Ui_preset_widget, QWidget):
    loadClickedSignal = Signal(object, list[str])
    saveClickedSignal = Signal(object, list[str])

    def __init__(self, parent):
        super(Ui_preset_widget, self).__init__()
        self.setupUi(self)
        self._settings = QtCore.QSettings()

        # 단일 저장만 가능한 현 시점에서는 일부 항목은 가린다.
        self.label.setVisible(False)
        # self.channelsListView.setModel(PresetModel.instance().list)
        self.cancelButton.clicked.connect(self.close)
        self.renameButton.clicked.connect(self.rename_preset)
        self.deleteButton.clicked.connect(self.delete_preset)
        self.loadButton.clicked.connect(self.load_preset)

        # 그룹 선택이 변경될 때
        self.groupListView.clicked.connect(self._update_itemsView)
        self.groupListView.doubleClicked.connect(self.load_preset)

        # active
        self._data_model = PresetModel.instance()
        self.presets_model = QStandardItemModel()
        self.refresh_preset_model()

    def show_manage_window(self):
        # 목록 초기화
        self.groupListView.reset()
        self.refresh_preset_model()
        self.groupListView.setModel(self.presets_model)
        self.groupListView.selectionModel().selectionChanged.connect(self._update_itemsView)

        self.loadButton.setFocus()
        self.show()

    def refresh_preset_model(self):
        presets_model = self.presets_model
        presets_model.clear()
        key_list = sorted(self._data_model.preset_map.keys())
        for key in key_list:
            val = self._data_model.get_channel_list(key)
            item_preset = QStandardItem(key)
            item_preset.setData(val, role=ROLE_CHANNEL_LIST)
            presets_model.appendRow(item_preset)
        return presets_model

    def has_preset(self, preset_name):
        return self._data_model.find_preset(preset_name)

    def rename_preset(self):
        selected_indexes = self._get_selected_preset()
        if not selected_indexes:
            return

        prev_name = selected_indexes.text()
        preset_name, ok = QtWidgets.QInputDialog.getText(
            self,
            "프리셋 이름 변경",
            "변경할 이름",
            # echo=None,
            # text=prev_name,
            # flags=QtCore.Qt.FramelessWindowHint,
            # inputMethodHints=QtCore.Qt.ImhNone
        )
        if not ok:
            return

        preset_name = preset_name.strip()
        if not preset_name:
            QMessageBox.warning(None, "ERROR", "프리셋 이름을 써 주세요")
        else:
            # 이름 중복 검사
            if self.has_preset(preset_name):
                QMessageBox.warning(None, "ERROR", "같은 이름이 이미 있습니다")
                return
            else:
                selected_indexes.setText(preset_name)
                self._data_model.rename_preset(prev_name, preset_name)
                self.refresh_preset_model()

    def add_preset(self, preset_name, str_list):
        self._data_model.set_preset_channels(preset_name, str_list)

    def load_preset(self):
        selected_item = self._get_selected_preset()
        if not selected_item:
            return
        preset_name = selected_item.text()

        str_list = self._data_model.get_channel_list(preset_name).stringList()
        self.loadClickedSignal.emit(str_list)
        self.close()

    def delete_preset(self):
        selected_indexes = self.groupListView.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = self.presets_model.itemFromIndex(
                self.presets_model.index(index.row(), 0)
            )
            m = self.groupListView.selectionModel()
            self._data_model.delete_preset(item.text())
            self.presets_model.removeRow(index.row())
            del m
            self._update_itemsView()
            return

    def _update_itemsView(self, model_index=None):
        selected_preset = self._get_selected_preset()
        if selected_preset is None:
            self.channelsListView.setModel(None)
            self.channelsListView.reset()
            return
        # 선택된 프리셋으로 채널 목록 변경
        preset_channels = selected_preset.data(ROLE_CHANNEL_LIST)
        self.channelsListView.setModel(preset_channels)

    def _get_selected_preset(self):
        """
        현재 선택된 프리셋 아이템을 반환한다.
        :return: QStandardItem 객체. 이 객체가 채널리스트를 data로 들고 있다.
        """
        selected_indexes = self.groupListView.selectedIndexes()
        if selected_indexes:
            index = selected_indexes[0]
            item = self.presets_model.itemFromIndex(
                self.presets_model.index(index.row(), 0)
            )
            return item
        return None
