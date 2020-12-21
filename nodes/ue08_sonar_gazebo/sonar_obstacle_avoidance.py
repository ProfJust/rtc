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
        rospy.loginfo("Publishing sonar_left/cmd_vel")
        rospy.loginfo("Publishing sonar_right/cmd_vel")

        self.sonar_sub_left = rospy.Subscriber('sonar_left',
                                               Range,
                                               self.get_sonar_left,
                                               queue_size=10)
        self.sonar_sub_right = rospy.Subscriber('sonar_right',
                                                Range,
                                                self.get_sonar_right,  # ????
                                                queue_size=10)

        self.cmd_pub_left = rospy.Publisher('sonar_left/cmd_vel',
                                            Twist, queue_size=10)
        self.cmd_pub_right = rospy.Publisher('sonar_right/cmd_vel',
                                            Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.rate.sleep()

    def get_sonar_left(self, sensor_data_left):
        # rospy.loginfo(" Sonar Data received ")
        twist = Twist()
        self.set_backward = False
        if sensor_data_left.range < 0.3:  # Hindernis erkannt
            rospy.loginfo("Detected Obstacle in "
                          + str(sensor_data_left.range)
                          + " m Distance Left")
            # zuruecksetzen und rechts drehen
            twist.linear.x = -0.1
            twist.angular.z = -0.5
            self.cmd_pub_left.publish(twist)
            self.set_backward = True
        else:
            if sensor_data_left.range < 0.7 and self.set_backward:
                # zuruecksetzen und drehen
                turn_vel = 0.5
                lin_vel = -0.1
                twist.linear.x = lin_vel
                twist.angular.z = turn_vel
                self.cmd_pub_left.publish(twist)

                rospy.loginfo("Detected Obstacle in "
                              + str(sensor_data_left.range)
                              + " m Distance Left")
                rospy.loginfo("Robot goes backward ")
            else:
                # rospy.loginfo("No Obstacle detected ")
                self.set_backward = False
            # nix senden

    def get_sonar_right(self, sensor_data_right):
        # rospy.loginfo(" Sonar Data received ")
        twist = Twist()
        self.set_backward_right = False
        if sensor_data_right.range < 0.3:  # Hindernis erkannt
            rospy.loginfo("Detected Obstacle in "
                          + str(sensor_data_right.range)
                          + " m Distance Right")
            # zuruecksetzen und links drehen
            twist.linear.x = -0.1
            twist.angular.z = 0.5
            self.cmd_pub_right.publish(twist)
            self.set_backward_right = True
        else:
            if sensor_data_right.range < 0.7 and self.set_backward_right:
                # zuruecksetzen und drehen
                turn_vel = 0.5
                lin_vel = -0.1
                twist.linear.x = lin_vel
                twist.angular.z = turn_vel
                self.cmd_pub_right.publish(twist)

                rospy.loginfo("Detected Obstacle in "
                              + str(sensor_data_right.range)
                              + " m Distance Right")
                rospy.loginfo("Robot goes backward ")
            else:
                # rospy.loginfo("No Obstacle detected ")
                self.set_backward_right = False
            # nix senden


if __name__ == '__main__':
    rospy.init_node('sonar_controller', anonymous=True)
    try:
        sonar = Sonar()
    except rospy.ROSInterruptException:
        pass
