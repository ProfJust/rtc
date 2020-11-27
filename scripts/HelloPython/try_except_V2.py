#!/usr/bin/env python
# --- try_except_V2.py ------
# Version vom 20.09.2019 by OJ
# Fehlerbehandlung - Demo
# vgl. Willemer Kap. 7
#----------------------------------

eingabe = 0
inputOK = False

while not inputOK:
	try: 
		eingabe = input("Geben Sie eine Zahl ein! (Als String) ")
		# built in function eval() => String 2 Int
		zahl = eval(eingabe)  
		inputOK=True
		# Ausgabe als Integer Dezimalzahl
		print("Die Zahl war %d" % zahl)
				
	except:
		print(" Fehler bei der Eingabe. ")
		
print("Ende des Programms erreicht")
