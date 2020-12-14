#!/usr/bin/env python3
# publish_point_2_file.py
# ################################################################################
# edited WHS, OJ , 3.12.2020 #
# usage
#   $1 roslaunch rtc turtlebot3_action_server_client_path_gazebo_house.launch
#   $2 rosrun rtc publish_pose_2_file.py
#   click at point at RViz-Map  => save in  File

import rospy
from geometry_msgs.msg import PoseStamped
filename = "/home/oj/catkin_ws/src/rtc/nodes/ue07_navigation_amcl/path.txt"


def clickCB(data):
    rospy.loginfo("clicked at " + str(data.pose.position.x)
                  + " " + str(data.pose.position.y))
    fobj = open(filename, 'a')
    write_str = "[" + str(data.pose.position.x) + ","\
                    + str(data.pose.position.y) + ","\
                    + str(data.pose.orientation.x) + ","\
                    + str(data.pose.orientation.y) + ","\
                    + str(data.pose.orientation.z) + ","\
                    + str(data.pose.orientation.w) \
                    + "] \n"
    fobj.write(write_str)
    fobj.close()


if __name__ == '__main__':
    try:
        rospy.init_node('goal_listener', anonymous=True)
        rospy.loginfo("Auf der RVIZ- Karte ein 2D Nav Goal ankllicken,\
                      /move_base_simple/goal2")
        click_sub = rospy.Subscriber('/move_base_simple/goal2',
                                     PoseStamped,
                                     clickCB)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            pass

    except rospy.ROSInterruptException:
        print("program close.")
