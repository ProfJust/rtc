#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 12.11.2021 #
# usage
#    $1 roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
#    $2 rosrun rtc turtlebot3_server_path.py
#    $3 rosrun rtc turtlebot3_client_path.py

import rospy
import actionlib
import turtlebot3_example.msg
import sys

msg = """
TurtleBot3 patrols along path
-----------------------------
"""


class Client():
    def __init__(self):
        rospy.loginfo("wait for server")
        self.client()

    def getkey(self):
        count = eval(input("Number of Patrols?  <to close, insert 'x'> \n"))
        return count

    def client(self):
        # Instanziierung des Clients
        client = actionlib.SimpleActionClient(
                'turtlebot3',
                turtlebot3_example.msg.Turtlebot3Action)
        client.wait_for_server()
        # goal instanziieren
        goal = turtlebot3_example.msg.Turtlebot3Goal()
        # ---------------------------------------------------------
        # Pfad festlegen
        path = [[2.0, 0.0], [2.0, 2.0], [0.0, 2.0], [0.0, 0.0]]
        # ---------------------------------------------------------
        # Runden?
        numbOfPatrols = self.getkey()
        runde_nr = 1
        while runde_nr <= numbOfPatrols and not rospy.is_shutdown():
            rospy.loginfo("Patrol Round Nr %d of %d ", runde_nr, numbOfPatrols)
            for koord in path:
                # set goal
                goal.goal.x = koord[0]
                goal.goal.y = koord[1]
                goal.goal.z = runde_nr
                req_str = 'Server is sending TurtleBot to point '
                req_str = req_str + str(goal.goal.x) + " " + str(goal.goal.y)
                rospy.loginfo(req_str)
                # send goal
                client.send_goal(goal)
                # wait for the action to return with timeout 40sec
                finished_before_timeout = client.wait_for_result(
                                           rospy.Duration(40.0))
                if finished_before_timeout is True:
                    rospy.loginfo(" Done before Timeout ")
                else:
                    rospy.loginfo(" Timeout ")
            # Runde beendet
            runde_nr = runde_nr + 1
        exit()


if __name__ == '__main__':
    rospy.init_node('turtlebot3_client')
    try:
        while not rospy.is_shutdown():
            print(msg)
            result = Client()
    except:
        print("program close.", file=sys.stderr)

