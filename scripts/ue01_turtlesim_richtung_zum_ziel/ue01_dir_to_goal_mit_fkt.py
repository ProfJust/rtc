#!/usr/bin/env python
# --- ue01_dir_to_goal.py ------
# Version vom 11.10.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math


def EingabePose():
    # --- Eingabe Pose ------
    eingabe = input(" Pose x ?  >:")  # str
    x = eval(eingabe)  # str -> Zahl
    eingabe = input(" Pose y ?  >:")
    y = eval(eingabe)
    eingabe = input(" Theta  ?  >:")
    theta = eval(eingabe)
    return(x, y, theta)


def EingabeGoal():
    # --- Eingabe Goal ------
    eingabe = input(" Goal x ?  >:")  # str
    xg = eval(eingabe)  # str -> Zahl
    eingabe = input(" Goal y ?  >:")
    yg = eval(eingabe)
    return (xg, yg)


print(" Weg zum Ziel berechnen \n")
# Funktion aufrufen und Ergebnis in globale Var speichern
_x, _y, _theta = EingabePose()
pose = [_x, _y, _theta]  # Initialisierung einer Liste
_xg, _yg = EingabeGoal()

# --- Berechne Strecke zum Ziel ----
_sx = _xg-_x
_sy = _yg-_y

# --- Berechne Winkel zum Ziel Weltkoordinaten ----
theta2goal = math.atan2(_sy, _sx)

# --- Berechne notwendigen DrehWinkel zum Ziel ----
theta2turn = _theta - theta2goal

# --- Berechne Abstand zum Ziel relativ zum Roboter----
dist2Goal = math.sqrt(_sy*_sy + _sx*_sx)

# --- Augabe des Ergebnisses ---
print(" Strecke zum Ziel:", _sx, _sy)
print(" abs. Winkel ", theta2goal,
      " Drehwinkel ", theta2turn,
      " und Distanz zum Ziel:", dist2Goal)
