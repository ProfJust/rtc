#!/usr/bin/env python
# --- ue01_dir_to_goal.py ------
# Version vom 11.10.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math


class clPose:
    def EingabePose(self):
        # --- Eingabe Pose ------
        eingabe = input(" Pose x ?  >:")  # str
        self.x = eval(eingabe)  # str -> Zahl
        eingabe = input(" Pose y ?  >:")
        self.y = eval(eingabe)
        eingabe = input(" Theta  ?  >:")
        self.theta = eval(eingabe)


class clGoal:
    def EingabeGoal(self):
        # --- Eingabe Goal ------
        eingabe = input(" Goal x ?  >:")  # str
        self.x = eval(eingabe)  # str -> Zahl
        eingabe = input(" Goal y ?  >:")
        self.y = eval(eingabe)


print(" Weg zum Ziel berechnen \n")
pose = clPose()
pose.EingabePose()

goal = clGoal()  # Instanz der Klasse clGoal() erstellen
goal.EingabeGoal()

# --- Berechne Strecke zum Ziel ----
_sx = goal.x - pose.x
_sy = goal.y - pose.y
0
# --- Berechne Winkel zum Ziel Weltkoordinaten ----
theta2goal = math.atan2(_sy, _sx)

# --- Berechne notwendigen DrehWinkel zum Ziel ----
theta2turn = pose.theta - theta2goal

# --- Berechne Abstand zum Ziel relativ zum Roboter----
dist2Goal = math.sqrt(_sy*_sy + _sx*_sx)

# --- Augabe des Ergebnisses ---
print(" Strecke zum Ziel:", _sx, _sy)
print(" abs. Winkel ", theta2goal,
      " Drehwinkel ", theta2turn,
      " und Distanz zum Ziel:", dist2Goal)
