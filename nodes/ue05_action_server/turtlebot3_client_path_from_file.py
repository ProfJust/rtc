#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 15.11.2021   #
# usage
#    $1 roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
#    $2 rosrun rtc turtlebot3_server_path.py
#    $3 rosrun rtc turtlebot3_client_path_from_file.py

import rospy
import actionlib
import turtlebot3_example.msg
import sys
# from yaml import load

msg = """
TurtleBot3 patrols along path
-----------------------------
"""


class Client():
    def __init__(self):
        self.client()

    def read_path_from_file(self,
                            filename="/home/oj/catkin_ws/src/rtc/nodes/ue05_action_server/path_ws22a.txt"):
        rospy.loginfo("Reading Path from path.txt : ")
        # Den vorgegebenen Pfad einlesen
        # self.path = [[0.0, 0.0],[2.0, 0.0], [2.0, 2.0], [0.0, 2.0]]
        # aus einer Datei funktioniert es oftmals nicht
        # beim lesen erfolgt Abbruch des Programms
        # Das liegt am relativen Datei-Pfad
        # muss absolut sein, vom root-Verzeichnis an
        # nicht ~/ verwenden!!!  => auf den User anpassen
        self.path = [[0.0, 0.0]]  # Initial Koordinaten
        with open(filename, 'r') as fin:
            for line in fin:
                self.path.append(eval(line))
            del self.path[0]  # [0, 0] entfernen
        rospy.loginfo(str(self.path))

    def getkey(self):
        count = eval(input("Number of Patrols?  <to close, insert 'x'> \n"))
        return count

    def client(self):
        # Instanzierung client
        client = actionlib.SimpleActionClient(
                'turtlebot3',
                turtlebot3_example.msg.Turtlebot3Action)
        client.wait_for_server()
        # Instanzierung goal
        goal = turtlebot3_example.msg.Turtlebot3Goal()
        self.read_path_from_file()  # Hole Pfad aus Datei
        numbOfPatrols = self.getkey()
        runde_nr = 1
        while runde_nr <= numbOfPatrols and not rospy.is_shutdown():
            rospy.loginfo("Patrol Round Nr %d of %d ", runde_nr, numbOfPatrols)
            for koord in self.path:
                # setze goal
                goal.goal.x = koord[0]
                goal.goal.y = koord[1]
                goal.goal.z = runde_nr
                req_str = 'Server is sending TurtleBot to point '
                req_str = req_str + str(goal.goal.x) + " " + str(goal.goal.y)
                rospy.loginfo(req_str)
                # sende goal an server
                client.send_goal(goal)
                # wait for the action to return
                finished_before_timeout = client.wait_for_result(
                                           rospy.Duration(40.0))
                if finished_before_timeout is True:
                    rospy.loginfo(" Done before Timeout ")
                else:
                    rospy.loginfo(" Timeout ")
            # Runde beendet
            runde_nr = runde_nr + 1
        client.cancel_all_goals()
        # http://wiki.ros.org/actionlib/DetailedDescription
        # exit()


if __name__ == '__main__':
    rospy.init_node('turtlebot3_client')
    try:
        while not rospy.is_shutdown():
            print(msg)
            client = Client()  # Instanziierung
    except:
        print("program closed.", file=sys.stderr)

