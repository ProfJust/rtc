#!/usr/bin/env python
# ------------------------------------------------
# --- global_and_local_Var.py ----
# Version vom 19.09.2019 by OJ
# -------------------------------------------------
#  WHS - Campus Bocholt - ROP
# globale Variablen - Demo
# -------------------------------------------------

# globale Variable
summe = 0


# Funktion
def summiere(upto):
    for i in range(1, upto+1, 1):
        summe += 1  # Zugriff auf globale Variable => Error


summiere(10)
print(summe)
