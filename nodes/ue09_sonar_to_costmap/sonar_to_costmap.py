#!/usr/bin/env python3
# sonar_to_costmap.py
# ################################################################################
# edited WHS, OJ , 23.12.2020 #
#
# brings Sonar detected Obstacles into move_base costmap
# using point_cloud - message
#
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
from geometry_msgs.msg import Point32
from sensor_msgs.msg import Range
from sensor_msgs.msg import PointCloud


class Sonar_Point_Cloud():
    def __init__(self):
        rospy.loginfo("Publishing PointCloud")

        # Instanziiere PointCloud
        self.cloud = PointCloud()
        self.cloud_pub = rospy.Publisher('sonar/point_cloud',
                                         PointCloud,
                                         queue_size=10)

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
        self.cloud_build()

    def get_sonar_right(self, sensor_data_right):
        # rospy.loginfo(" Sonar Data Right received ")
        self.dist_right = sensor_data_right.range
        self.cloud_build()

    def cloud_build(self):
        # add sonar readings (robot-local coordinate frame) to cloud
        p = Point32()

        # Linke Seite
        p.x = self.dist_left
        p.y = -0.5
        p.z = 0.0
        self.cloud.points.append(p)

        # Rechte Seite  punkt einfügen  (x,y,z)
        p.x = self.dist_right
        p.y = 0.5
        p.z = 0.0
        self.cloud.points.append(p)

        # Senden
        self.cloud_pub.publish(self.cloud)


if __name__ == '__main__':
    rospy.init_node('sonar_controller', anonymous=True)
    try:
        sonar = Sonar_Point_Cloud()
    except rospy.ROSInterruptException:
        pass
