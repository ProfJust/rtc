#!/usr/bin/python3
# -------------------------------------------------------------------------
# pyqt_sw05_slider.py
# Beispiel fuer Slider
# https://pythonprogramminglanguage.com/pyqt5-sliders/
# -------------------------------------------------------------------------
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox,
                             QRadioButton, QVBoxLayout,
                             QWidget, QSlider)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Grid - Layout aus 4 gleichen Gruppen
        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup(), 1, 0)
        grid.addWidget(self.createExampleGroup(), 0, 1)
        grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Sliders")
        self.resize(400, 300)

    def createExampleGroup(self):
        groupBox = QGroupBox("Slider Example")

        radio1 = QRadioButton("&Radio horizontal slider")
        radio1.setChecked(True)

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
