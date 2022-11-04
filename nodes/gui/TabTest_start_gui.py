#!/usr/bin/env python3
# -- TabTess_start_gui.py --
# GUI to control all the Launch Files etc. in the RTC22 course
# edited WHS, OJ , 04.11.2022
# now with Tabs and more options


from PyQt5.QtWidgets import (QWidget,
                             QApplication,
                             QPushButton,
                             QGridLayout,
                             QHBoxLayout,
                             QVBoxLayout,
                             QLabel,
                             QTabWidget,
                             QFormLayout,
                             QLineEdit,
                             QCheckBox,
                             QRadioButton)
from PyQt5.QtCore import *
import sys
import os


class MainWindow(QTabWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # https://www.tutorialspoint.com/pyqt/pyqt_qtabwidget.htm

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        # --- Window konfigurieren und starten
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('RTC22 - Starthilfe ')
        # self.show()

    def tab1UI(self):  # --- Simulation ----
        layout = QVBoxLayout()
        # --- roscore ---
        self.myPb_roscore = QPushButton(self)
        self.myPb_roscore.setText(' ROS-Master ')
        # self.myPb_roscore.setGeometry(10, 10, 300, 40)  # x,y,w,h
        self.myPb_roscore.clicked.connect(self.slot_roscore)
        layout.addWidget(self.myPb_roscore)

        # --- Empty-Gazebo  ---
        self.myPb_gzb_empty = QPushButton(self)
        self.myPb_gzb_empty.setText(' TB3 in Empty-Gazebo_World !')
        # self.myPb_gzb_empty.setGeometry(10, 50, 300, 40)  # x,y,w,h
        self.myPb_gzb_empty.clicked.connect(self.slot_empty_world)
        layout.addWidget(self.myPb_gzb_empty)

        # --- Gazebo-House ---
        self.myPb_gzb_house = QPushButton(self)
        self.myPb_gzb_house.setText(' TB3 in Gazebo_House !')
        # self.myPb_gzb_house.setGeometry(10, 90, 300, 40)  # x,y,w,h
        self.myPb_gzb_house.clicked.connect(self.slot_gazebo_house)
        layout.addWidget(self.myPb_gzb_house)

        # --- Starte RViz ---
        self.myPb_rviz = QPushButton(self)
        self.myPb_rviz.setText(' RViz ')
        # self.myPb_rviz.setGeometry(10, 130, 300, 40)  # x,y,w,h
        self.myPb_rviz.clicked.connect(self.slot_rviz)
        layout.addWidget(self.myPb_rviz)

        # --- Starte Mapping ---
        self.myPb_gmap = QPushButton(self)
        self.myPb_gmap.setText(' Gmapping ')
        # self.myPb_gmap.setGeometry(10, 170, 300, 40)  # x,y,w,h
        self.myPb_gmap.clicked.connect(self.slot_gmapping)
        layout.addWidget(self.myPb_gmap)

        # --- Start Action Server Script ---
        self.myPb_action = QPushButton(self)
        self.myPb_action.setText('Action Server')
        # self.myPb_action.setGeometry(10, 210, 300, 40)  # x,y,w,h
        self.myPb_action.clicked.connect(self.slot_action_server)
        layout.addWidget(self.myPb_action)

        # --- Client ---
        self.myPb_client = QPushButton(self)
        self.myPb_client.setText(' Action Client - path from file')
        # self.myPb_client.setGeometry(10, 250, 300, 40)  # x,y,w,h
        self.myPb_client.clicked.connect(self.slot_action_client)
        layout.addWidget(self.myPb_client)

        self.setTabText(0, "Simualtion")
        self.tab1.setLayout(layout)

    def tab2UI(self):  # --- real TB3 ----
        self.Line_Edit_IP = QLineEdit("192.168.1.162")
        # --- Starte SSH Button ---
        self.myPb_ssh = QPushButton(self)
        self.myPb_ssh.setText('SSH - Start')
        self.myPb_ssh.clicked.connect(self.slot_ssh)
        # --- Map Saver Button ---
        self.myPb_map_save = QPushButton(self)
        self.myPb_map_save.setText('Save Map')
        self.myPb_map_save.clicked.connect(self.slot_save_map)
        # --- Navigation Start Button ---
        self.myPb_navigate = QPushButton(self)
        self.myPb_navigate.setText('Navigate to Goal with my_map')
        self.myPb_navigate.clicked.connect(self.slot_navigate_to_goal)

        self.myPb_navigate2 = QPushButton(self)
        self.myPb_navigate2.setText('Navigate to Goal with gmapping on')
        self.myPb_navigate2.clicked.connect(self.slot_navigate_to_goal2)
        # --- Teleop Start Button ---
        self.myPb_teleop = QPushButton(self)
        self.myPb_teleop.setText(' Teleop Keyboard ')
        self.myPb_teleop.clicked.connect(self.slot_teleop)

        # --- Grid Layout ---
        vbox = QVBoxLayout()
        # --- 1. Line ---
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("IP TurtleBot3 im WLAN eintragen"))
        hbox1.addWidget(self.myPb_teleop)
        vbox.addLayout(hbox1)
        # --- 2. Line ---
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel("SSH"))
        hbox2.addWidget(self.Line_Edit_IP)
        hbox2.addWidget(self.myPb_ssh)
        vbox.addLayout(hbox2)
        # --- 3. Line ---
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.myPb_map_save)
        vbox.addLayout(hbox3)
        # --- 4. Line ---
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.myPb_navigate)
        hbox4.addWidget(self.myPb_navigate2)
        vbox.addLayout(hbox4)

        self.setTabText(1, "real TurtleBot3 - SSH")
        self.tab2.setLayout(vbox)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.setTabText(2, "not used yet")
        self.tab3.setLayout(layout)

    # --- Die  Slot-Methoden ---
    def slot_roscore(self):
        os.system('gnome-terminal --tab -- /bin/bash -c "roscore; exec bash"')

    def slot_empty_world(self):
        os.system('gnome-terminal --tab -- /bin/bash -c \
                  "roslaunch turtlebot3_gazebo\
                  turtlebot3_empty_world.launch;\
                  exec bash"')

    def slot_gazebo_house(self):
        os.system('gnome-terminal --tab -- /bin/bash -c \
                  "roslaunch turtlebot3_gazebo turtlebot3_house.launch;\
                  exec bash"')

    def slot_rviz(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "roslaunch turtlebot3_gazebo\
                   turtlebot3_gazebo_rviz.launch;\
                  exec bash"')

    def slot_gmapping(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "roslaunch turtlebot3_slam\
                   turtlebot3_gmapping.launch ;\
                  exec bash"')

    def slot_action_server(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "rosrun rtc\
                  turtlebot3_server_path.py;\
                  exec bash"')

    def slot_action_client(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "rosrun rtc\
                  turtlebot3_client_path_from_file.py;\
                  exec bash"')

    def slot_ssh(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "ssh ubuntu@192.168.1.162; exec bash "')

    # absoluter Pfad notwendig "~"" does not work, evtl $HOME ?
    def slot_save_map(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "cd ~/catkin_ws/src/rtc/rtc_maps &&\
                  rosrun map_server map_saver -f \
                  my_map;\
                  exec bash"')

    def slot_navigate_to_goal(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "cd ~/catkin_ws/src/rtc/rtc_maps &&\
                  roslaunch turtlebot3_navigation\
                  turtlebot3_navigation.launch\
                  map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/my_map.yaml;\
                  exec bash"')

    def slot_navigate_to_goal2(self):
        os.system('gnome-terminal --tab -- /bin/bash -c\
                  "cd ~/catkin_ws/src/rtc/rtc_maps &&\
                  roslaunch turtlebot3_navigation\
                  turtlebot3_navigation.launch\
                  map_file:=dont_want_to_find_map_here\
                  exec bash"')
    
    def slot_teleop(self):
        os.system('gnome-terminal -- /bin/bash -c\
                  "rosrun teleop_twist_keyboard teleop_twist_keyboard.py;\
                  exec bash"')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
