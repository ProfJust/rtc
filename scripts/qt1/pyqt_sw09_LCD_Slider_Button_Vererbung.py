#!/usr/bin/python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication, QLabel)


class myButton(QPushButton):
    # Konstruktor
    # benötigt Zugriff auf str '<' oder '>', Label und Slider
    def __init__(self, str, lbl, slider):
        super(myButton, self).__init__()
        self.setText(str)
        self.label = lbl
        self.sld = slider
        # > "this" bzw. self muss in Python immer explixit angegeben
        # > werden, anders als z.B. bei C++.
        #  Das ist einer der Python-Grundsätze:
        #  "Explicit is better than implicit",

    # zusaetzliche Fkt von myButton zu QPushButton
    def SlotKlick(self):
        sender = self.sender()
        wert = self.sld.value()
        if sender.text() == '<':
            self.label.setText('less')
            wert = wert-1
        else:
            self.label.setText('more')
            wert = wert+1
        self.sld.setValue(wert)


class Example(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        self.lblStatus = QLabel('Statuszeile')
        self.pbLess = myButton('<', self.lblStatus, self.sld)
        self.pbMore = myButton('>', self.lblStatus, self.sld)

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        # 1.Reihe
        vbox.addWidget(lcd)
        # 2.Reihe
        vbox.addWidget(self.sld)
        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbLess)
        hbox.addWidget(self.pbMore)
        vbox.addLayout(hbox)
        # 4.Reihe
        vbox.addWidget(self.lblStatus)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sld.valueChanged.connect(lcd.display)
        self.sld.valueChanged.connect(lcd.display)

        self.pbLess.clicked.connect(self.pbLess.SlotKlick)
        self.pbMore.clicked.connect(self.pbMore.SlotKlick)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
