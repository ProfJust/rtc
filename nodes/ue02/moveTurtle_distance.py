#!/usr/bin/env python3
# --- moveTurtle_distance.py ------
# Version vom 16.11.2020 by OJ
# ohne OOP und Klasse
# ----------------------------------
# Starten von ROS und der TurtleSim
# $1 roscore
# $2 rosrun turtlesim turtlesim_node
# $3 python moveTurtle_distance.py   (vorher ausführbar machen mit chmod +x)
# ------------------------------------------

import rospy
from math import pow, atan2, sqrt, pi

from geometry_msgs.msg import Twist  # cmd_vel
from turtlesim.msg import Pose       # pose

# --- Instanzierung einer globale pose - Variable ---
# Wird benoetigt um die pose aus der callback-Funktion
# (ohne Aufruf bzw. return) heraus zu bekommen,
pose = Pose()


def update_pose(data):
    # Callback function which is called when a new message
    # of type Pose is received by the subscriber.
    # rospy.loginfo(rospy.get_caller_id() + "x %s  y %s  theta %s",
    #                                   data.x, data.y, data.theta)
    pose.x = round(data.x, 4)  # Runde auf 4 Stellen
    ### HIER CODE EINFUEGEN ###


def move():
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('turtlebot_controller', anonymous=True)

    # Publisher which will publish to the Twist topic '/turtle1/cmd_vel'.
    velocity_publisher = rospy.Publisher('### HIER CODE EINFUEGEN ###',
                                         ### HIER CODE EINFUEGEN ###,
                                         queue_size=10)
    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('### HIER CODE EINFUEGEN ###',  Pose, ### HIER CODE EINFUEGEN ###)
    rate = rospy.Rate(10)

    # Get the input from the user.
    dist_x = eval(input("Set your x dist: "))
    dist_y = ### HIER CODE EINFUEGEN ###

    # Wegstrecke und Orientierung der Turtle berechnen
    dist = ### HIER CODE EINFUEGEN ###
    sollTheta = ### HIER CODE EINFUEGEN ###

    # Get start pose of Turtle - meanwhile received?
    start_x = pose.x
    start_y = pose.y

    # Debug ausgabe
    rospy.loginfo("Start Pose is %s %s", start_x, start_y)
    rospy.loginfo("Angle to turn %s ", sollTheta)
    rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))

    vel_msg = Twist()  # Twist Nachricht instanzieren

    # --- Erst die Turtle drehen ---
    tolerance = 0.015
    while (abs(pose.theta - sollTheta) > tolerance):
        # theta auf Bereich [-pi...pi] begrenzen
        ### HIER CODE EINFUEGEN ###

        # set Angular velocity in the z-axis.
        if pose.theta - sollTheta > 0:
            vel_msg.angular.z = -0.4
        else:
            vel_msg.angular.z = 0.4

        # Debug ausgabe
        rospy.loginfo("Pose is %s", pose.theta)
        rospy.loginfo("Goal angle is %s", sollTheta)
        rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))

        velocity_publisher.publish(### HIER CODE EINFUEGEN ###)  # Publishing our vel_msg
        rate.sleep()  # Publish at the desired rate

    # Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(### HIER CODE EINFUEGEN ###)

    # --- Dann die Strecke fahren ---
    while ### HIER CODE EINFUEGEN ###:

        # Linear velocity in the x-axis.
        ### HIER CODE EINFUEGEN ###

        # Publishing our vel_msg

        velocity_publisher.publish(### HIER CODE EINFUEGEN ###)  # Publishing our vel_msg

        rospy.loginfo("Pose is %s %s", pose.x, pose.y)
        rospy.loginfo("Still to Go %s ",
                      dist-sqrt(pow((start_x - pose.x), 2)
                                + pow((start_y - pose.y), 2)))

        # Publish at the desired rate.
        rate.sleep()

    # Stopping our robot after the movement is over.
    rospy.loginfo("Reached aim - now stopping ")

    # Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

    exit()
    # If we press control + C, the node will stop.
    # rospy.spin()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
