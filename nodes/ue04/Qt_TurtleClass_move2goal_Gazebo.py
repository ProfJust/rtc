#!/usr/bin/env python3
# --- TurtleClass_move2Goal_Gazebo.py ------
# Version vom 23.11.2020 by OJ
# ----------------------------
# from
# --- P3_V4_TurtleClass_move2goal.py ------
# Version vom 22.10.2019 by OJ
# Basiert auf der Loesung aus dem Turtlesim Tutorial
# http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal
#
import sys
import rospy
from TurtleBotClassFile import TurtleBotClass
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
    
    def SlotGo(self):
        self.Stop = False
        """ Hier geht die Turtle ab """
        turtle1.goal.x = self.sld.value()
        turtle1.goal.y = self.sldY.value()
        self.timer.start(20)

    def SlotStop(self):
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
