#!/usr/bin/env python3
# oop01.py  Version vpm 20.11.20
# -------------------------
class Person:
    _name = " leer "
    _alter = 17

    def reden(self):
        print("RTC ist super!")

    def reden2(self, text):
        print(str(text))


class nochKeineLust:
    pass


if __name__ == '__main__':
    # Instanzzierung
    Obj1 = Person()
    # Aufruf der Methode
    Obj1.reden()
    Obj1.reden2("Moin Moin ! ")
