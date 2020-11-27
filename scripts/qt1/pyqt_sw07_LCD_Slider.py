# ---------------------------------------------------------------------
# pyqt_sw07_LCD_Slider.py
# Beispiel fuer Signal Slot Konzept
# ---------------------------------------------------------------------

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLCDNumber, QApplication, QPushButton)
from PyQt5.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # --- Slider erstellen -----
        self.mySlider = QSlider(Qt.Horizontal, self)
        self.mySlider.setFocusPolicy(Qt.NoFocus)
        self.mySlider.setGeometry(30, 40, 180, 30)  # x,y,w,h
        self.mySlider.setValue(20)

        # --- LCD konstruieren -----
        self.myLcd = QLCDNumber(2, self)
        self.myLcd.setGeometry(60, 100, 80, 50)  # x,y,w,h
        self.myLcd.display(20)

        # Verbinden des Signals valueChanged
        # mit der Slot-Funktion myLcd.display
        self.mySlider.valueChanged[int].connect(self.myLcd.display)

        # --- zwei PushButtons
        myPBmore = QPushButton(self)
        myPBmore.setText('>')
        myPBmore.setGeometry(0, 0, 40, 40)   # x,y,w,h
        myPBmore.clicked.connect(self.plus)

        self.myPBless = QPushButton(self)
        self.myPBless.setText('<')
        self.myPBless.setGeometry(180, 0, 40, 40)  # x,y,w,h
        self.myPBless.clicked.connect(self.minus)

        # --- Window konfigurieren
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Robotik Bocholt - Slider LCD')
        self.show()

    # --- Die beiden Slot-Methoden
    def plus(self):
        wert = self.mySlider.value()  # Slider Wert holen
        wert = wert+1
        self.mySlider.setValue(wert)  # Slider Wert setzen

    def minus(self):
        wert = self.mySlider.value()
        wert = wert-1
        self.mySlider.setValue(wert)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())

