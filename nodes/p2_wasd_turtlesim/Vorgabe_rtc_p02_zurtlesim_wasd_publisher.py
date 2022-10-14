#!/usr/bin/env python3
# --- rtc_p02_turtlesim_wasd_publisher.py ------
# Version vom 14.10.2022 by OJ
# -----------------------------
import rospy
from geometry_msgs.msg import Twist
# from turtlesim.msg import Pose


# Einzelnes Zeichen lesen mit getch()
# https://www.raspberrypi.org/forums/viewtopic.php?t=69046
def getch():
    import sys
    import termios
    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch


# Publisher which will publish to the topic '/turtle1/cmd_vel'.
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0


def set_vel():
    c = getch()
    # if c == 'w' and vel_msg.linear.x <= 1.0:
    #    vel_msg.linear.x += 0.1
    # ## HIER CODE EINFUEGEN ###
    vel_msg.linear.x = 0.1
    vel_msg.angular.z = -0.1


if __name__ == '__main__':
    # Node wird vereinbart
    rospy.init_node('wasd_node', anonymous=True)
    rate = rospy.Rate(50)  # 50hz
    print(" wasd-Steurung für die TurtleSim"
          "- bitte Taste drücken, Exit mit 'c'")

    try:
        while not rospy.is_shutdown():
            set_vel()
            velocity_publisher.publish(vel_msg)
            rate.sleep()

    except rospy.ROSInterruptException:
        rospy.loginfo(" ROS Fehler ")
        pass
