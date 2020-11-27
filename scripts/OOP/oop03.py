#!/usr/bin/env python3
# oop03.py.py
# -----------------------------
class Kiste:
    anzahl = 0   # Statische Klassenvariable Anzahl der Instanzen

    def __init__(self):
        self._breite = 0    # hier jetzt privat=> _breite
        self._hoehe = 0
        self._tiefe = 0
        self._vol = -1
        Kiste.anzahl += 1  # Wert der Klassenvariable erhoehen

    def zeigeAnzahl():  # statische Methode
        print("Die Instanzanzahl ist jetzt :" + str(Kiste.anzahl))

    zeigeAnzahl = staticmethod(zeigeAnzahl)

    def setBreite(self, breite):
        if self._breite != breite:
            self._breite = breite
            self._vol = -1

    def getBreite(self):
        return self._breite

    # Property  (Getter, Setter)
    breite = property(getBreite, setBreite)

    def setHoehe(self, hoehe):
        if self._hoehe != hoehe:
            self._hoehe = hoehe
            self._vol = -1

    def setTiefe(self, tiefe):
        if self._tiefe != tiefe:
            self._tiefe = tiefe
            self._vol = -1

    def getVolumen(self):
        if (self._vol == -1):
            print("calc")
            self._vol = self._breite * self._hoehe * self._tiefe
        return self._vol


if __name__ == '__main__':
    # Instantziierung
    kiste = Kiste()

    Kiste.anzahl = 5  # setzen der Klassenvariable
    print("---", Kiste.anzahl)  # get ueber Klassen-Bezeichner
    print(kiste.anzahl)  # get ueber Objekt-Bezeichner

    # Instantzierung zweite Kiste => Anzahl +=1
    kiste2 = Kiste()
    print("---", Kiste.anzahl)

    # geht nicht
    kiste2.anzahl = 77
    print("---", Kiste.anzahl)

    # Propertys nutzen
    # kiste.breite = 5  # setter
    # print(kiste.breite)  # getter

    # Setter fuer die privaten Attribute
    # kiste.setBreite(2)
    # kiste.setHoehe(3)
    # kiste.setTiefe(4)

    print(kiste.getVolumen())
