#!/usr/bin/python
# -*- coding: utf-8 -*-
## pyqt_sw22a_GamePad_mit_ROS_joy.py
#----------------------------------------

# https://github.com/zeth/inputs
""" sudo apt-get install python-pygame """
# => DragonRise Inc.   Generic   USB  Joystick
# OJ: Getestet mit XBox360 Controller am USB


import sys
from PyQt5.QtCore import (Qt, QTimer, QRect)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtGui import QPixmap, QKeyEvent
import pygame


global ballsize
ballsize = 40

global keepersize
keepersize = 50

class Ui(QWidget):
	#statische Klassenvariablen
	pos_x = 200
	pos_y = 20
	pos_keeper = 200
	speed_x = +5
	speed_y = -6
	keyLeft = False
	keyRight = False
	
	def __init__(self): #Konstrukor
		#Konstruktor der Elternklasse aufrufen
		super(Ui, self).__init__()  
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update)  
		self.timer.start(20) 
		####### Gamepad #########
		pygame.init()
		# Initialize the joysticks
		pygame.joystick.init()
		# Get count of joysticks
		joystick_count = pygame.joystick.get_count()
		print("Number of joysticks: {}".format(joystick_count) )
		# For each joystick:
		for i in range(joystick_count):
			self.joystick = pygame.joystick.Joystick(i)
			self.joystick.init()    
			print("Joystick {}".format(i) )
		# Get the name from the OS for the controller/joystick
		self.name = self.joystick.get_name()
		print("Joystick name: {}".format(self.name) )
		self.axes = self.joystick.get_numaxes()
		print("Number of axes: {}".format(self.axes) )   
		
		#--------------------          
		self.initUI()
	
	def initUI(self):         
		#UI-Fenster Konfigurieren
		self.setGeometry(30, 30, 600, 600)
		self.setWindowTitle('Qt - Painter')
		self.show()
		
	def paintEvent(self, event):
		p = QPainter()
		p.begin(self)
		self.drawFunc(event, p)        
		p.end()
	
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Left:
			self.keyLeft = True
		if event.key() == Qt.Key_Right:
			self.keyRight = True
			
	def keyReleaseEvent(self, event):
		if event.key() == Qt.Key_Left:
			 self.keyLeft = False
		if event.key() == Qt.Key_Right:
			 self.keyRight = False
		event.accept()
		
	def drawFunc(self, event, p):            
		#Hintergrund mit Pixmap        
		pix = QPixmap("gras.jpg") 
		p.drawPixmap(self.rect(),pix)
		
		# Ball: bewegtes Rechteck zeichnen mit Pixmap          
		pix2 = QPixmap("ball_transparent.png")  #PNG mit Transparenz
		target =  QRect(self.pos_x,self.pos_y,ballsize,ballsize) #import QRect
		p.drawPixmap(target,pix2)
			
		#Keeper
		p.setBrush(QColor(0, 0, 0))#RGB 
		p.drawRect(self.pos_keeper,570,keepersize*2,20)
		
	def update(self): 
		# Gamepad lesen
		# EVENT PROCESSING STEP
		event = pygame.event.get() # User did something 
		print(event)        
		# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		
		for i in range( self.axes ):
			axis = self.joystick.get_axis( i )
			print("Axis {} value: {:>6.3f}".format(i, axis) )
			  
		buttons = self.joystick.get_numbuttons()
		print("Number of buttons: {}".format(buttons) )
	   
		for i in range( buttons ):
			button = self.joystick.get_button( i )
			print("Button {:>2} value: {}".format(i,button) )
		
		self.pos_x = self.pos_x + self.speed_x
		self.pos_y = self.pos_y + self.speed_y
		if self.pos_x < 0:
			self.speed_x = -self.speed_x
		if self.pos_x > 600-ballsize:
			self.speed_x = -self.speed_x       
		if self.pos_y < 0:
			self.speed_y = -self.speed_y
		#Keeper
		leftJoy = self.joystick.get_axis( 0 )
		print(leftJoy)
		if leftJoy<-0.1  and self.pos_keeper >=10:
				self.pos_keeper  = self.pos_keeper  - 5
		if leftJoy>0.1  and self.pos_keeper <=500:
				self.pos_keeper  = self.pos_keeper  + 5
		#Ball am Keeper
		if self.pos_y > 540:
			if (self.pos_x <= (self.pos_keeper + keepersize+ballsize)) and (self.pos_x >= (self.pos_keeper - keepersize)):
				self.speed_y = -self.speed_y
				self.pos_y = self.pos_y + self.speed_y
				
			else:
				pass
				#print("Game Over " + str(self.pos_x)+" " +str(self.pos_keeper ))
				#sys.exit()
					
		self.repaint()
   
if __name__ == '__main__':    
	app = QApplication(sys.argv)
	ui = Ui()
	sys.exit(app.exec_())
