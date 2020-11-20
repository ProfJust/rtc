# oop01.py
class Person:
    name = "Florian"
    alter = 17
    _txt = "  "
    def __init__(self, text): 
        self._txt = text
        
    def reden(self):
        print(str(self._txt))
        
if __name__ == '__main__':
    Heinz = Person("Moin Moin ! ") # Instanzzierung mit Parametern
    Karl  = Person("Keine Lust") 
    
    Heinz.reden()    # Aufruf der Methode
    Karl.reden()
    