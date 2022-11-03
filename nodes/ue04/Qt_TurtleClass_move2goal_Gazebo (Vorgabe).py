#!/usr/bin/env python3
# --- TurtleClass_move2Goal_Gazebo.py ------
# Version vom 31.10.2022 by OJ
# ----------------------------
# from
# --- P3_V4_TurtleClass_move2goal.py ------
# Version vom 22.10.2019 by OJ
# Basiert auf der Loesung aus dem Turtlesim Tutorial
# http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal
# usage
# $1 roscore
# $2 roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch 
# start this file here
# $3 rosrun rtc Qt_TurtleClass_move2goal_Gazebo.py
#
import sys
import rospy
from TurtleBotClassFile import TurtleBotClass
# Falls der Import nicht klappt, checke PYTHONPATH
# in der .bashrc (Skript Kapitel 11.7)
# export PYTHONPATH=$PYTHONPATH:~/catkin_ws/src/rtc/rtc_dist-packages
# danach catkin_make nicht vergessen

# Qt -------------------------------
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication,
                             QLabel)


class TurtleUIClass(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(TurtleUIClass, self).__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        LCDstartWert = 0
        self.lcdX = QLCDNumber(self)
        self.lcdX.display(LCDstartWert)
        self.lcdY = QLCDNumber(self)
        self.lcdY.display(LCDstartWert)
        
        self.sldX = QSlider(Qt.Horizontal, self)
        self.sldX.setMaximum(6)
        self.sldX.setMinimum(-6)
        self.sldX.setValue(LCDstartWert)

        self.sldY = QSlider(Qt.Horizontal, self)
        self.sldY.setMaximum(6)
        self.sldY.setMinimum(-6)
        self.sldY.setValue(LCDstartWert)
        
        self.pbLessX = QPushButton('<')
        self.pbMoreX = QPushButton('>')
        self.pbLessY = QPushButton('<')
        self.pbMoreY = QPushButton('>')
        self.pbGo = QPushButton(' Go Turtle ')
        self.pbStop = QPushButton(' Stop ')

        self.lblInfoX = QLabel('X-Goal (world coordinates)')
        self.lblInfoY = QLabel('Y-Goal (world coordinates)')
        self.lblStatus = QLabel('Status - Ausgabe')

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        #  0.Reihe - Label
        hbox = QHBoxLayout()
        hbox.addWidget(self.lblInfoX)
        hbox.addWidget(self.lblInfoY)
        vbox.addLayout(hbox)
        # 1.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.lcdX)
        hbox.addWidget(self.lcdY)
        vbox.addLayout(hbox)
        # 2.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.sldX)
        hbox.addWidget(self.sldY)
        vbox.addLayout(hbox)

        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbLessX)
        hbox.addWidget(self.pbMoreX)
        hbox.addWidget(self.pbLessY)
        hbox.addWidget(self.pbMoreY)
        vbox.addLayout(hbox)

        # 4.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbGo)
        vbox.addLayout(hbox)

        # 5.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbStop)
        vbox.addLayout(hbox)

        # 6.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.lblStatus)
        vbox.addLayout(hbox)

        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('RTC - PyQt - TurtleSteering')
        self.show()

        # Signal und Slot verbinden
        self.sldX.valueChanged.connect(self.lcdX.display)
        self.sldY.valueChanged.connect(self.lcdY.display)

        self.pbLessX.clicked.connect(self.SlotKlickX)
        self.pbMoreX.clicked.connect(self.SlotKlickX)
        self.pbLessY.clicked.connect(self.SlotKlickY)
        self.pbMoreY.clicked.connect(self.SlotKlickY)
        self.pbGo.clicked.connect(self.SlotGo)
        self.pbStop.clicked.connect(self.SlotStop)

    def SlotKlickX(self):
        sender = self.sender()
        self.lblStatus.setText(' X ' + sender.text() + ' was pressed')
        if sender.text() == '<':
            wert = self.sldX.value()
            wert = wert-1
            self.sldX.setValue(wert)
        else:
            wert = self.sldX.value()
            wert = wert+1
            self.sldX.setValue(wert)
    
    def SlotKlickY(self):
        sender = self.sender()
        self.lblStatus.setText(' Y ' + sender.text() + ' was pressed')
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
        turtle1.goal.x = self.sldX.value()
        turtle1.goal.y = self.sldY.value()
        self.timer.start(20)  # 20 msec

    def SlotStop(self):
        self.lblStatus.setText(' Stop Button klicked ')
        self.timer.stop()
        turtle1.stop_robot()

    def update(self):
        turtle1.move2goal()


if __name__ == '__main__':
    try:
        turtle1 = TurtleBotClass()
        # Konsole ---------------
        # turtle1.getGoalFromUser()
        # turtle1.start_info()
        # turtle1.move2goal()

        # Qt ----------------------
        app = QApplication(sys.argv)
        ui = TurtleUIClass()
        sys.exit(app.exec_())

    except rospy.ROSInterruptException:
        pass
