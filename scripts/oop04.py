
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# oop03_statVar.py

class Schokofigur:
    # statische Variable fuer alle Objekte der Klasse gemeinsam
    schoko_gesamt = 0

    def __init__(self, name, gewicht):  # Konstruktor
        # Name der Klasse. Name der stat. Var
        Schokofigur.schoko_gesamt += gewicht
        self._gewicht = gewicht

        # Normale Variable
        self._bez = name

    def getBez(self):
        return self._bez

    def __str__(self):  # String-Ausgabe überladen
        myStr = (self._bez + " ist " +
                 str(self._gewicht) + " g schwer")
        return myStr


if __name__ == '__main__':
    objekt1 = Schokofigur('Weihnachtsmann', 200)
    objekt2 = Schokofigur("Osterei", 50)

    print(objekt2)
    print(objekt1.getBez())
    print(objekt1)
    print("Gesamtgewicht Schokolade: " + str(Schokofigur.schoko_gesamt))
