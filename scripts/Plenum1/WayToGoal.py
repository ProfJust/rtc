#!/usr/bin/env python
# --- WayToGoal.py ------
# Version vom 30.9.2021 by OJ
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
theta2Goal = math.atan2(sy, sx)

# --- Berechne notwendigen DrehWinkel zum Ziel ----
theta2Turn = theta - theta2Goal

# --- Berechne Abstand zum Ziel relativ zum Roboter----
dist2Goal = math.sqrt(sy*sy + sx*sx)

print(" Strecke zum Ziel:", sx, sy)
print(" abs. Winkel ", theta2Goal,  " Drehwinkel ", theta2Turn, " und Distanz zum Ziel:", dist2Goal)
