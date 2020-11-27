#!/usr/bin/python
# -*- coding: utf-8 -*-
##pyqt_sw14_QSound.py

import sys
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)

###from PyQt5.QtMultimedia import *
###import QtMultimedia

from PyQt5.QtMultimedia import QSound
import random

class Ui(QWidget):
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(1000) 
        self.toggleFlag = True;  
        self.initUI()
    
    def initUI(self): 
        self.btn = QPushButton(self) 
        self.btn.setStyleSheet("background-color: grey")
        self.btn.resize(100,100)
        self.btn.move(20,20)   
            
        #UI-Fenster Konfigurieren
        self.setGeometry(20, 20,  400, 400)
        self.setWindowTitle('Qt - Timer')
        self.show()
        
    def update(self): 
        if self.toggleFlag == True: # Ein Feld in Bunt 
            self.toggleFlag = False
            # pick a sound file (.wav only) 
            # https://www.thesoundarchive.com/ringtones.asp
            sound_file = "pacman_death.wav"
            QSound.play(sound_file)
            zf = random.randint(0,3) #Zufallszahl               
            if zf == 0:
                self.btn.setStyleSheet("background-color: green")               
            elif zf == 1:            
                self.btn.setStyleSheet("background-color: red")
            elif zf== 2:            
                self.btn.setStyleSheet("background-color: yellow")
            elif zf == 3:            
                self.btn.setStyleSheet("background-color: blue")
        else:
            self.toggleFlag = True # Alle Felder Grau
            self.btn.setStyleSheet("background-color: grey")
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
