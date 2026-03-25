from Autor import Autore

class Buch:
    def __init__(self, titel, autor: Autore , erscheinungsjahr, isbn, seitenanzahl, stilrichtung):
        """Initialisiert ein neues Buch-Objekt."""
        self._titel = titel
        self._autor = autor
        self._erscheinungsjahr = erscheinungsjahr
        self._isbn = isbn
        self._seitenanzahl = seitenanzahl
        self._stilrichtung = stilrichtung

    def setTitel(self, titel):
        self._titel = titel
    def getTitel(self):
        return self._titel
    titel = property(getTitel, setTitel)

    def setAutor(self, autor):
        self._autor = autor
    def getAutor(self):
        return self._autor
    autor = property(getAutor, setAutor)
    
    def setErscheinungsjahr(self, erscheinungsjahr):
        self._erscheinungsjahr = erscheinungsjahr
    def getErscheinungsjahr(self):
        return self._erscheinungsjahr
    erscheinungsjahr = property(getErscheinungsjahr, setErscheinungsjahr)

    def setIsbn(self, isbn):
        self._isbn = isbn
    def getIsbn(self):
        return self._isbn
    isbn = property(getIsbn, setIsbn)

    def setSeitenanzahl(self, seitenanzahl):
        self._seitenanzahl = seitenanzahl
    def getSeitenanzahl(self):
        return self._seitenanzahl
    seitenanzahl = property(getSeitenanzahl, setSeitenanzahl)

    def setStilrichtung(self, stilrichtung):
        self._stilrichtung = stilrichtung
    def getStilrichtung(self):
        return self._stilrichtung
    stilrichtung = property(getStilrichtung, setStilrichtung)

    def __str__(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, Erscheinungsjahr: {self.erscheinungsjahr}, ISBN: {self.isbn}, Seitenzahl: {self.seitenanzahl}"
    
    def __gt__(self, seitenanzahl):
        return self.seitenanzahl > seitenanzahl
    
    def __eq__(self, jahr):
        return self.erscheinungsjahr == jahr
    
class StilrichtungBuch:
    def __init__(self, stilrichtung):
        self.stilrichtung = stilrichtung

class Sachbuch(StilrichtungBuch):
    def __init__(self, stilrichtung):
        super().__init__("Sachbuch")

class Roman(StilrichtungBuch):
    def __init__(self, stilrichtung):
        super().__init__("Roman")

class Thriller(StilrichtungBuch):
    def __init__(self, stilrichtung):
        super().__init__("Thriller")

class Kochbuch(StilrichtungBuch):
    def __init__(self, stilrichtung):
        super().__init__("Kochbuch")

class Kinderbücher(StilrichtungBuch):
    def __init__(self, stilrichtung):
        super().__init__("Kinderbücher")     
