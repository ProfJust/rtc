#!/usr/bin/env python3
# --- talker.py ------
# Version vom 18.10.2021 by OJ
# -----------------------------
import rospy  # Standard Bibliothek für ROS mit Python
from std_msgs.msg import String  # vordefinierte Message


def talker():
    # Publisher wirt vereinbart message name, typ, ..
    pub = rospy.Publisher('rtc-chatter', String, queue_size=10)

    # Node wird vereinbart
    rospy.init_node('rtc-talker', anonymous=True)
    rate = rospy.Rate(1)  # 1hz
    i = 1
    while not rospy.is_shutdown():
        hello_str = "WHS - Hello python world %d" % i
        i = i + 1
        rospy.loginfo(hello_str)  # Ausgabe Shell
        pub.publish(hello_str)  # Ausgabe im ROS
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo(" Fehler im ROS ")
        #  pass
