#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sw02_modul_klasse_import.py

# from 'Dateiname' ohne .py import Klasse aus der Datei
from sw01_modul_klasse import Schokofigur


if __name__ == '__main__':
    objekt1 = Schokofigur('Weihnachtsmann', 200)
    objekt2 = Schokofigur("Osterei", 50)
    print(objekt2)
    print(objekt1.getBez())
    print("Geamstgewicht Schokolade: " + str(Schokofigur.schoko_gesamt))
