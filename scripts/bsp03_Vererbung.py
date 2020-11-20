class PersonKl:  #Basisklasse
    
    # Konstruktor 
    def __init__(self, vorname, nachname, geburtsdatum):
        #setzen der private Attribute
        self._vorname = vorname
        self._nachname = nachname
        self._geburtsdatum = geburtsdatum
        
    # Funnktion der Basisklasse  
    # Wenn eine Klasse eine Methode mit dem Namen __str__ enthaelt,
    # dann ueberschreibt diese das voreingestellte Verhalten von
    # Pythons eingebauter str Funktion. Wichtig fuer print()
    
    def __str__(self):
        ret = "Person " + self._vorname + " " + self._nachname
        ret += ", " + self._geburtsdatum
        return  ret
        
class AngestellterKl(PersonKl): #von PersonKl Abgeleitete Klasse    

    def __init__(self, vorname, nachname, geburtsdatum, personalnummer):
        # Aufruf des Konstruktors der Basisklasse
        PersonKl.__init__(self, vorname, nachname, geburtsdatum)
        # alternativ:
        # super().__init__(vorname, nachname, geburtsdatum)
        
        # zusaetzliches Attribut der abgel. Klasse
        self.__personalnummer = personalnummer
    
    # Ueberschreiben der Funnktion __str__ der Basisklasse 
    # Ergaenze Personalnummer
    def __str__(self):        
        #return super().__str__() + " " + self.__personalnummer
        return PersonKl.__str__(self) + " " + "   Angestellter " + self.__personalnummer
    
    
if __name__ == "__main__":
    x = AngestellterKl("Mueller", "Manfred", "09.08.1969", "007")
    print(x)