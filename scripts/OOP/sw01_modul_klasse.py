#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sw01_modul_klasse.py

import sys

# Hier wird nur eine Klasse deklariert


class Schokofigur:
    # statische Variable fuer alle Objekte der Klasse gemeinsam
    schoko_gesamt = 0

    def __init__(self, name, gewicht):  # Konstruktor
        # Name der Klasse. Name der stat. Var
        Schokofigur.schoko_gesamt += gewicht
        # Normale Variable
        self._bez = name

    def getBez(self):
        return self._bez

    def __str__(self):  # String-Ausgabe überladen
        myStr = (self._bez + " ist " 
                 + str(Schokofigur.schoko_gesamt) +" g schwer")
        return myStr

