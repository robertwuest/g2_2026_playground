class Autore:
    """Classe Autor"""

    def __init__(
        self,
        vorname,
        nachname,
        nationalitaet,
        geburtsjahr,
        lieblingsgenre,
        anzahl_buecher,
        todesjahr=None,
    ):
        self.vorname = vorname
        self.nachname = nachname
        self.nationalitaet = nationalitaet
        self.geburtsjahr = geburtsjahr
        self.todesjahr = todesjahr
        self.lieblingsgenre = lieblingsgenre
        self.anzahl_buecher = anzahl_buecher

    def buch_hinzufuegen(self, anzahl=1):
        self.anzahl_buecher += anzahl

    def ist_aktiv(self):
        return self.todesjahr is None

    def __str__(self):
        return f"{self.vorname} {self.nachname}"

    def __len__(self):
        """Books total"""
        self.anzahl_buecher

    def __lt__(self, other):
        """Confronts two author by the count of the books (<)"""
        return self.anzahl_buecher < other.anzahl_buecher

    def __gt__(self, other):
        """Confronts two author by the count of the books (>)"""
        return self.anzahl_buecher > other.anzahl_buecher
