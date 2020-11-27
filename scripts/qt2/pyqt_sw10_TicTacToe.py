#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyqt_sw10_TicTacToe.py

TicTacToe-Spiel mit QPushButton
erweitert durch Vererbung um
reihe, spalte 

Author: Olaf Just
Website: robotik.bocholt@w-hs.de
Last edited: 20.11.2018
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)

class myTicTacButton(QPushButton):
    # Konstruktor
    # benötigt Angabe von Reihe Spalte
    def __init__(self, r, s, parent=None):  #####<==== kein PROBLEM mehr
        super(myTicTacButton,self).__init__(parent)        
        #QPushButton.__init__(self,'Text')  
              
        # setzen der zusaetzlichen Attribute
        self._reihe = r
        self._spalte = s
        # setzen der Attribute der Elternklasse QPushButton
        self.setText(' ')  
        self.resize(50,50)
        self.move((r+1)*50, (s+1)*50)      

    # zusaetzliche Fkt von myTicTacButton 
    def KlickSlot(self):
        clkSender = self.sender()    #Sender holen
        print(clkSender)
        clkReihe  = clkSender._reihe #Werte vom Sender
        clkSpalte = clkSender._spalte
        print('geklickt auf ' + str(clkReihe) + ' ' + str(clkSpalte))
        if clkSender.text()==' ':
            if ex.XistDran==True:
                clkSender.setText('X')
                ex.XistDran = False
                ex.lblStatus.setText('O ist dran')
            else:
                clkSender.setText('O')
                ex.XistDran = True
                ex.lblStatus.setText('X ist dran')

        #Aufruf der Funktion der Hauptklasse ex        
        ex.checkGameOver()
        if ex.gameState==3:
            ex.lblStatus.setText('Spiel zu Ende - Alles Belegt')
        if ex.gameState==1:
            ex.lblStatus.setText('X hat gewonnen')
        if ex.gameState==2:
            ex.lblStatus.setText('O hat gewonnen')
                

class Game(QWidget):
    
    # List 
    gameState = 0  # 0=noch was frei, 1 = X,  2=O  hat gewonnen, 3=alles belegt
    
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Game, self).__init__()      
        self.initUI()
    
    def initUI(self): 
        
        self.XistDran = True
        # Instanziierung der Widgets          
        # Tupel fuer Reihen und Spalten Indizierung
        rangeReihenIndex  = (0,1,2) 
        rangeSpaltenIndex = (0,1,2)
        self.matrix = [[myTicTacButton(r,s,self) for s in range(3)] for r in range(3)] 

        ##        self.btn = QPushButton('Text',self)# ====> funkt nur mit self
        #self.btn = myTicTacButton(0,0,self)  
        #(0,0,self)===> TypeError: __init__() takes exactly 3 arguments (4 given)
        #self is passed implicitly when you call an instance method on an instance
        # => Paramter parent einfügen
               
        for reihe in rangeReihenIndex:
          for spalte in rangeSpaltenIndex:
            #Signal und Slot verbinden
            self.matrix[reihe][spalte].clicked.connect(self.matrix[reihe][spalte].KlickSlot)
                
        self.lblStatus = QLabel('X ist dran      ',self)
        self.lblStatus.setGeometry(60, 350, 200, 50)
        # self.lblStatus.move(60, 350)         
        
        #Fenster Konfigurieren
        self.setGeometry(20, 20, 400, 400)
        self.setWindowTitle('Tic Tac Toe')
        self.show()
        
    def checkGameOver(self):
        #Noch ein Platz unbelegt?
        allesBelegt = False
#        for s in range(3):
#            for r in range(3):
#                if self.matrix[r][s].text==' ':
#                    allesBelegt = False
#                    print(self.matrix[r][s].text)
        if allesBelegt == False:
            if self.matrix[0][0].text() =='X' and self.matrix[0][1].text()=='X' and self.matrix[0][2].text() =='X':
                self.gameState = 1
            if self.matrix[0][0].text() =='O' and self.matrix[0][1].text()=='O' and self.matrix[0][2].text() =='O':
                self.gameState = 2
        else:
            self.gameState = 3 #alles belegt, aber keiner gewonnen
        
        return allesBelegt

if __name__ == '__main__':    
    
    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())
