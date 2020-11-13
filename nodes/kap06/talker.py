#!/usr/bin/env python3
# --- talker.py ------
# Version vom 12.11.2020 by OJ
# -----------------------------
import rospy
from std_msgs.msg import String


def talker():
    # Publisher wirt vereinbart message name, typ, ..
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # Node wird vereinbart
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    i = 0
    while not rospy.is_shutdown():
        hello_str = "WHS - Hello python world %d" % i
        i = i + 1
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo(" Fehler ")
        pass
