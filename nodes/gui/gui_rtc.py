#!/usr/bin/env python3
# --- gui_rtc.py ------
# Version vom 28.10.2022 by OJ
# basiert auf dem GUI-Pojekt aus dem WS21/22
# von L. Fuhrig, M. Heinen,
#     J. Klinker, Y. Kurniawan
# -----------------------------
# usage: $ rosrun rtc gui_rtc.py  ? funkt nicht, warum?
# aber so: oj@RosePC:~/catkin_ws/src/rtc$ /usr/bin/python3 /home/oj/catkin_ws/src/rtc/nodes/gui/gui_rtc.py

from ast import While
import io
import shlex
import subprocess
import sys
import os
import threading
import time

from PyQt5.QtCore import QObject, QThread, QThreadPool, pyqtSignal, QRunnable, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QDial, QDialog, QMainWindow, QMessageBox)
from PyQt5.QtGui import QTextCursor
from PyQt5.uic import loadUi

from ros_pyqt_ui import Ui_Dialog

def call_log(logobj):
    font = logobj.font()
    font.setFamily('Courier')
    font.setPointSize(10)
    return font

def add_to_log(logobj, text, font):
    logobj.moveCursor(QTextCursor.End)
    logobj.setCurrentFont(font)
    logobj.insertPlainText(text)
    logobj.insertPlainText("\r\n")
    sb = logobj.verticalScrollBar()
    sb.setValue(sb.maximum())
    print("Added to Log:", text)

