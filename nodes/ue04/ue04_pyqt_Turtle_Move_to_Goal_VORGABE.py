#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
 QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QLabel)

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBotClass:
	# globale Variablen	
	goal = Pose()

	def __init__(self):
		# Creates a node with name 'turtlebot_controller' and make sure it is a
		# unique node (using anonymous=True).
		rospy.init_node('turtlebot_controller', anonymous=True)

		# Publisher which will publish to the topic '/turtle1/cmd_vel'.
		self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

		# A subscriber to the topic '/turtle1/pose'. self.update_pose is called
		# when a message of type Pose is received.
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
		
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

	def angular_vel(self, goal_pose, constant=6):
		return constant * (self.steering_angle(goal_pose) - self.pose.theta)
		
	def getGoalFromUser(self):
		goal_pose = Pose() #lokal
		goal_pose.x = input("Set your x goal: ")
		goal_pose.y = input("Set your y goal: ")	
		return goal_pose

	def move2goal(self):
		"""Moves the turtle to the goal."""
		distance_tolerance  = 0.1 
		# fuer die Funktion lokale Objekte instanzieren => kein self notwendig		
		vel_msg = Twist()
		
		# Debug Info
		rospy.loginfo("Start Pose is %s %s", self.pose.x, self.pose.y)
		rospy.loginfo("Goal is       %s %s", self.goal.x, self.goal.y)
		rospy.loginfo("Distannce to Goal is  %f ", self.euclidean_distance(self.goal))
		rospy.loginfo("SteeringAngle to Goal is  %f ", self.steering_angle(self.goal))
		#raw_input("Hit any Key to start")

		while self.euclidean_distance(self.goal) >= distance_tolerance:
			# Porportional controller.
			# https://en.wikipedia.org/wiki/Proportional_control

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
			rospy.loginfo("Speed is x: %s  theta: %s", vel_msg.linear.x, vel_msg.angular.z)

		# Stopping our robot after the movement is over.
		rospy.loginfo(" ######  Goal reached #######" )
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.velocity_publisher.publish(vel_msg)
		#exit()
		
class TurtleUIClass(QWidget):	
	def __init__(self): #Konstrukor
		#Konstruktor der Elternklasse aufrufen
		super(TurtleUIClass, self).__init__()      
		self.initUI()
				
	def initUI(self): 
		#Instanziierung der Widgets    
		startWert = 5  
		lcd = QLCDNumber(self)
		lcd.display(startWert)
		self.sld = QSlider(Qt.Horizontal, self)
		self.sld.setMaximum(11)
		self.sld.setMinimum(0)
		self.sld.setValue(startWert)
		pbLess = QPushButton('<')
		pbMore = QPushButton('>')
		pbGo = QPushButton(' Go Turtle ')
		self.lblStatus = QLabel('Statuszeile')
		
		#BOX-Layout mit Widgets füllen
		vbox = QVBoxLayout()
		#1.Reihe        
		vbox.addWidget(lcd)
		#2.Reihe
		vbox.addWidget(self.sld)
		#3.Reihe
		hbox = QHBoxLayout()
		hbox.addWidget(pbLess)
		hbox.addWidget(pbMore)
		vbox.addLayout(hbox)
		#4.Reihe
		vbox.addWidget(pbGo)
		#Alle Boxen ins Window setzen        
		self.setLayout(vbox)           
		
		#Signal und Slot verbinden
		self.sld.valueChanged.connect(lcd.display)
		self.sld.valueChanged.connect(lcd.display)

		pbLess.clicked.connect(self.SlotKlick)
		pbMore.clicked.connect(self.SlotKlick)		
		pbGo.clicked.connect(self.SlotGo)
		
		#Fenster Konfigurieren
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('ROP - PyQt - TurtleSteering')
		self.show()
		
	def SlotKlick(self):
		sender = self.sender()
		self.lblStatus.setText(sender.text() + ' was pressed')   
		if sender.text()=='<':
			wert = self.sld.value()
			wert = wert-1
			self.sld.setValue(wert)  
		else:
			wert = self.sld.value()
			wert = wert+1
			self.sld.setValue(wert)
			
	def SlotGo(self):
		""" Hier geht die Turtle ab """
		turtle1.goal.x = self.sld.value()
		turtle1.goal.y = self.sld.value()
		turtle1.move2goal()
		
if __name__ == '__main__':    
	turtle1 = TurtleBotClass()
	
	app = QApplication(sys.argv)
	ex = TurtleUIClass()
	sys.exit(app.exec_())
