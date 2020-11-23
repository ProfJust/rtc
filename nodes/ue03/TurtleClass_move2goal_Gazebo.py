#!/usr/bin/env python3
# --- TurtleClass_move2Goal_Gazebo.py ------
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
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt


class TurtleBotClass:
    # globale Variablen
    goal = Pose()

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/odpm. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('odom',
                                                Odometry, self.update_pose)

        # globale Variablen instanzieren
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def quaternion_to_euler(self, x, y, z, w):
        # https://computergraphics.stackexchange.com/questions/8195/how-to-convert-euler-angles-to-quaternions-and-get-the-same-euler-angles-back-fr
        """t0 = 2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll = atan2(t0, t1) # Drehung um X-Achse

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch = asin(t2))  # Drehung um Y-Achse"""

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = atan2(t3, t4)  # Drehung um Z-Achse in rad

        return yaw

    def update_pose(self, data):
        # Callback function which is called when a new message
        # of type Pose is received by the subscriber.
        self.pose.x = round(data.pose.pose.position.x, 4)
        self.pose.y = round(data.pose.pose.position.y, 4)
        # rospy.loginfo(rospy.get_caller_id() + "x %s  y %s ", pose.x, pose.x)
        # orientation als Quaternion
        x = data.pose.pose.orientation.x
        y = data.pose.pose.orientation.y
        z = data.pose.pose.orientation.z
        w = data.pose.pose.orientation.w
        self.pose.theta = self.quaternion_to_euler(x, y, z, w)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=0.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=1.0):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def getGoalFromUser(self):
        goal_pose = Pose()  # lokal
        goal_pose.x = eval(input("Set your x goal: "))
        goal_pose.y = eval(input("Set your y goal: "))
        return goal_pose

    def move2goal(self, distance_tolerance=0.05, maxSpeedX=0.3, maxSpeedZ=0.5):
        """Moves the turtle to the goal."""
        # fuer die Funktion lokale Objekte instanzieren => kein self notwendig
        vel_msg = Twist()

        # Debug Info
        rospy.loginfo("Start Pose is %s %s", self.pose.x, self.pose.y)
        rospy.loginfo("Goal is       %s %s", self.goal.x, self.goal.y)
        rospy.loginfo("Distannce to Goal is  %f ",
                      self.euclidean_distance(self.goal))
        rospy.loginfo("SteeringAngle to Goal is  %f ",
                      self.steering_angle(self.goal))
        # python V2 raw_input("Hit any Key to start")
        input("Hit any Key to start")

        while self.euclidean_distance(self.goal) >= distance_tolerance:
            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            speedX = self.linear_vel(self.goal)
            if speedX > maxSpeedX:
                speedX = maxSpeedX  # Maximum begrenzen
            vel_msg.linear.x = speedX
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            speedZ = self.angular_vel(self.goal)
            if speedZ > maxSpeedZ:
                speedZ = maxSpeedZ  # Maximum begrenzen
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = speedZ

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

