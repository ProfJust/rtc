import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleBotClass:
    def __init__(self, turtleName='turtle1'):  # Konstruktor
        # globale Klassen-Variablen instanzieren
        self.pose = Pose()
        self.goal = Pose()
        self.vel_msg = Twist()

        self.objektname = turtleName
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        try:
            rospy.init_node('turtlebot_controller', anonymous=True)
        except rospy.ROSInterruptException:
            pass

        zk = turtleName + '/cmd_vel'  # eine Zeichenkette
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher(zk,
                                                  Twist, queue_size=10)

        zk = turtleName + '/pose'
        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber(zk,
                                                Pose, self.update_pose)
        self.rate = rospy.Rate(10)

    def start_info(self):
        # Debug Info
        rospy.loginfo("Start Pose is %f %f", self.pose.x, self.pose.y)
        rospy.loginfo("Goal is       %f %f", self.goal.x, self.goal.y)
        rospy.loginfo("Distannce to Goal is  %f ",
                      self.euclidean_distance())
        rospy.loginfo("SteeringAngle to Goal is  %f ",
                      self.steering_angle())
        input("Hit any Key to start")

    def getGoalFromUser(self):
        # self.stop_robot()
        print(self.objektname)
        self.goal.x = eval(input("Set your x goal: "))
        self.goal.y = eval(input("Set your y goal: "))
        # goal.theta not used
        if self.goal.x < 0 or self.goal.y < 0:
            input("Keine negativen Werte erlaubt - hit any key")
            exit(1)

    def update_pose(self, data):  # CallbacK für Pose
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((self.goal.x - self.pose.x), 2) +
                    pow((self.goal.y - self.pose.y), 2))

    def set_linear_vel(self, constant=0.5, lin_max=1.0):
        lin_vel = constant * self.euclidean_distance()
        if lin_vel > lin_max:
            lin_vel = lin_max  # Maximum begrenzen
        self.vel_msg.linear.x = lin_vel
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0

    def steering_angle(self):
        return atan2(self.goal.y - self.pose.y, self.goal.x - self.pose.x)

    def set_angular_vel(self, constant=3.0, ang_vel_max=1.5):
        ang_vel = constant * (self.steering_angle() - self.pose.theta)
        if(ang_vel > ang_vel_max):
            ang_vel = ang_vel_max
        # Message to publish
        self.vel_msg.angular.z = ang_vel
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0

    def stop_robot(self):
        # Stopping our robot after the movement is over.
        rospy.loginfo(" ######  Goal reached, Stop Robot #######")
        # Message to publish
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

    def is_goal_reached(self, distance_tolerance=0.1):
        if self.euclidean_distance() < distance_tolerance:
            return True
        else:
            return False

    def pose_speed_info(self):
        rospy.loginfo("Pose is %s %s",
                      round(self.pose.x, 4),
                      round(self.pose.y, 4))
        rospy.loginfo("Speed is x: %s  theta: %s",
                      round(self.vel_msg.linear.x, 4),
                      round(self.vel_msg.angular.z, 4))

    def move2goal(self):
        # Moves the turtle to the goal

        while not self.is_goal_reached():
            # Linear velocity in the x-axis.
            self.set_linear_vel()
            # Angular velocity in the z-axis.
            self.set_angular_vel()
            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)
            # Publish at the desired rate.
            # self.rate.sleep()  <===== Wieso Fehler ????
            # debug Info
            self.pose_speed_info()

        self.stop_robot()  # when goal is reached
        # exit()