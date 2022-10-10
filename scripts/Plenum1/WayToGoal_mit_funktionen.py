#!/usr/bin/env python
# --- WayToGoal_mit_Funktionen.py ------
# Version vom 30.9.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math


def EingabePose():
    # --- Eingabe Pose ------
    eingabe = input(" Pose x ?  >:")  # str
    _x = eval(eingabe)  # str -> Zahl
    eingabe = input(" Pose y ?  >:")
    _y = eval(eingabe)
    eingabe = input(" Theta  ?  >:")
    _theta = eval(eingabe)
    # Liste aus lokalen Variablen übergeben
    return (_x, _y, _theta)


def EingabeGoal():
    # --- Eingabe Goal ------
    eingabe = input(" Goal x ?  >:")  # str
    _xg = eval(eingabe)  # str -> Zahl
    eingabe = input(" Goal y ?  >:")
    _yg = eval(eingabe)
    # Liste aus lokalen Variablen übergeben
    return (_xg, _yg)


print(" Weg zum Ziel berechnen \n")
x, y, theta = EingabePose()
xg, yg = EingabeGoal()

# --- Berechne Strecke zum Ziel ----
sx = xg-x
sy = yg-y

# --- Berechne Winkel zum Ziel ----
theta2Goal = math.atan2(sy, sx)

# --- Berechne Abstand zum Ziel ----
dist2Goal = math.sqrt(sy*sy + sx*sx)

# ---- Ausgabe ------
print(" Strecke zum Ziel:", sx, sy)
print(" Winkel ", theta2Goal, " und Distanz zum Ziel:", dist2Goal)
