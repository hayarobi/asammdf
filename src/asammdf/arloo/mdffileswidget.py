import gc
from pathlib import Path
import platform

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSettings
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QMessageBox
from natsort import natsorted

from asammdf import MDF
from asammdf.arloo.arloofile import ArlooFileWidget
from asammdf.arloo.model.mdf_files import MdfFiles
from asammdf.arloo.summay import time_to_str
from asammdf.arloo.ui.multifile_widget import Ui_MultiFileWidget
from asammdf.gui.widgets.mdi_area import WithMDIArea, MdiAreaWidget


class MDFFilesWidget(WithMDIArea, Ui_MultiFileWidget, QWidget):
    add_file_signal = QtCore.Signal(str)
    remove_file_signal = QtCore.Signal(int)
    extract_signal = QtCore.Signal(object)

    def __init__(
            self,
            *args,
            **kwargs,
    ):
        super(Ui_MultiFileWidget, self).__init__(*args, **kwargs)
        WithMDIArea.__init__(self)
        self._settings = QtCore.QSettings()
        self.setupUi(self)

        self._mdf_util = MdfFiles()
        self._model = QStandardItemModel()
        self.mdfListView.setModel(self._model)
        self.extractButton.clicked.connect(self.extract)
        self.addButton.clicked.connect(self.add_file)
        self.removeButton.clicked.connect(self.remove_file)

        self.mdi_area = MdiAreaWidget()
        self.mdi_area.setVisible(False)

    def update_all_channel_trees(self):
        # do nothing
        pass

    def add_file(self):
        self.open_file(None)

    def open_file(self, event):
        system = platform.system().lower()
        if system == "linux":
            # see issue #567
            # file extension is case sensitive on linux
            file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(
                self,
                "Select measurement file",
                self._settings.value("last_opened_path", "", str),
                "CSV (*.csv);;MDF v3 (*.dat *.mdf);;MDF v4(*.mf4 *.mf4z);;DL3/ERG files (*.dl3 *.erg);;All files (*.csv *.dat *.mdf *.mf4 *.mf4z *.dl3 *.erg)",
                "All files (*.csv *.dat *.mdf *.mf4 *.mf4z *.dl3 *.erg)",
                options=QtWidgets.QFileDialog.DontUseNativeDialog,
            )
        else:
            file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(
                self,
                "Select measurement file",
                self._settings.value("last_opened_path", "", str),
                "CSV (*.csv);;MDF v3 (*.dat *.mdf);;MDF v4(*.mf4 *.mf4z);;DL3/ERG files (*.dl3 *.erg);;All files (*.csv *.dat *.mdf *.mf4 *.mf4z *.dl3 *.erg)",
                "All files (*.csv *.dat *.mdf *.mf4 *.mf4z *.dl3 *.erg)",
            )

        if file_names:
            self._settings.setValue("last_opened_path", file_names[0])
            gc.collect()

        for file_name in natsorted(file_names):
            self.append_file(file_name)

    def append_file(self, file_name):
        file_path = Path(file_name)
        mdf_file = self._mdf_util.make_mdf_file(file_name)
        # items = []
        # item_start_time = QStandardItem(time_to_str(mdf_file.start_time))
        # item_start_time.setData(mdf_file.start_time)
        # item_size = QStandardItem(str(3))
        item_mdf = QStandardItem(mdf_file.__str__())
        item_mdf.setData(mdf_file)
        # items.append(item_start_time)
        # items.append(item_size)
        # items.append(item_mdf)
        self._model.appendRow(item_mdf)

    def remove_file(self):
        for row in self.mdfListView.selectedIndexes():
            self._model.removeRow(row.row())

    def extract(self):
        mdfs = []
        file_count = self._model.rowCount()
        if file_count == 0:
            QMessageBox.information(self, 'no files', 'add files first', QMessageBox.Ok)
            return

        for row in range(0, file_count):
            item = self._model.item(row)
            mdfs.append(item.data())
        merged = self._mdf_util.merge_mdf_files(mdfs)
        self.extract_signal.emit(ExtractEvent(merged,self._mdf_util.dbc_files_arr))

class ExtractEvent:
    def __init__(self, mdf, database_arr) -> None:
        super().__init__()
        self.mdf = mdf
        self.database = database_arr