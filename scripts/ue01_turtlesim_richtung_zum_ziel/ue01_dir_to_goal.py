#!/usr/bin/env python
# --- ue01_dir_to_goal.py ------
# Version vom 11.10.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math

print(" Weg zum Ziel berechnen \n")
# --- Eingabe Pose ------
eingabe = input(" Pose x ?  >:")  # str
x = eval(eingabe)  # str -> Zahl
eingabe = input(" Pose y ?  >:")
y = eval(eingabe)
eingabe = input(" Theta  ?  >:")
theta = eval(eingabe)

# --- Eingabe Goal ------
eingabe = input(" Goal x ?  >:")  # str
xg = eval(eingabe)  # str -> Zahl
eingabe = input(" Goal y ?  >:")
yg = eval(eingabe)

# --- Berechne Strecke zum Ziel ----
sx = xg-x
sy = yg-y

# --- Berechne Winkel zum Ziel Weltkoordinaten ----
theta2goal = math.atan2(sy, sx)

# --- Berechne notwendigen DrehWinkel zum Ziel ----
theta2turn = theta - theta2goal

# --- Berechne Abstand zum Ziel relativ zum Roboter----
dist2Goal = math.sqrt(sy*sy + sx*sx)

# --- Augabe des Ergebnisses ---
print(" Strecke zum Ziel:", sx, sy)
print(" abs. Winkel ", theta2goal,
      " Drehwinkel ", theta2turn,
      " und Distanz zum Ziel:", dist2Goal)


