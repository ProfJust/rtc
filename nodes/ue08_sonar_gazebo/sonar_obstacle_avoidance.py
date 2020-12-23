#!/usr/bin/env python3
# sonar_obstacle_avoidance.py
# ################################################################################
# edited WHS, OJ , 17.12.2020 #
# usage
# copy content of turtlebot3.burger.gazebo_sonar.xacro
#              to turtlebot3.burger.gazebo_sonar.xacro
# copy content of turtlebot3.burger.urdf_sonar.xacro
#              to turtlebot3.burger.urdf.xacro
#
#   $1 roslaunch turtlebot3_gazebo turtlebot3_house.launch
#   $2 roslaunch turtlebot3_navigation turtlebot3_navigation.launch
#                map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map_2020_12_07.yaml
#   $4 rosrun rtc turtlebot3_sonar.py
# ---------------------------------------

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range


class Sonar():
    def __init__(self):
        rospy.loginfo("Publishing sonar/cmd_vel")
        self.cmd_pub = rospy.Publisher('sonar/cmd_vel',
                                       Twist, queue_size=10)
        # receiving sonar_left and sonar_right
        self.sonar_sub_left = rospy.Subscriber('sonar_left',
                                               Range,
                                               self.get_sonar_left,
                                               queue_size=10)
        self.sonar_sub_right = rospy.Subscriber('sonar_right',
                                                Range,
                                                self.get_sonar_right,
                                                queue_size=10)
        self.dist_left = 0.0
        self.dist_right = 0.0
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.rate.sleep()

    def get_sonar_left(self, sensor_data_left):
        # rospy.loginfo(" Sonar Data Left received ")
        self.dist_left = sensor_data_left.range
        self.sonar_move()

    def get_sonar_right(self, sensor_data_right):
        # rospy.loginfo(" Sonar Data Right received ")
        self.dist_right = sensor_data_right.range
        self.sonar_move()

    def sonar_move(self):
        twist = Twist()
        if self.dist_left < 0.3:  # Hindernis links erkannt
            if self.dist_left < self.dist_right:
                rospy.loginfo("detects obstacle in "
                              + str(self.dist_left)
                              + " m distance Left")
                # zuruecksetzen und rechts drehen
                twist.linear.x = -0.1
                # minus ist rechtsherun, getestet mit rqt
                twist.angular.z = -0.5
                self.cmd_pub.publish(twist)
                return

        if self.dist_right < 0.3:  # Hindernis rechts erkannt
            if self.dist_right < self.dist_left:
                rospy.loginfo("detects obstacle in "
                              + str(self.dist_right)
                              + " m distance right")
                # zuruecksetzen und links drehen
                twist.linear.x = -0.1
                twist.angular.z = 0.5
                self.cmd_pub.publish(twist)
        return


if __name__ == '__main__':
    rospy.init_node('sonar_controller', anonymous=True)
    try:
        sonar = Sonar()
    except rospy.ROSInterruptException:
        pass
