#!/usr/bin/env python
# BMI.py
# -----------------------------------
#  9.11.2020 by OJ
# -----------------------------------

def bmi(m, le):
    bmi = m/(le**2)
    return bmi


def bewertung(b, a):
    # Die Tabelle in einer konstanten Liste gespeichert (Tupel)
    matrix = ((19, 25, 35, 45, 55, 65),  # Alter Untergrenze Intervall
              (19, 20, 21, 22, 23, 24),  # Untergrenze BMI
              (24, 25, 26, 27, 28, 29))  # Obergrenze BMI
    i = 0
    while a >= matrix[0][i]:
        i += 1

    if i >= 1:
        i = i-1  # einen zuerueck

    # debug Ausgabe
    print("Alter ", a, "Index i ", i, "OG ", matrix[2][i], "UG ", matrix[1][i])

    if (b > matrix[2][i]):
        print(" =>Uebergewicht")
    elif (b < matrix[1][i]):
        print(" => Untergewicht")
    else:
        print(" => Normalgewicht")


def main():
    # seit Python3 mit eval(): str => int
    gewicht = eval(input("Geben Sie Ihr Gewicht in kg an \n"))
    laenge = eval(input("Geben Sie Ihre Koerpergroesse in m an \n"))
    alter = eval(input("Geben Sie Ihr Alter in Jahren an \n"))

    _bmi = bmi(gewicht, laenge)  # globale Variable
    print("BMI: ", _bmi)
    bewertung(_bmi, alter)


# ------------------------------------------------------
main()