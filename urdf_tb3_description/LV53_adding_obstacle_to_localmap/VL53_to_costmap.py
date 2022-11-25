#!/usr/bin/env python3
# sonar_to_costmap.py
# ################################################################################
# edited WHS, OJ , 25.11.2022 #
#
# brings VL53L0x detected Obstacles into move_base local costmap
# using point_cloud - message
#
# edit
# only Gazebo
# copy content of turtlebot3.burger.gazebo_sonar.xacro
#              to turtlebot3.burger.gazebo_sonar.xacro
# copy content of turtlebot3.burger.urdf_sonar.xacro
#              to turtlebot3.burger.urdf.xacro
#
# real Bot and Gazebo
# edit costmap_common_params_burger.yaml
#    observation_sources: scan sonar
#    scan: ...
#    sonar: {sensor_frame: base_link, data_type: PointCloud,
#             topic: /sonar/point_cloud, marking: true, clearing: true}
#
# edit move_base.launch  => /cmd_vel to /move_base/cmd_vel
#     <arg name="cmd_vel_topic" default="/move_base/cmd_vel" />
#
# usage
#   $1 roslaunch turtlebot3_gazebo turtlebot3_house.launch
#   $2 roslaunch turtlebot3_navigation turtlebot3_navigation.launch
#                map_file:=$HOME/catkin_ws/src/rtc/rtc_maps/gazebo_house_map_2020_12_07.yaml
#   $3 roslaunch rtc sonar_twist_mux.launch
#   $4 rosrun rtc sonar_obstacle_avoidance.py
#   $5 rosrun rtc sonar_to_costmap.py
# ------------------------------------------------------------------

import rospy
import std_msgs.msg
from geometry_msgs.msg import Point32
from sensor_msgs.msg import Range
from sensor_msgs.msg import PointCloud  # Message für die Sonar-Hindernisse


class VL53_to_Point_Cloud():
    def __init__(self):
        rospy.loginfo("Publishing PointCloud")

        self.cloud_pub = rospy.Publisher('VL53/point_cloud',
                                         PointCloud,
                                         queue_size=10)

        # receiving sonar_left and sonar_right
        self.sonar_sub_left = rospy.Subscriber('VL53_left',
                                               Range,
                                               self.get_sonar_left,
                                               queue_size=10)
        self.sonar_sub_right = rospy.Subscriber('VL53_right',
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
        pl = Point32()  # Punkt von Sonar Left
        # pm = Point32()  # Mittelpunkt
        pr = Point32()  # Sonar Right
        # Instanziiere leere PointCloud
        cloud = PointCloud()
        # filling pointcloud header
        header = std_msgs.msg.Header()  # Leere Instanz
        header.stamp = rospy.Time.now()  # Fülle Zeitstempel
        header.frame_id = 'base_link'
        cloud.header = header

        # Linke Seite
        if(self.dist_left < 0.7 and self.dist_left > 0.05):
            # difference frames: base_link to base_sonar_front_right
            pl.x = self.dist_left * 0.866 + 0.05  # Offset Sensor Montagepunkt
            pl.y = self.dist_left * 0.5 - 0.03  # Offset Sensor Montagepunkt
            pl.z = 0.06
            cloud.points.append(pl)

        # Rechte Seite  punkt einfügen  (x,y,z)
        # Gegenkathete = sin(phi) * Hypothenuse
        # phi = 60° = 1.042  sin(60°) = 0.866
        # Hyphotenuse = dist
        # Ankathete = cos(60°) * dist
        # cos(60°) = 0.5
        if(self.dist_right < 0.7 and self.dist_right > 0.05):
            # difference frames: base_link to base_sonar_front_right
            pr.x = self.dist_right * 0.866 + 0.05  # Offset Sensor Montagepunkt
            pr.y = -(self.dist_right * 0.5) + 0.03  # Offset Sensor Montagepunkt
            pr.z = 0.06
            cloud.points.append(pr)

        # Senden
        self.cloud_pub.publish(cloud)


if __name__ == '__main__':
    rospy.init_node('VL53_controller', anonymous=True)
    try:
        vl53 = VL53_to_Point_Cloud()
    except rospy.ROSInterruptException:
        pass
