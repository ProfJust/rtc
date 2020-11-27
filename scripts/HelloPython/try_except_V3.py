#!/usr/bin/env python
# --- try_except_V3.py ------
# Version vom 20.09.2019 by OJ
# Fehlerbehandlung - Demo
# vgl. Willemer Kap. 7
#----------------------------------

eingabe = 0
inputOK = False

while not inputOK:
	try: 
		eingabe = input("Geben Sie eine Zahl ein! ")
		# built in function eval() => String 2 Int
		zahl = eingabe # py3 : eval(eingabe)  
		inputOK=True
		# Ausgabe als Integer Dezimalzahl
		print("Die Zahl war %d" % zahl)
				
	except:
		print(" Fehler bei der Eingabe. ")
		
print("Ende des Programms erreicht")
