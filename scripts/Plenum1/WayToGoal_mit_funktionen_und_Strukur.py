#!/usr/bin/env python
# --- WayToGoal_mit_Funktionen.py ------
# Version vom 30.9.2021 by OJ
# Weg zum Ziel in der TurtleSim berechnen
# ---------------------------------------

# Import math Library wegen atan2()
import math


class clPose:
    # Erstellen einer Strukur über eine Klasse
    # hier Konstruktor nicht notwendig
    # def __init__(self, x, y, theta):
    #     self.x = x
    #     self.y = y
    #     self.theta = theta

    def EingabePose(self):
        # --- Eingabe Pose ------
        eingabe = input(" Pose x ?  >:")  # str
        self.x = eval(eingabe)  # str -> Zahl
        eingabe = input(" Pose y ?  >:")
        self.y = eval(eingabe)
        eingabe = input(" Theta  ?  >:")
        self.theta = eval(eingabe)


class clGoal:
    # hier Konstruktor nicht notwendig
    #  def __init__(self, x, y):
    #    self.x = x
    #    self.y = y

    def EingabeGoal(self):
        # --- Eingabe Goal ------
        eingabe = input(" Goal x ?  >:")  # str
        self.x = eval(eingabe)  # str -> Zahl
        eingabe = input(" Goal y ?  >:")
        self.y = eval(eingabe)


print(" Weg zum Ziel berechnen \n")
pose = clPose()  # Instanzieren
pose.EingabePose()  # Fkt. der Klasse aufrufen

goal = clGoal()
goal.EingabeGoal()

# --- Berechne Strecke zum Ziel ----
sx = goal.x - pose.x
sy = goal.y - pose.y

# --- Berechne Winkel zum Ziel ----
theta2Goal = math.atan2(sy, sx)

# --- Berechne Abstand zum Ziel ----
dist2Goal = math.sqrt(sy*sy + sx*sx)

# ---- Ausgabe ------
print(" Strecke zum Ziel:", sx, sy)
print(" Winkel ", theta2Goal, " und Distanz zum Ziel:", dist2Goal)
