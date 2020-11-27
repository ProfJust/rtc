#!/usr/bin/env python3
# oop01.py  Version vpm 20.11.20
# -------------------------
class Person:
    _name = " leer "
    _alter = 99
    _txt = "  "

    # Konstruktor mit Parametern
    def __init__(self, name, alter, text):
        self._name = name
        self._alter = alter
        self._txt = text

    def reden(self):
        print(str(self._name) + ", " + str(self._alter) +
              "  Jahre, spricht: " + str(self._txt))

    def reden2(self, text):
        print(str(text))


if __name__ == '__main__':
    # Instanzzierung mit Parametern
    Obj1 = Person("Heinz", 68, "Moin Moin ! ")
    Obj2 = Person("Kevin", 17, "Null Bock Alter")

    Obj1.reden()    # Aufruf der Methode
    Obj2.reden()
