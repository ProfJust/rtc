# !/usr/bin/env python
# BMI.py
# -----------------------------------------
# 10.10.2022 by OJ
# -----------------------------------------

def bmi(m, le):
    bmi = m/(le*le)
    return bmi


def bewertung(b):
    if (b > 25):
        print(" => Uebergewicht ")
    elif (b < 18.5):
        print(" => Untergewicht")
    else:
        print(" => Normalgewicht")
        

def main():
    eingabe = input("Geben Sie Ihr Gewicht in kg an \n")
    gewicht = eval(eingabe)
    eingabe = input("Geben Sie Ihre Koerpergroesse in m an \n")
    laenge = eval(eingabe)
    # globale Variable werden oft durch "_" gekenzeichnet
    _bmi = bmi(gewicht, laenge)
    print("BMI: %f " % _bmi)
    bewertung(_bmi)

    
# ------------------------------------------------------
main()
