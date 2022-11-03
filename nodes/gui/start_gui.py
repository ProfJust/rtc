#!/usr/bin/env python3
# -- start_gui.py --
# GUI to control all the Launch Files etc. in the RTC22 course
# edited WHS, OJ , 03.11.2022 #

from PyQt5.QtWidgets import (QWidget,QApplication,  QPushButton)
from PyQt5.QtCore import Qt
import sys
import os


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # --- roscore ---
        self.myPb_roscore = QPushButton(self)
        self.myPb_roscore.setText('Starte ROS-Master')
        self.myPb_roscore.setGeometry(10, 10, 300, 40)  # x,y,w,h
        self.myPb_roscore.clicked.connect(self.slot_roscore)

        # --- roslaunch ---
        self.myPb_gazebo_ur5 = QPushButton(self)
        self.myPb_gazebo_ur5.setText('Starte TB3 in Empty-Gazebo_World !')
        self.myPb_gazebo_ur5.setGeometry(10, 50, 300, 40)  # x,y,w,h
        self.myPb_gazebo_ur5.clicked.connect(self.slot_empty_world)

        self.myPb_depth = QPushButton(self)
        self.myPb_depth.setText('Starte TB3 in Gazebo_House !')
        self.myPb_depth.setGeometry(10, 90, 300, 40)  # x,y,w,h
        self.myPb_depth.clicked.connect(self.slot_gazebo_house)

        # --- Start Action Server Script ---
        self.myPb_pick_place = QPushButton(self)
        self.myPb_pick_place.setText('Action Server/Client Empty-World ')
        self.myPb_pick_place.setGeometry(10, 130, 300, 40)  # x,y,w,h
        self.myPb_pick_place.clicked.connect(self.slot_action_empty)

        self.myPb_pick_place_dc = QPushButton(self)
        self.myPb_pick_place_dc.setText('Action Server/Client Gazebo-House')
        self.myPb_pick_place_dc.setGeometry(10, 170, 300, 40)  # x,y,w,h
        self.myPb_pick_place_dc.clicked.connect(self.slot_action_house)

        """# --- find_object_2D ---
        self.myPb_find_object_2D = QPushButton(self)
        self.myPb_find_object_2D.setText('find_object_2D - gazebo')
        self.myPb_find_object_2D.setGeometry(10, 210, 300, 40)  # x,y,w,h
        self.myPb_find_object_2D.clicked.connect(self.slot_find_object_2D)

        # --- find_object_2D und Astra---
        self.myPb_astra = QPushButton(self)
        self.myPb_astra.setText(' Astra Orbbec und find_object_2D - real')
        self.myPb_astra.setGeometry(10, 250, 300, 40)  # x,y,w,h
        self.myPb_astra.clicked.connect(self.slot_astra_cam)
        """

        # --- Window konfigurieren und starten
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('RTC22 - Starthilfe ')
        self.show()

    # --- Die  Slot-Methoden ---
    def slot_roscore(self):
        os.system('gnome-terminal --tab -- /bin/bash -c "roscore; exec bash"')

    def slot_empty_world(self):
        os.system('gnome-terminal --tab -- /bin/bash -c \
                  "roslaunch rtc turtlebot3_gazebo turtlebot3_empty_world.launch; \
                  exec bash"')

    def slot_gazebo_house(self):
        os.system('gnome-terminal --tab -- /bin/bash -c \
                  "roslaunch rtc turtlebot3_gazebo turtlebot3_house.launch;\
                  exec bash"')

    def slot_action_empty(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "roslaunch rtc\
                  turtlebot3_action_server_client_path_gazebo_empty.launch;\
                  exec bash"')

    def slot_action_house(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "roslaunch rtc\
                  turtlebot3_action_server_client_path_gazebo_house.launch;\
                  exec bash"')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
