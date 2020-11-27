#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
# --------------------------------------------------------------------------------------
# pyqt_sw04_push_button.py
# Beispiel fuer Push_Button mit Click-Event
# https://pythonprogramminglanguage.com/pyqt5-button/
# -------------------------------------------------------------------------------------
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("PyQt button example"
                            "- pythonprogramminglanguage.com")

        # Push Button
        pybutton = QPushButton('Click me', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100, 32)
        pybutton.move(50, 50)

    def clickMethod(self):
        # Callback Funktion für clicked
        print('Clicked Pyqt button.')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
