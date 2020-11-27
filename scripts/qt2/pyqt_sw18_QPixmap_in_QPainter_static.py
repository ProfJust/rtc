#!/usr/bin/python
# -*- coding: utf-8 -*-
##pyqt_sw17_QPainter_dynamic.py

# https://www.tutorialspoint.com/pyqt/pyqt_qpixmap_class.htm

import sys
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtGui import QPixmap

class Ui(QWidget):
    #statische Klassenvariablen
    pos_x = 200
    pos_y = 20
    speed_x = -5
    
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(100)        
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
        
    def drawFunc(self, event, p):            
        #Rechteck zeichnen
        p.setBrush(QColor(0, 0, 0))#RGB 
        p.drawRect(10,100,196,442)
        
        pix = QPixmap("gras.jpg") 
        p.drawPixmap(self.rect(),pix)
        
##        pixmap = QPixmap("myPic.png")
##        painter.drawPixmap(self.rect(), pixmap)
##        
        #Ball zeichnen
        p.setBrush(QColor(255,0,0))
        p.drawEllipse(self.pos_x,self.pos_y,25,25)
            
        
    def update(self): 
        self.pos_x = self.pos_x + self.speed_x
        if self.pos_x < 0:
            self.pos_x = 300
        self.repaint()
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
