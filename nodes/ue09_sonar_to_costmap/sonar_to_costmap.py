#!/usr/bin/env python3
# sonar_to_costmap.py
# ################################################################################
# edited WHS, OJ , 23.12.2020 #
#
# brings Sonar detected Obstacles into move_base local costmap
# using point_cloud - message
#
# edit
# copy content of turtlebot3.burger.gazebo_sonar.xacro
#              to turtlebot3.burger.gazebo_sonar.xacro
# copy content of turtlebot3.burger.urdf_sonar.xacro
#              to turtlebot3.burger.urdf.xacro
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
#   $3 roslaunch rts sonar_twist_mux.launch
#   $4 rosrun rtc sonar_obstacle_avoidance.py
#   $5 rosrun rtc sonar_to_costmap.py
# ------------------------------------------------------------------

import rospy
import std_msgs.msg
from geometry_msgs.msg import Point32
from sensor_msgs.msg import Range
from sensor_msgs.msg import PointCloud


class Sonar_to_Point_Cloud():
    def __init__(self):
        rospy.loginfo("Publishing PointCloud")

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
        pl = Point32()
        pm = Point32()
        pr = Point32()
        # Instanziiere leere PointCloud
        cloud = PointCloud()
        # filling pointcloud header
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        header.frame_id = 'base_link'
        cloud.header = header

        # Linke Seite
        if(self.dist_left < 0.95 and self.dist_left > 0.05):
            pl.x = self.dist_left + 0.05
            pl.y = 0.02
            pl.z = 0.0
            cloud.points.append(pl)

            pm.x = (self.dist_left + self.dist_right)/2 + 0.05
            pm.y = 0.0
            pm.z = 0.0
            cloud.points.append(pm)

        # Rechte Seite  punkt einfügen  (x,y,z)
        if(self.dist_right < 0.95 and self.dist_right > 0.05):
            pr.x = self.dist_right + 0.05
            pr.y = -0.02
            pr.z = 0.0
            cloud.points.append(pr)

        # Senden
        self.cloud_pub.publish(cloud)


if __name__ == '__main__':
    rospy.init_node('sonar_controller', anonymous=True)
    try:
        sonar = Sonar_to_Point_Cloud()
    except rospy.ROSInterruptException:
        pass
