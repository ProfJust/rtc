#!/usr/bin/python
# -*- coding: utf-8 -*-
##pyqt_sw15_QPixmap.py
import sys
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
from PyQt5.QtGui import QPixmap

class Ui(QWidget):
    #statische Klassenvariablen
    pos_label_x = 20
    
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(100)        
        self.initUI()
    
    def initUI(self):         
        self.lbl = QLabel(" Ein Label ", self)
        self.lbl.setGeometry(20, 20,  196, 442)
        #self.lbl.setStyleSheet("background-color: blue")
        
        pix = QPixmap("Streicholz.png") #196x442 Pixel
        self.lbl.setPixmap(pix)
            
        #UI-Fenster Konfigurieren
        self.setGeometry(20, 20,  1000, 500)
        self.setWindowTitle('Qt - Pixmap')
        self.show()
        
    def update(self): 
        self.pos_label_x = self.pos_label_x+10
        if self.pos_label_x > 1000:
            self.pos_label_x = 0
        self.lbl.move(self.pos_label_x,20)
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
