#!/usr/bin/env python
# --- WayToGoal_mit_Funktionen.py ------
# Version vom 30.9.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math

# Erstellen einer Liste aus Variablen
x = 0
y = 0
theta = 0
pose = [x, y, theta]  # Initialisierung einer Liste

xg = 0
yg = 0
goal = [xg, yg]  # Initialisierung einer Liste


def EingabePose():
    # --- Eingabe Pose ------
    eingabe = input(" Pose x ?  >:")  # str
    _x = eval(eingabe)  # str -> Zahl
    eingabe = input(" Pose y ?  >:")
    _y = eval(eingabe)
    eingabe = input(" Theta  ?  >:")
    _theta = eval(eingabe)
    # Liste aus lokalen Variablen übergeben
    return [_x, _y, _theta]


def EingabeGoal():
    # --- Eingabe Goal ------
    eingabe = input(" Goal x ?  >:")  # str
    _xg = eval(eingabe)  # str -> Zahl
    eingabe = input(" Goal y ?  >:")
    _yg = eval(eingabe)
    # Liste aus lokalen Variablen übergeben
    return [_xg, _yg]


print(" Weg zum Ziel berechnen \n")
pose = EingabePose()
goal = EingabeGoal()

print("Goal", goal)
# --- Berechne Strecke zum Ziel ----
sx = goal[0] - pose[0]
sy = goal[1] - pose[1]

# --- Berechne Winkel zum Ziel ----
theta2Goal = math.atan2(sy, sx)

# --- Berechne Abstand zum Ziel ----
dist2Goal = math.sqrt(sy*sy + sx*sx)

# ---- Ausgabe ------
print(" Strecke zum Ziel:", sx, sy)
print(" Winkel ", theta2Goal, " und Distanz zum Ziel:", dist2Goal)
