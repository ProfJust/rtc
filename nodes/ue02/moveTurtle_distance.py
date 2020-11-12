#!/usr/bin/env python3
# --- moveTurtle_distance.py ------
# Version vom 12.11.2030 by OJ
# ohne OOP und Klasse
#----------------------------------
# Starten
# $1 roscore
# $2 rosrun turtlesim turtlesim_node 
# $3 python moveTurtle_distance.py   (vorher ausführbar machen mit chmod +x)
#------------------------------------------


import rospy
import math
#from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt   

#--- globale Variable ---
pose=Pose()

def update_pose(data):
    # Callback function which is called when a new message 
    # of type Pose is received by the subscriber.
    #rospy.loginfo(rospy.get_caller_id() + "x %s  y %s  theta %s", data.x, data.y, data.theta)
    pose.x = round(data.x, 4)
    pose.y = round(data.y, 4)
    pose.theta = round(data.theta,  4)
    
def move():
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('turtlebot_controller', anonymous=True)
    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('/turtle1/pose',  Pose, update_pose)    
    rate = rospy.Rate(10)
    # Get the input from the user.
    dist_x = eval(input("Set your x dist: "))
    dist_y = eval(input("Set your y dist: "))
    dist = sqrt(pow(dist_x,2)+pow(dist_y,2))
    sollTheta = atan2(dist_y,dist_x)
    
    # Get start Position of Turtle - meanwhile received?
    start_x = pose.x
    start_y = pose.y
    # Please, insert a number slightly greater than 0 (e.g. 0.01).
    # dist_tolerance = input("Set your tolerance: ")
    rospy.loginfo("Start Pose is %s %s", start_x, start_y)
    rospy.loginfo("Angle to turn %s ", sollTheta)
    rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))
    vel_msg = Twist()
   
    #--- Erst den Drehwinkel korrigieren---
    while (abs(pose.theta - sollTheta) > 0.015):
        # theta Bereich [-pi...pi]
        if pose.theta > math.pi:
            pose.theta =pose.theta-2*math.pi
        elif pose.theta < -math.pi:
            pose.theta = pose.theta+2*math.pi
        
        # Angular velocity in the z-axis.
        if pose.theta - sollTheta > 0:
            vel_msg.angular.z = -0.1
        else:
            vel_msg.angular.z = 0.1
       
        rospy.loginfo("Pose is %s", pose.theta)
        rospy.loginfo("Goal angle is %s", sollTheta)
        rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))
        velocity_publisher.publish(vel_msg) # Publishing our vel_msg
        rate.sleep() # Publish at the desired rate
         
    # Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    
    #--- Dann die Strecke fahren ---
    while sqrt(pow((start_x - pose.x),2)+pow((start_y - pose.y),2)) < abs(dist):
        # Linear velocity in the x-axis.
       
       
       #----- hier Code einfügen ------
       
       
        # Publishing our vel_msg
        
            #----- hier Code einfügen ------
               
        
        # Publish at the desired rate.
        rate.sleep()
                
    # Stopping our robot after the movement is over.
    rospy.loginfo("Reached aim - now stopping ")
    
        #----- hier Code einfügen ------
       
    exit()
    # If we press control + C, the node will stop.
    # rospy.spin()
    

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