def master_ntpupdate(slf):
    slf.master_ntpUpdateLabel.setText("NTP Update gestartet")
    font = call_log(slf.master_log)

    with open('test.log', 'wb') as f: 
        process = subprocess.Popen(['sudo', 'ntpdate', '192.168.1.111'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while process.stdout.readable():
            line = process.stdout.readline()
            if not line:
                break
            else:
                add_to_log(slf.master_log, line.strip().decode('utf-8'), font)

    slf.master_ntpUpdateLabel.setText("NTP Update beendet")

def master_start_ros(slf):
    font = call_log(slf.master_log)
    os.system('gnome-terminal -- bash -c "roscore; exec bash"')


    if False:
        with subprocess.Popen(['roscore'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0) as proc:
            text = proc.stdout.read().decode('utf-8')
            #text = proc.communicate()
            print(text)
            add_to_log(slf.master_log, text, font)

def master_check_ros(slf):
        font = call_log(slf.master_log)
        logs = []
        with open('test.log', 'wb') as f: 
            process = subprocess.Popen(['rosnode', 'list'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, preexec_fn=os.setsid, bufsize=1)
            while process.stdout.readable():
                line = process.stdout.readline()
                if not line:
                    break
                else:
                    text = str(line.strip().decode('utf-8'))
                    logs.append(text)
                    add_to_log(slf.master_log, text, font)
        if '/rosout' in logs:
            add_to_log(slf.master_log, "The ROS Master is running as the ros node rosout is available", font)

def client_ntpupdate(slf):
    font = call_log(slf.client_log)
    with subprocess.Popen(['sudo', 'ntpdate', '192.168.1.111'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0) as proc:
        text = proc.stdout.read().decode('utf-8')
        add_to_log(slf.client_log, text, font)

def client_getRTCPath(slf):
    path = slf.client_rtcproject_path.toPlainText()
    return path

def client_getArenaName(slf):
    input = slf.client_alternativeArena.toPlainText()
    if not input or input == "" or len(input) == 0:
        return "Arena"
    else:
        return str(input)

def client_mapSelection(slf):
    alternativeArena = client_getArenaName(slf)
    # if another arena is typed in, use that name and not the selected one
    if alternativeArena == "Arena":
        index = slf.client_wegauswahl.currentIndex()
        if index == 0:
            return "Arena_kurz"
        elif index == 1:
            return "Arena_Umweg"
        elif index == 2:
            return "Arena_PlanB"
    else:
        return alternativeArena

def client_slam(slf):
    command = "roslaunch rtc_project slam.launch gazebo:=false controller_layout:=2 map_file:=" + client_getRTCPath(slf) + "/maps/" + client_getArenaName(slf)
    add_to_log(slf.client_log, command, call_log(slf.client_log))
    os.system('gnome-terminal -- bash -c "' + command + '; exec bash"')
    pass

def client_punkteSetzen(slf):
    command = "roslaunch rtc_project set_navigation_points.launch points_via_robot:=true gazebo:=false controller_layout:=2 map_file:=" + client_getRTCPath(slf) + "/maps/" + client_getArenaName(slf) + ".yaml"
    add_to_log(slf.client_log, command, call_log(slf.client_log))
    os.system('gnome-terminal -- bash -c "' + command + '; exec bash"')
    pass

def client_rviz(slf):
    command = "roslaunch rtc_project navigation.launch gazebo:=false map_file:=" + client_getRTCPath(slf) + "/maps/" + client_getArenaName(slf) + ".yaml"
    add_to_log(slf.client_log, command, call_log(slf.client_log))
    os.system('gnome-terminal -- bash -c "' + command + '; exec bash"')
    pass

def client_wegfuehrungStarten(slf):
    command = "rosrun rtc_project turtlebot3_move_base_action_client.py " + client_getRTCPath(slf) + "/maps/" + client_mapSelection(slf) + ".txt"
    add_to_log(slf.client_log, command, call_log(slf.client_log))
    os.system('gnome-terminal -- bash -c "' + command + '; exec bash"')
    pass

def turtlebot_ntpupdate(slf):
    import paramiko
    host = slf.turtlebot_ip.toPlainText()
    username = slf.turtlebot_user.toPlainText()
    password = slf.turtlebot_password.toPlainText()

    try:
        add_to_log(slf.turtlebot_log, 'Attempting NTP Update at ' + host, call_log(slf.turtlebot_log))
        add_to_log(slf.turtlebot_log, 'Connecting via SSH to ' + host, call_log(slf.turtlebot_log))
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        stdin, _stdout,_stderr = client.exec_command("ntpdate 192.168.1.111")
        add_to_log(slf.turtlebot_log, _stdout.read().decode('utf-8'), call_log(slf.turtlebot_log))
        client.close()
    except Exception as e:
        add_to_log(slf.turtlebot_log, str(e), call_log(slf.turtlebot_log))

def turtlebot_bringup(slf):
    import paramiko
    host = slf.turtlebot_ip.toPlainText()
    username = slf.turtlebot_user.toPlainText()
    password = slf.turtlebot_password.toPlainText()

    try:
        add_to_log(slf.turtlebot_log, 'Attempting Bringup at ' + host, call_log(slf.turtlebot_log))
        add_to_log(slf.turtlebot_log, 'Connecting via SSH to ' + host, call_log(slf.turtlebot_log))
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        stdin, _stdout,_stderr = client.exec_command("roslaunch turtlebot3_bringup turtlebot3_bringup.launch")
        add_to_log(slf.turtlebot_log, _stdout.read().decode('utf-8'), call_log(slf.turtlebot_log))
        client.close()
    except Exception as e:
        add_to_log(slf.turtlebot_log, str(e), call_log(slf.turtlebot_log))

def call_worker(a, func, *args, **kwargs):
    worker = Worker(func, a, *args, **kwargs)
    a.threadpool.start(worker)

class Worker(QRunnable):

    def __init__(self, fn, slf, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.slf = slf

    @pyqtSlot()
    def run(self):
        self.fn(self.slf, *self.args, **self.kwargs)

class Window(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.threadpool = QThreadPool()
        self.master_ntpupdate.clicked.connect(lambda: call_worker(self, master_ntpupdate))
        self.master_roscore.clicked.connect(lambda: call_worker(self, master_start_ros))
        self.master_roscoreCheck.clicked.connect(lambda: call_worker(self, master_check_ros))
        
        self.client_ntpupdate.clicked.connect(lambda: call_worker(self, client_ntpupdate))
        self.client_SLAM.clicked.connect(lambda: call_worker(self, client_slam))
        self.client_punkteSetzen.clicked.connect(lambda: call_worker(self, client_punkteSetzen))
        self.client_RVIZ.clicked.connect(lambda: call_worker(self, client_rviz))
        self.client_wegfuehrungStarten.clicked.connect(lambda: call_worker(self, client_wegfuehrungStarten))

        self.turtlebot_ntpupdate.clicked.connect(lambda: call_worker(self, turtlebot_ntpupdate))
        self.turtlebot_bringup.clicked.connect(lambda: call_worker(self, turtlebot_bringup))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())