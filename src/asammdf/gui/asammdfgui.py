# -*- coding: utf-8 -*-
import argparse
import os
import sys
from time import sleep

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen

os.environ["QT_API"] = "pyside6"
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

import pyqtgraph
from PySide6 import QtGui, QtWidgets

from asammdf.gui.utils import excepthook
from asammdf.gui.widgets.main import MainWindow
from asammdf.gui.widgets.plot import monkey_patch_pyqtgraph
from asammdf.gui.arloo import arresource_rc

sys.excepthook = excepthook


def _cmd_line_parser():
    """"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--measurements", nargs="*", help="list of measurement files")
    return parser


def main(measurements=None):
    monkey_patch_pyqtgraph()
    parser = _cmd_line_parser()
    args = parser.parse_args(sys.argv[1:])
    app = pyqtgraph.mkQApp()
    app.setOrganizationName("py-asammdf")
    app.setOrganizationDomain("py-asammdf")
    app.setApplicationName("py-asammdf")

    pixmap = QPixmap(":/splash_image.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    sleep(1.0)
    main = MainWindow(args.measurements)
    # TODO 일단 이 기능은 막아둠. 나중에 설정 추가하면 다시 활성화
    #main.showMaximized()
    splash.finish(main)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    app.exec()


if __name__ == "__main__":
    main()
