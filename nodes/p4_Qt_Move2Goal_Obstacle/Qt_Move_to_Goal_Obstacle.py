#!/usr/bin/env python3
# --- Qt_Move_to_Goal_Obstacle-py ------
# Version vom 17.11.2021 by OJ
# ----------------------------

import sys
import rospy
from TurtleBotClassFile_21_11_17 import TurtleBotClass
# Qt -------------------------------
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication,
                             QLabel)
# Obstacle Detection with Lidar ----------------------------
from sensor_msgs.msg import LaserScan


class TurtleUIClass(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(TurtleUIClass, self).__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        startWert = 0
        lcd = QLCDNumber(self)
        lcd.display(-3)
        lcdY = QLCDNumber(self)
        lcdY.display(1)
        lcdDist = QLCDNumber(self)
        lcdDist.display(0.5)

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setMaximum(6)
        self.sld.setMinimum(-6)
        self.sld.setValue(startWert)
        self.sldY = QSlider(Qt.Horizontal, self)
        self.sldY.setMaximum(6)
        self.sldY.setMinimum(-6)
        self.sldY.setValue(startWert)
        self.sldDist = QSlider(Qt.Horizontal, self)
        self.sldDist.setMaximum(10)
        self.sldDist.setMinimum(1)
        self.sldDist.setValue(5)

        pbLess = QPushButton('<')
        pbMore = QPushButton('>')
        pbLessY = QPushButton('<')
        pbMoreY = QPushButton('>')
        pbGo = QPushButton(' Go Turtle ')
        pbStop = QPushButton(' STOPP ')
        self.lblStatus = QLabel('Statuszeile')
        self.lblInfoX = QLabel('X-Goal')
        self.lblInfoY = QLabel('Y-Goal')
        self.lblDist = QLabel('Stopp Distance in 10cm')

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        # 0.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.lblInfoX)
        hbox.addWidget(self.lblInfoY)
        vbox.addLayout(hbox)
        # 1.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(lcd)
        hbox.addWidget(lcdY)
        vbox.addLayout(hbox)
        # 2.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.sld)
        hbox.addWidget(self.sldY)
        vbox.addLayout(hbox)
        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(pbLess)
        hbox.addWidget(pbMore)
        hbox.addWidget(pbLessY)
        hbox.addWidget(pbMoreY)
        vbox.addLayout(hbox)
        # 4.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(pbGo)
        hbox.addWidget(pbStop)
        vbox.addLayout(hbox)
        # 5.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.lblDist)
        hbox.addWidget(self.sldDist)
        hbox.addWidget(lcdDist)
        vbox.addLayout(hbox)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sld.valueChanged.connect(lcd.display)
        self.sldY.valueChanged.connect(lcdY.display)
        self.sldDist.valueChanged.connect(lcdDist.display)

        pbLess.clicked.connect(self.SlotKlick)
        pbMore.clicked.connect(self.SlotKlick)
        pbLessY.clicked.connect(self.SlotKlickY)
        pbMoreY.clicked.connect(self.SlotKlickY)
        pbGo.clicked.connect(self.SlotGo)
        pbStop.clicked.connect(self.timer.stop)
        pbStop.clicked.connect(self.SlotStop)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('RTC - PyQt - TurtleSteering')
        self.show()

    def SlotKlick(self):
        sender = self.sender()
        self.lblStatus.setText(sender.text() + ' was pressed')
        if sender.text() == '<':
            wert = self.sld.value()
            wert = wert-1
            self.sld.setValue(wert)
        else:
            wert = self.sld.value()
            wert = wert+1
            self.sld.setValue(wert)

    def SlotKlickY(self):
        sender = self.sender()
        if sender.text() == '<':
            wert = self.sldY.value()
            wert = wert-1
            self.sldY.setValue(wert)
        else:
            wert = self.sldY.value()
            wert = wert+1
            self.sldY.setValue(wert)

    def SlotGo(self):
        self.Stop = False
        """ Hier geht die Turtle ab """
        turtle1.goal.x = self.sld.value()
        turtle1.goal.y = self.sldY.value()
        self.timer.start(20)

    def SlotStop(self):
        turtle1.stop_robot()

    def detectObstacle(self):
        # get Laser Data
        scan = rospy.wait_for_message('scan', LaserScan)
        # Mittelwert aus den beiden  Werten gerade voraus
        self.detectedDistance = (scan.ranges[0] + scan.ranges[359]) / 2
        rospy.loginfo("Distance to detected Obstacle is %s",
                      round(self.detectedDistance, 2))

    def update(self, STOP_DISTANCE=0.5):  # regelmäßig vom Timer aufgerufen
        self.detectObstacle()
        STOP_DISTANCE = self.sldDist.value()/10 + 0.1  # wegen Roboterlänge
        if self.detectedDistance > STOP_DISTANCE:
            turtle1.move2goal()
        else:
            turtle1.stop_robot()


if __name__ == '__main__':
    try:
        turtle1 = TurtleBotClass()
        # Qt ----------------------
        app = QApplication(sys.argv)
        ui = TurtleUIClass()
        sys.exit(app.exec_())

    except rospy.ROSInterruptException:
        pass
