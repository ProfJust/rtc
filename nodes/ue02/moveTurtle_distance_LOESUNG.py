#!/usr/bin/env python3
# --- moveTurtle_distance_LOESUNG.py ------
# Version vom 16.11.2020 by OJ
# ohne OOP und Klasse
# ----------------------------------
# Starten von ROS und der TurtleSim
# $1 roscore
# $2 roslaunch turtlebot3_gazebo turtlebot3_house.launch
# $3 rosrun rtc moveTurtle_distance_gazebo.py
# (vorher catkin_make und  ausführbar machen mit chmod +x)
# ------------------------------------------

import rospy
from math import pow, atan2, sqrt, pi

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

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
    pose.y = round(data.y, 4)
    pose.theta = round(data.theta,  4)


def move():
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('turtlebot_controller', anonymous=True)

    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                         Twist,
                                         queue_size=10)
    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('/turtle1/pose',  Pose, update_pose)
    rate = rospy.Rate(10)

    # Get the input from the user.
    dist_x = eval(input("Set your x dist: "))
    dist_y = eval(input("Set your y dist: "))

    # Wegstrecke und Orientierung der Turtle berechnen
    dist = sqrt(pow(dist_x, 2) + pow(dist_y, 2))
    sollTheta = atan2(dist_y, dist_x)

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
        if pose.theta > pi:
            pose.theta = pose.theta - 2 * pi
        elif pose.theta < -pi:
            pose.theta = pose.theta + 2 * pi

        # set Angular velocity in the z-axis.
        if pose.theta - sollTheta > 0:
            vel_msg.angular.z = -0.1
        else:
            vel_msg.angular.z = 0.1
        # Debug ausgabe
        rospy.loginfo("Pose is %s", pose.theta)
        rospy.loginfo("Goal angle is %s", sollTheta)
        rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))
        velocity_publisher.publish(vel_msg)  # Publishing our vel_msg
        rate.sleep()  # Publish at the desired rate

    # Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

    # --- Dann die Strecke fahren ---
    while sqrt(pow((start_x - pose.x), 2)
               + pow((start_y - pose.y), 2)) < abs(dist):

        # Linear velocity in the x-axis.
        vel_msg.linear.x = 0.2
        rospy.loginfo("Pose is %s %s", pose.x, pose.y)
        rospy.loginfo("Still to Go %s ",
                      dist-sqrt(pow((start_x - pose.x), 2)
                                + pow((start_y - pose.y), 2)))
        # Publishing our vel_msg
        velocity_publisher.publish(vel_msg)

        # Publish at the desired rate.
        rate.sleep()

    # Stopping our robot after the movement is over.
    rospy.loginfo("Reached aim - now stopping ")

    # ----- hier Code einfügen ------

    exit()
    # If we press control + C, the node will stop.
    # rospy.spin()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
