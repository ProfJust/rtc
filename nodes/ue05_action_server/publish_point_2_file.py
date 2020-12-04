#!/usr/bin/env python3
# publish_point_2_file.py
# ################################################################################
# edited WHS, OJ , 3.12.2020 #
# usage
#   $1 roslaunch rtc turtlebot3_action_server_client_path_gazebo_house.launch
#   $2 rosrun rtc publish_point_2_file
#   click at point at RViz-Map  => save in  File

import rospy
from geometry_msgs.msg import PointStamped


def clickCB(data):
    rospy.loginfo("clicked at " + str(data.point.x) + " " + str(data.point.y))
    fobj = open("/home/oj/catkin_ws/src/rtc/nodes/ue05_action_server/path2.txt", 'a')
    write_str = "[" + str(data.point.x) + ", " + str(data.point.y) + "] \n"
    fobj.write(write_str)    
    fobj.close()


if __name__ == '__main__':
    try:
        rospy.init_node('click_listner', anonymous=True)
        rospy.loginfo("Auf der RVIZ- Karte einen Publish Point ankllicken")
        click_sub = rospy.Subscriber('clicked_point',
                                     PointStamped,
                                     clickCB)
        rate = rospy.Rate(10)
        
        while not rospy.is_shutdown():
            pass




    except:
        print("program close.", file=sys.stderr)
