#!/usr/bin/env python3
# --- moveTurtle_distance_gazebo.py ------
# Version vom 16.11.2020 by OJ
# ohne OOP und Klasse
# ----------------------------------
# Starten von ROS und der TurtleSim
# $1 roscore
# $2 roslaunch turtlebot3_gazebo turtlebot3_house.launch
# $3 rosrun rtc moveTurtle_distance_gazebo.py
# vorher catkin_make + ausführbar machen mit chmod +x
# ------------------------------------------

import rospy
from math import pow, atan2, sqrt, pi

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose

# --- Instanzierung einer globale pose - Variable ---
# Wird benoetigt um die pose aus der callback-Funktion
# (ohne Aufruf bzw. return) heraus zu bekommen,
pose = Pose()


def quaternion_to_euler(self, x, y, z, w):
    # https://computergraphics.stackexchange.com/questions/8195/how-to-convert-euler-angles-to-quaternions-and-get-the-same-euler-angles-back-fr
    """t0 = 2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = atan2(t0, t1) # Drehung um X-Achse

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = asin(t2))  # Drehung um Y-Achse"""

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = atan2(t3, t4)  # Drehung um Z-Achse in rad

    return yaw


def update_pose(data):
    # Callback function which is called when a new message
    # of type Pose is received by the subscriber.
    pose.x = round(data.pose.pose.position.x, 4)
    pose.y = round(data.pose.pose.position.y, 4)
    # rospy.loginfo(rospy.get_caller_id() + "x %s  y %s ", pose.x, pose.x)
    # orientation als Quaternion
    x = data.pose.pose.orientation.x
    y = data.pose.pose.orientation.y
    z = data.pose.pose.orientation.z
    w = data.pose.pose.orientation.w
    pose.theta = quaternion_to_euler(x, y, z, w)


def move():
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('turtlebot_controller', anonymous=True)

    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    velocity_publisher = rospy.Publisher('/cmd_vel',
                                         Twist,
                                         queue_size=10)
    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('odom',  Odometry, update_pose)
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
    # rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))

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
            vel_msg.angular.z = -0.2
        else:
            vel_msg.angular.z = 0.2
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

        # Publishing our vel_msg

        velocity_publisher.publish(vel_msg)  # Publishing our vel_msg

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
