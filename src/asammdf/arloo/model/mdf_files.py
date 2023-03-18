from typing import Sequence

from PySide6.QtCore import QAbstractListModel, QModelIndex

from asammdf import MDF
from asammdf.arloo.arloos import DEFAULT_TIME_ZONE

DATABASE_FILE1 = "./src/asammdf/arloo/280-V00-BRA-030902.dbc"


class MdfFiles:
    """
    object holding multiple mdf files
    """

    def __init__(self, parent=None):
        self.dbc_files = {
            "CAN": [(DATABASE_FILE1, 0)],
        }
        self.dbc_files_arr = [DATABASE_FILE1]

        self.mdf_files = []

    def append_file(self, file_path: str):
        added_file = self.make_mdf_file(file_path)
        self.mdf_files.append(added_file)

    def make_mdf_file(self, file_path):
        added_file = MdfFile(file_path, self.dbc_files)
        return added_file

    def remove_file(self, idx: int):
        self.mdf_files.remove(idx)

    def merge_mdf_files(self, mdf_files):
        filenames = []
        for file in mdf_files:
            filenames.append(file.file_name)
        merged = MDF.concatenate(filenames)
        return merged


class MdfFile:
    def __init__(self, file_path: str, databases):
        self.file_name = file_path
        self._raw_data = MDF(file_path, version='4.10')
        self._parsed = self._raw_data.extract_bus_logging(database_files=databases)
        self.start_time = self._raw_data.start_time.astimezone(DEFAULT_TIME_ZONE)

    def __str__(self) -> str:
        return "{} : {} ".format(self.start_time, self.file_name)
