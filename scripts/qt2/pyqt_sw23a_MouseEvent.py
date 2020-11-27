#!/usr/bin/python
# -*- coding: utf-8 -*-
#pyqt_sw23_MouseEvent.py

import sys
from PyQt5.QtCore import (Qt, QTimer, QRect)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtGui import QPixmap, QKeyEvent

class Ui(QWidget):
    #statische Klassenvariablen
    mouse_pos_x = 0
    mouse_pos_y = 0
        
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.initUI()
    
    def initUI(self):         
        #UI-Fenster Konfigurieren
        self.setGeometry(30, 30, 600, 600)
        self.setWindowTitle('Qt - Mouse Event')
        self.setMouseTracking(True)
        self.show()
    
    def mouseMoveEvent(self, event): #Methode der QWidget-Klasse
        self.mouse_pos_x = event.x()
        self.mouse_pos_y = event.y()
        #print Mouse Position
        print('x: %d  y: %d' % (self.mouse_pos_x, self.mouse_pos_y))
        
    def mousePressEvent(self, event): #Methode der QWidget-Klasse
        if  event.button()== Qt.LeftButton:
            print('Linksklick')
        if  event.button()== Qt.RightButton:
            print("Rechtsklick")
            
    def mouseDoubleClickEvent(self, event): #Methode der QWidget-Klasse
        if  event.button()== Qt.LeftButton:
            print('Linksklick doppelt, mit Rechtsklick doppelt wird es wieder klein')
            #self.showMaximized() #mit Titelzeile
            self.showFullScreen() #ohne Titelzeile
        if  event.button()== Qt.RightButton:
            print("Rechtsklick doppelt")
            self.showNormal() #urspruengiche Groesse
            #self.showMinimized() #ganz weg
            
    def paintEvent(self, event): #Methode der QWidget-Klasse
        p = QPainter()
        p.begin(self)
        self.drawFunc(event, p)        
        p.end()
    
    def keyPressEvent(self, event): #Methode der QWidget-Klasse
        if event.key() == Qt.Key_Left:
            self.keyLeft = True
        if event.key() == Qt.Key_Right:
            self.keyRight = True
            
    def keyReleaseEvent(self, event): #Methode der QWidget-Klasse
        if event.key() == Qt.Key_Left:
             self.keyLeft = False
        if event.key() == Qt.Key_Right:
             self.keyRight = False
        event.accept()
    
    def drawFunc(self, event, p):            
        #Hintergrund mit Pixmap        
        pix = QPixmap("gras.jpg") 
        p.drawPixmap(self.rect(),pix)   
             
        
  
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
