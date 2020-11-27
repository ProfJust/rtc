#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyqt_sw11_Quinto.py

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
N = 4 #Spielfeldgroesse
from enum import Enum
class stateClass (Enum):
        FREI = 0
        XWIN = 1
        OWIN = 2
        AOCC = 3

class myQuintoButton(QPushButton):
    # Konstruktor
    # benötigt Angabe von Reihe Spalte
    def __init__(self, r, s, ui, parent): 
        super(myQuintoButton,self).__init__(parent) 
        # setzen der zusaetzlichen Attribute
        self._reihe = r
        self._spalte = s
        # Farbe auf Blau
        self.color ="blue" 
        self.setStyleSheet("background-color: blue")
        # setzen der Attribute der Elternklasse QPushButton
        self.resize(50,50)
        self.move((r+1)*50, (s+1)*50)   
         

    # zusaetzliche Fkt fuer Quinto
    def KlickSlot(self):
        clkSender = self.sender()    #Sender holen
        clkReihe  = clkSender._reihe #Werte vom Sender
        clkSpalte = clkSender._spalte
        print('geklickt auf ' + str(clkReihe) + ' ' + str(clkSpalte))
        
        if clkSender.color == "blue":    
            clkSender.setStyleSheet("background-color: red") 
            clkSender.color = "red"
            if clkReihe+1 < N:
                ui.matrix[clkReihe+1][clkSpalte].setStyleSheet("background-color: red")
                ui.matrix[clkReihe+1][clkSpalte].color = "red" 
            if clkReihe-1 >= 0:
                ui.matrix[clkReihe-1][clkSpalte].setStyleSheet("background-color: red") 
                ui.matrix[clkReihe-1][clkSpalte].color = "red" 
            if clkSpalte+1 < N:
                ui.matrix[clkReihe][clkSpalte+1].setStyleSheet("background-color: red")
                ui.matrix[clkReihe][clkSpalte+1].color = "red"  
            if clkSpalte-1 >= 0:
                ui.matrix[clkReihe][clkSpalte-1].setStyleSheet("background-color: red") 
                ui.matrix[clkReihe][clkSpalte-1].color = "red" 
        else:
            clkSender.setStyleSheet("background-color: blue") 
            clkSender.color = "blue" 
            if clkReihe+1 < N:
                ui.matrix[clkReihe+1][clkSpalte].setStyleSheet("background-color: blue")
                ui.matrix[clkReihe+1][clkSpalte].color = "blue" 
            if clkReihe-1 >= 0:
                ui.matrix[clkReihe-1][clkSpalte].setStyleSheet("background-color: blue") 
                ui.matrix[clkReihe-1][clkSpalte].color = "blue" 
            if clkSpalte+1 < N:
                ui.matrix[clkReihe][clkSpalte+1].setStyleSheet("background-color: blue")
                ui.matrix[clkReihe][clkSpalte+1].color = "blue"  
            if clkSpalte-1 >= 0: 
                ui.matrix[clkReihe][clkSpalte-1].setStyleSheet("background-color: blue")
                ui.matrix[clkReihe][clkSpalte-1].color = "blue"  
                
        if ui.checkGameOver():
            ui.lblStatus.setText('Game Over - Züge'+ str(ui.spielZugNr))
        else:
            ui.spielZugNr = ui.spielZugNr+1
            ui.lblStatus.setText( str(ui.spielZugNr)+'.Zug ')


class Game(QWidget):
    # List 
    #gameState = 0  # 0=noch was frei, 1 = X,  2=O  hat gewonnen, 3=alles belegt
    gameState = stateClass.FREI
    spielZugNr = 1
        
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Game, self).__init__()      
        self.initUI()
    
    def initUI(self): 
       
        # Instanziierung der Widgets          
        # Tupel fuer Reihen und Spalten Indizierung
        rangeReihenIndex  = range(N) #(0,1,2,3) 
        rangeSpaltenIndex = range(N)
        self.matrix = [[myQuintoButton(r,s,self,self) for s in range(N)] for r in range(N)] 
       
        for reihe in rangeReihenIndex:
          for spalte in rangeSpaltenIndex:
            #Signal und Slot verbinden
            self.matrix[reihe][spalte].clicked.connect(self.matrix[reihe][spalte].KlickSlot)
        
        self.lblStatus = QLabel("Quinto",self)        
        self.lblStatus.setGeometry(60, 350, 200, 50)
               
        #Fenster Konfigurieren
        self.setGeometry(20, 20, 400, 400)
        self.setWindowTitle('Quinto')
        self.show()
        
    def checkGameOver(self):
        #Alle Felder rot?
        for r in range(N):
          for s in range(N):
            if self.matrix[r][s].color == "blue":
                return False
        return True #kein blue mehr gefunden=> alles rot
            

if __name__ == '__main__':    
    
    app = QApplication(sys.argv)
    ui = Game()
    sys.exit(app.exec_())
