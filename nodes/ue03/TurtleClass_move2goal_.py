#!/usr/bin/env python3
# --- TurtleClass_move2Goal.py ------
# Version vom 23.11.2020 by OJ
# ----------------------------
# from
# --- P3_V4_TurtleClass_move2goal.py ------
# Version vom 22.10.2019 by OJ
# Basiert auf der Loesung aus dem Turtlesim Tutorial
# http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal
#
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleBotClass:
    # Attribut der Klasse
    goal = Pose()

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        # globale Variablen instanzieren
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=1):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def getGoalFromUser(self):
        goal_pose = Pose()  # lokal
        goal_pose.x = eval(input("Set your x goal: "))
        goal_pose.y = eval(input("Set your y goal: "))
        return goal_pose

    def debug_info(self):
        # Debug Info
        rospy.loginfo("Start Pose is %s %s", self.pose.x, self.pose.y)
        rospy.loginfo("Goal is       %s %s", self.goal.x, self.goal.y)
        rospy.loginfo("Distannce to Goal is  %f ",
                      self.euclidean_distance(self.goal))
        rospy.loginfo("SteeringAngle to Goal is  %f ",
                      self.steering_angle(self.goal))

    def move2goal(self, distance_tolerance=0.1):
        """Moves the turtle to the goal."""
        # fuer die Funktion lokale Objekte instanzieren => kein self notwendig
        vel_msg = Twist()

        self.debug_info()

        # python V2 raw_input("Hit any Key to start")
        input("Hit any Key to start")

        while self.euclidean_distance(self.goal) >= distance_tolerance:
            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(self.goal)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(self.goal)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()
            rospy.loginfo("Pose is %s %s", self.pose.x, self.pose.y)
            rospy.loginfo("Speed is x: %s  theta: %s",
                          vel_msg.linear.x, vel_msg.angular.z)

        # Stopping our robot after the movement is over.
        rospy.loginfo(" ######  Goal reached #######")
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        exit()


if __name__ == '__main__':
    try:
        turtle1 = TurtleBotClass()
        turtle1.goal = turtle1.getGoalFromUser()
        turtle1.move2goal()
    except rospy.ROSInterruptException:
        pass
