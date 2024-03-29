#!/usr/bin/env python3
# ################################################################################
# edited WHS, OJ , 15.11.2021 #
# usage
#    $1 roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
#    $2 rosrun rtc turtlebot3_server_path.py
#    $3 rosrun rtc turtlebot3_client_path.py

# oder
# $ roslaunch rtc turtlebot3_action_server_client_path_gazebo_empty.launch

import rospy
import actionlib
import turtlebot3_example.msg
# from TurtleBotClassFile import TurtleBotClass
from TurtleBotClassOhneInitNodeLaserScan import TurtleBotClass


class Turtlebot3Action(object):
    # Daten fuer Feedback und Result instanziieren
    _feedback = turtlebot3_example.msg.Turtlebot3ActionFeedback()
    _result = turtlebot3_example.msg.Turtlebot3ActionResult()

    def __init__(self, name):
        self.myTurtle = TurtleBotClass()
        self._action_name = name
        self._as = actionlib.SimpleActionServer(
                   self._action_name,
                   turtlebot3_example.msg.Turtlebot3Action,
                   execute_cb=self.execute_cb,
                   auto_start=False)

        self.init_stats = True
        self._as.start()
        rospy.loginfo('Server is On - Waiting for client-request')

    def execute_cb(self, goal):
        self.myTurtle.goal.x = goal.goal.x
        self.myTurtle.goal.y = goal.goal.y
        req_str = 'Server is sending TurtleBot to point '\
                  + str(goal.goal.x) + " " + str(goal.goal.y)
        rospy.loginfo(req_str)
        # Ziel erreicht => True
        while not self.myTurtle.move2goal() and not rospy.is_shutdown():
            # feedback not working yet
            # feedback_str = 'Server: Turtlebot ist auf dem Weg '\
            # + str(goal.goal.x) + " " + str(goal.goal.y)
            # self._feedback.feedback = feedback_str
            # self._as.publish_feedback(self._feedback)
            pass

        # ---- SET RESULT -----
        # publish result, Umbruch zu lange codezeile mit \
        result_str = 'Server: Turtlebot reached point '\
                     + str(goal.goal.x) + " " + str(goal.goal.y)
        self._result.result = result_str
        self._as.set_succeeded(self._result)
        # rospy.loginfo(result_str)


if __name__ == '__main__':
    rospy.init_node('turtlebot3')
    server = Turtlebot3Action(rospy.get_name())
    rospy.spin()
