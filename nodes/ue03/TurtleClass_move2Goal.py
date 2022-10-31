#!/usr/bin/env python3
# --- TurtleClass_move2Goal.py ------
# Version vom 25.10.2021 by OJ
# ----------------------------
# Basiert auf der Loesung aus dem Turtlesim Tutorial
# http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal

import rospy
from TurtleClassFile import TurtleBotClass


if __name__ == '__main__':
    try:
        turtle1 = TurtleBotClass('turtle1')
        turtle1.getGoalFromUser()
        turtle1.start_info()
        turtle1.move2goal()

        turtle2 = TurtleBotClass('turtle2')  # Name der Turtle
        turtle2.getGoalFromUser()
        turtle2.start_info()
        turtle2.move2goal()
    except rospy.ROSInterruptException:
        pass