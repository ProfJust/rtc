#!/usr/bin/env python
# bsp01_WHILE.py
# -----------------------------------
# 30.09.2021 by OJ
# -----------------------------------

# ---- Variablen ----
i = 0

while(i <= 9):
    print("Zahl {0:02d}".format(i),
          "Zahl {0:03d}".format(i**2),
          "Zahl {0:04d}".format(i**3))
    i += 1  # i++ gibt es nicht!

print("Schleife zu Ende")




