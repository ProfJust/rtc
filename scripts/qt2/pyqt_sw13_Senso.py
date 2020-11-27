#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=Q-U9oqv2bTk
##pyqt_sw13_Senso.py
import sys
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
# sudo apt-get install python-pyqt5.qtmultimedia
from PyQt5.QtMultimedia import QSound

import random

global S 
S = 2 #Spalten
global R 
R = 2 #Reihen
global SIZE
SIZE = 150

class Ui(QWidget):
    #statische Klassnevariablen
    zug_anz = 0
    zug = 0
    user_dran = False
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(1000) 
        self.toggleFlag = True;  
        self.initUI()
        # Sounds aus http://codeperspectives.com/front-end/simon-says-sound/
        self.sound_red= "sounds/a_sharp.wav"
        self.sound_green= "sounds/c_sharp.wav"
        self.sound_yellow= "sounds/d_sharp.wav"
        self.sound_blue= "sounds/f_sharp.wav"
        
        self._list = ["Liste der Farben: "]
           
    def klickSlot(self):
        clkSender = self.sender()    #Sender holen
        clkColor  = clkSender.color #Werte vom Sender
        #clkSpalte = clkSender._spalte
        print('geklickt auf ' + str(clkColor) )   
        if clkColor == "green":     
            self.btn[0][0].setStyleSheet("background-color: green")
        if clkColor == "yellow":     
            self.btn[1][0].setStyleSheet("background-color: yellow")
        if clkColor == "red":     
            self.btn[0][1].setStyleSheet("background-color: red")
        if clkColor == "blue":     
            self.btn[1][1].setStyleSheet("background-color: blue")
        
        #for i in range(Ui.zug_anz):
                #welcher Button wird geklickt?
                
                #wenn falsch QSound und exit()
                
                #entspricht der Button der Liste
        Ui.user_dran=False
        self.timer.start(1000) 
        
    def initUI(self): 
        self.btn = [[QPushButton(self)  for s in range(S)] for r in range(R)] 
        self.btn[0][0].color = "green" 
        self.btn[1][0].color = "yellow" 
        self.btn[0][1].color = "red" 
        self.btn[1][1].color = "blue" 
        for r in range(R):
          for s in range(S): 
            self.btn[r][s].setStyleSheet("background-color: grey")
            self.btn[r][s].resize(SIZE,SIZE)
            self.btn[r][s].move(SIZE*r+20, SIZE*s+20)   
            #Signal und Slot verbinden
            #pybutton = QPushButton('Click me', self)
            #pybutton.clicked.connect(self.clickMethod)
            self.btn[r][s].clicked.connect(self.klickSlot)
            
        self.lblStatus = QLabel("Senso",self)        
        self.lblStatus.setGeometry(10, 10, SIZE * R +40, 50)
        self.lblStatus.setWordWrap(True)
        
        #Fenster Konfigurieren
        self.setGeometry(20, 20, SIZE * S + 40, SIZE * R +40)
        self.setWindowTitle('Qt - Senso')
        self.show()        
        
    
    def update(self): 
        if Ui.user_dran==False: #Senso ist dran
            if self.toggleFlag == True: # Ein Feld in Bunt 
                self.toggleFlag = False
                Ui.zug = Ui.zug + 1
                if Ui.zug >= Ui.zug_anz: #neuer Zug 
                    Ui.zug_anz = Ui.zug_anz+1
                    Ui.user_dran = True
                    Ui.zug = 0
                    zf = random.randint(0,3) #Zufallszahl               
                    if zf == 0:
                        self.btn[0][0].setStyleSheet("background-color: green")
                        self.btn[0][1].setStyleSheet("background-color: grey")
                        self.btn[1][0].setStyleSheet("background-color: grey")
                        self.btn[1][1].setStyleSheet("background-color: grey") 
                        QSound.play(self.sound_green)
                        self._list.append("green")
                    elif zf == 1:            
                        self.btn[0][0].setStyleSheet("background-color: grey")
                        self.btn[0][1].setStyleSheet("background-color: red")
                        self.btn[1][0].setStyleSheet("background-color: grey")
                        self.btn[1][1].setStyleSheet("background-color: grey") 
                        QSound.play(self.sound_red)
                        self._list.append("red")
                    elif zf== 2:            
                        self.btn[0][0].setStyleSheet("background-color: grey")
                        self.btn[0][1].setStyleSheet("background-color: grey")
                        self.btn[1][0].setStyleSheet("background-color: yellow")
                        self.btn[1][1].setStyleSheet("background-color: grey")
                        QSound.play(self.sound_yellow)
                        self._list.append("yellow")
                    elif zf == 3:            
                        self.btn[0][0].setStyleSheet("background-color: grey")
                        self.btn[0][1].setStyleSheet("background-color: grey")
                        self.btn[1][0].setStyleSheet("background-color: grey")
                        self.btn[1][1].setStyleSheet("background-color: blue")
                        QSound.play(self.sound_blue)
                        self._list.append("blue")
            else:
                self.toggleFlag = True # Alle Felder Grau
                self.btn[0][0].setStyleSheet("background-color: grey")
                self.btn[0][1].setStyleSheet("background-color: grey")
                self.btn[1][0].setStyleSheet("background-color: grey")
                self.btn[1][1].setStyleSheet("background-color: grey")
                self.lblStatus.setText(str(self._list))
        else: #Benutzer ist dran                
            self.timer.stop()
            #alles bunt
            
            self.btn[0][0].setStyleSheet("background-color: darkgreen")
            self.btn[0][1].setStyleSheet("background-color: darkred")
            self.btn[1][0].setStyleSheet("background-color: orange")
            self.btn[1][1].setStyleSheet("background-color: darkblue")
            # => laueft im klickSlot


    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
