#!/usr/bin/env python3
# --- Qt_Move_to_Goal_Obstacle.py ------
# Version vom 28.10.2021 by OJ
# -------------------------------------------------
# TurtleBot fährt zum Ziel und stoppt bei Hindernis
# rtc P4
# -------------------------------------------------
import sys
import rospy
import math
from TurtleBotClassFile import TurtleBotClass
# Qt -------------------------------
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication,
                             QLabel)
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
        lcd.display(startWert)
        lcdY = QLCDNumber(self)
        lcdY.display(startWert)

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setMaximum(6)
        self.sld.setMinimum(-6)
        self.sld.setValue(startWert)
        self.sldY = QSlider(Qt.Horizontal, self)
        self.sldY.setMaximum(6)
        self.sldY.setMinimum(-6)
        self.sldY.setValue(startWert)

        pbLess = QPushButton('<')
        pbMore = QPushButton('>')
        pbLessY = QPushButton('<')
        pbMoreY = QPushButton('>')
        pbGo = QPushButton(' Go Turtle ')
        pbStop = QPushButton(' STOPP ')
        self.lblStatus = QLabel('Statuszeile')
        self.lblInfoX = QLabel('X-Goal')
        self.lblInfoY = QLabel('Y-Goal')

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
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sld.valueChanged.connect(lcd.display)
        self.sldY.valueChanged.connect(lcdY.display)

        pbLess.clicked.connect(self.SlotKlick)
        pbMore.clicked.connect(self.SlotKlick)
        pbLessY.clicked.connect(self.SlotKlickY)
        pbMoreY.clicked.connect(self.SlotKlickY)
        pbGo.clicked.connect(self.SlotGo)
        pbStop.clicked.connect(self.timer.stop)
        pbStop.clicked.connect(self.SlotStop)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
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

    def SlotGo(self, timerIntervall=20):
        self.Stop = False
        """ Hier geht die Turtle ab """
        turtle1.goal.x = self.sld.value()
        turtle1.goal.y = self.sldY.value()
        self.timer.start(timerIntervall)  # in ms

    def SlotStop(self):
        turtle1.stop_robot()

    def get_scan(self):
        scan = rospy.wait_for_message('scan', LaserScan)
        scan_filtered = []
        numbOfScans = len(scan.ranges)  # 
        # This number of samples is defined in
        # turtlebot3_<model>.gazebo.xacro file,
        # the default is 360.
        samples_view = 1            # 1 <= samples_view <= samples

        if samples_view > numbOfScans:
            samples_view = numbOfScans

        if samples_view == 1:
            scan_filtered.append(scan.ranges[0])

        else:
            left_lidar_samples_ranges = -(samples_view//2 + samples_view % 2)
            right_lidar_samples_ranges = samples_view//2
            left_lidar_samples = scan.ranges[left_lidar_samples_ranges:]
            right_lidar_samples = scan.ranges[:right_lidar_samples_ranges]
            scan_filtered.extend(left_lidar_samples + right_lidar_samples)

        for i in range(samples_view):
            if scan_filtered[i] == float('Inf'):
                scan_filtered[i] = 3.5
            elif math.isnan(scan_filtered[i]):
                scan_filtered[i] = 0

        return scan_filtered

    def obstacle_detected(self):
        STOP_DISTANCE = 0.3
        LIDAR_ERROR = 0.05
        SAFE_STOP_DISTANCE = STOP_DISTANCE + LIDAR_ERROR

        lidar_distances = self.get_scan()
        min_distance = min(lidar_distances)
        if min_distance < SAFE_STOP_DISTANCE:
            rospy.loginfo(" Obstacle detected ")
            return True
        else:
            rospy.loginfo(" No Obstacle detected ")
            return False

    def update(self):  # Aufruf per Timer alle 20ms
        self.get_scan()
        if not self.obstacle_detected():
            turtle1.move2goal()
        else:
            turtle1.robot_wait()


if __name__ == '__main__':
    try:
        turtle1 = TurtleBotClass()
        # Qt ----------------------
        app = QApplication(sys.argv)
        ui = TurtleUIClass()
        sys.exit(app.exec_())

    except rospy.ROSInterruptException:
        pass
