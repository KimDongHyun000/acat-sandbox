# -*- coding: utf-8 -*-
import argparse
import os
import sys

# import pyqtgraph
import random

from PySide6 import QtWidgets, QtCore
import excepthook


os.environ["QT_API"] = "pyside6"
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

sys.excepthook = excepthook


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def _cmd_line_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--measurements", nargs="*", help="list of measurement files")
    return parser


def main(measurements=None):
    parser = _cmd_line_parser()
    args = parser.parse_args(sys.argv[1:])
    print(args)
    """
    app = pyqtgraph.mkQApp()
    app.setOrganizationName("cp6")
    app.setOrganizationDomain("cp6-acat-investigator")
    app.setApplicationName("acat")
    # main = MainWindow(args.measurements)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    app.exec()
    """


if __name__ == "__main__":
    # main()
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
