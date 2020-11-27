#!/usr/bin/env python
# ------------------------------------------------
# --- global_and_local_Var_V2.py ----
# Version vom 19.09.2019 by OJ
# -------------------------------------------------
# WHS - Campus Bocholt - ROP
# globale Variablen - Demo
# -------------------------------------------------

# globale Variable
summe = 2


# Funktion
def summiere(upto):
    local_summe = 0
    for i in range(1, upto+1, 1):
        local_summe += i
    return local_summe


summiere(3)   # Rueckgabe nicht genutzt
print(summe)  # =>2

summe = summiere(3)
print(summe)  # =>6
