#!/usr/bin/env python
# --- try_except.py ------
# Version vom 20.09.2019 by OJ
# Fehlerbehandlung - Demo
# vgl. Willemer Kap. 7
#----------------------------------

eingabe = 0
eingabe = input("Geben Sie eine Zahl ein! ")

# built in function eval() => String 2 Int
# nur python3: zahl = eval(eingabe)  

zahl = eingabe

# Ausgabe als Dezimalzahl
print("Die Zahl war %d" % zahl)


