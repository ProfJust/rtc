#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 12.12.2020 #
# usage
#    $1 roslaunch turtlebot3_gazebo turtlebot3_house.launch
#    $2 roslaunch turtlebot3_navigation turtlebot3_navigation.launch /
#         map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map_2020_12_07
#    $3 rosrun rtc turtlebot3_move_base_action_client.py  (this file here)
#       the Server is already started with move_base
# based on the code from
# https://hotblackrobotics.github.io/en/blog/2018/01/29/action-client-py/

# den RVIZ-Tool Pfeil Navigation Goal nutzen um die
# Posen in den Pfad zu schreiben
# über Tool Properties anderes Topic einstellen
# mit publish_pose_2_file.py

import rospy
import actionlib  # Brings in the SimpleActionClient
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Initial Koordinaten für Ort x,y und Orientierung x,y,z,w
path = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
# Vollstaendiger Pfad der Datei
filename = "/home/oj/catkin_ws/src/rtc/nodes/ue07_navigation_amcl/path.txt"


def read_path_from_file(filename):
    rospy.loginfo("Reading Path from path.txt : ")
    # Den vorgegebenen Pfad einlesen, jede Zeile ein Goal
    with open(filename, 'r') as fin:
        for line in fin:
            path.append(eval(line))  # Goal anhaengen
    del path[0]  # [0, 0] entfernen
    rospy.loginfo(str(path))


def movebase_client():
    # Create an action client called "move_base" /
    # with action definition file "MoveBaseAction"
    # /opt/ros/noetic/include/move_base_msgs
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # Waits until the action server has started up
    # and is listening for goals.
    client.wait_for_server()
    read_path_from_file(filename)  # Hole Pfad aus Datei
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    for koord in path:
        # set posistion (no z)
        goal.target_pose.pose.position.x = koord[0]
        goal.target_pose.pose.position.y = koord[1]
        # set orientation - quaternion
        goal.target_pose.pose.orientation.x = koord[2]
        goal.target_pose.pose.orientation.y = koord[3]
        goal.target_pose.pose.orientation.z = koord[4]
        goal.target_pose.pose.orientation.w = koord[5]

        # Sends the goal to the action server.
        client.send_goal(goal)

        # wait for the action to return, with timeout
        finished_before_timeout = client.wait_for_result(
                                           rospy.Duration(120.0))
        if finished_before_timeout is True:
            rospy.loginfo(" Reached Goal before Timeout ")
        else:
            rospy.loginfo(" Timeout ")

    return client.get_result()


# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
        # let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Path execution done!")

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
