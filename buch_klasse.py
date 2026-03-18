from Autor import Autore

class Buch:
    def __init__(self, titel, autor: Autore , erscheinungsjahr, isbn, seitenanzahl):
        """Initialisiert ein neues Buch-Objekt."""
        self._titel = titel
        self._autor = autor.voller_name
        self._erscheinungsjahr = erscheinungsjahr
        self._isbn = isbn
        self._seitenanzahl = seitenanzahl

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

    def setSeitenzahl(self, seitenzahl):
        self._seitenanzahl = seitenzahl
    def getSeitenzahl(self):
        return self._seitenanzahl
    seitenanzahl = property(getSeitenzahl, setSeitenzahl)

    def __str__(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, Erscheinungsjahr: {self.erscheinungsjahr}, ISBN: {self.isbn}, Seitenzahl: {self.seitenanzahl}"