#!/usr/bin/python3
# pyqt_sw03_hello_world_class.py
# Hello World im OO-Style
# https://pythonprogramminglanguage.com/pyqt5-hello-world/
# ------------------------------------------------------------------
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    # Konstruktor
    def __init__(self):
        # Window Init
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(240, 80))
        self.setWindowTitle("WHS - Campus Bocholt")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Layout
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        # Label
        title = QLabel("Hello World from PyQt5", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()  # Objekt instanziieren
    mainWin.show()
    sys.exit(app.exec_())
