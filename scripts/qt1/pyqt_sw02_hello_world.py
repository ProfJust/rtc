#!/usr/bin/python3
import sys
# Hello World mit den Aenderungen fuer Qt5

from PyQt5 import QtWidgets


def window():
    # App
    app = QtWidgets.QApplication(sys.argv)

    # Fenster instanziierem
    window = QtWidgets.QWidget()
    window.setGeometry(100, 100, 200, 50)
    window.setWindowTitle("PyQt - Version Qt5")

    # Label auf Window setzen
    label = QtWidgets.QLabel(window)
    label.setText("Hello World!")
    label.move(50, 20)

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
