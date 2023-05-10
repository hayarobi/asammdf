import gc
import operator
import platform
from pathlib import Path

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QAbstractTableModel, Qt, QDateTime
from PySide6.QtWidgets import QWidget, QMessageBox
from natsort import natsorted

from asammdf.arloo.arloos import DEFAULT_Q_TIME_ZONE
from asammdf.arloo.model.mdf_files import MdfFiles
from asammdf.arloo.ui.multifile_widget import Ui_MultiFileWidget
from asammdf.gui.widgets.mdi_area import WithMDIArea, MdiAreaWidget


class MdfTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent=None):
        return len(self.mylist)

    def columnCount(self, parent=None):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.layoutAboutToBeChanged.emit()
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.layoutChanged.emit()

    def appendRow(self, item):
        self.mylist.append(item)
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(1))
        self.rowsInserted.emit(None, 0, len(self.mylist) - 1)

    def removeRow(self, row):
        del self.mylist[row]
        self.rowsRemoved.emit(None, row, row)

    def get_mdf_list(self):
        result_list = []
        for tup in self.mylist:
            result_list.append(tup[4])
        return result_list

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
        # 테이블 뷰 초기화
        header = ['파일명', '시작 시각', '종료 시각', '평균 샘플 갯수']
        self._model = MdfTableModel(self, [], header)
        self.mdfListView.setColumnWidth(1, 512)
        self.mdfListView.setColumnWidth(2, 192)
        self.mdfListView.setColumnWidth(3, 192)
        self.mdfListView.setModel(self._model)
        self.mdfListView.updateGeometry()
        self.mergeSaveButton.clicked.connect(self.merge_convert)
        self.batchConvertButton.clicked.connect(self.batch_convert)

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

        item_mdf = (mdf_file.file_name, self.to_qdatetime(mdf_file.start_time),
                    self.to_qdatetime(mdf_file.end_time), mdf_file.sample_count, mdf_file)
        self._model.appendRow(item_mdf)

    def remove_file(self):
        for row in self.mdfListView.selectedIndexes():
            self._model.removeRow(row.row())

    def merge_convert(self):
        mdfs = []
        file_count = self._model.rowCount(None)
        if file_count == 0:
            QMessageBox.information(self, '병합 실패', '입력 파일을 먼저 추가해 주세요', QMessageBox.Ok)
            return
        mdfs = self._model.get_mdf_list()
        # for row in range(0, file_count):
        #     item = self._model.item(row)
        #     mdfs.append(item.data())
        merged = self._mdf_util.merge_mdf_files(mdfs)
        self.extract_signal.emit(ExtractEvent(merged, self._mdf_util.dbc_files_arr))

    def batch_convert(self):
        """
        입력 파일을 개별적으로 저장하기
        :return:
        """
        # 구현하자
        mdfs = []
        file_count = self._model.rowCount()
        if file_count == 0:
            QMessageBox.information(self, 'no files', '변환할 파일이 없습니다.', QMessageBox.Ok)
            return

        # TODO 디렉토리 선택 대화창 띄우기

        # TODO 파일을 순회하며 저장하기.
        QMessageBox.information(self, 'Not Implemented', 'Not Implemented yet.', QMessageBox.Ok)

    def to_qdatetime(self, py_dt):
        return QDateTime.fromSecsSinceEpoch(py_dt.timestamp(), DEFAULT_Q_TIME_ZONE)


class ExtractEvent:
    def __init__(self, mdf, database_arr) -> None:
        super().__init__()
        self.mdf = mdf
        self.database = database_arr
