from Autor import Autore

class Buch:
    def __init__(self, titel, autor: Autore , erscheinungsjahr, isbn, seitenanzahl):
        """Initialisiert ein neues Buch-Objekt."""
        self.titel = titel
        self.autor = autor.voller_name
        self.erscheinungsjahr = erscheinungsjahr
        self.isbn = isbn
        self.seitenanzahl = seitenanzahl
