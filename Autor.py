class Autore:
    """Klasse für Autoren (basierend auf dem Kapitel-Stil von Pintone)"""

    def __init__(
        self,
        vorname="",
        nachname="",
        nationalitaet="",
        geburtsjahr=0,
        todesjahr=None,
        lieblingsgenre="",
        anzahl_buecher=0,
    ):
        """Konstruktor - initialisiert einen Autor"""
        self._vorname = vorname
        self._nachname = nachname
        self._nationalitaet = nationalitaet
        self._geburtsjahr = geburtsjahr
        self._todesjahr = todesjahr
        self._lieblingsgenre = lieblingsgenre
        self._anzahl_buecher = anzahl_buecher

    # Getter und Setter Methoden
    def set_vorname(self, vorname):
        self._vorname = vorname

    def get_vorname(self):
        return self._vorname

    def set_nachname(self, nachname):
        self._nachname = nachname

    def get_nachname(self):
        return self._nachname

    def set_nationalitaet(self, nationalitaet):
        self._nationalitaet = nationalitaet

    def get_nationalitaet(self):
        return self._nationalitaet

    def set_geburtsjahr(self, jahr):
        if jahr < 0:
            raise ValueError("Geburtsjahr kann nicht negativ sein!")
        self._geburtsjahr = jahr

    def get_geburtsjahr(self):
        return self._geburtsjahr

    def set_todesjahr(self, jahr):
        if jahr and jahr < self._geburtsjahr:
            raise ValueError("Todesjahr kann nicht vor Geburtsjahr sein!")
        self._todesjahr = jahr

    def get_todesjahr(self):
        return self._todesjahr

    def set_lieblingsgenre(self, genre):
        self._lieblingsgenre = genre

    def get_lieblingsgenre(self):
        return self._lieblingsgenre

    def set_anzahl_buecher(self, anzahl):
        if anzahl < 0:
            raise ValueError("Anzahl Bücher kann nicht negativ sein!")
        self._anzahl_buecher = anzahl

    def get_anzahl_buecher(self):
        return self._anzahl_buecher

    # Property Definitionen (wie im Kapitel 1.9)
    vorname = property(get_vorname, set_vorname)
    nachname = property(get_nachname, set_nachname)
    nationalitaet = property(get_nationalitaet, set_nationalitaet)
    geburtsjahr = property(get_geburtsjahr, set_geburtsjahr)
    todesjahr = property(get_todesjahr, set_todesjahr)
    lieblingsgenre = property(get_lieblingsgenre, set_lieblingsgenre)
    anzahl_buecher = property(get_anzahl_buecher, set_anzahl_buecher)

    # Methoden
    def vollstaendiger_name(self):
        """Gibt den vollständigen Namen zurück"""
        return f"{self._vorname} {self._nachname}"

    def alter_bei_tod(self):
        """Berechnet das Alter beim Tod (falls verstorben)"""
        if self._todesjahr:
            return self._todesjahr - self._geburtsjahr
        return None

    def ist_aktiv(self):
        """Prüft ob der Autor noch lebt"""
        return self._todesjahr is None

    def info(self):
        """Gibt alle Informationen über den Autor aus"""
        print(f"Autor: {self.vollstaendiger_name()}")
        print(f"  Nationalität: {self._nationalitaet}")
        print(f"  Geburtsjahr: {self._geburtsjahr}")
        if self._todesjahr:
            print(f"  Todesjahr: {self._todesjahr} (Alter: {self.alter_bei_tod()})")
        else:
            print("  Status: Lebend")
        print(f"  Lieblingsgenre: {self._lieblingsgenre}")
        print(f"  Anzahl Bücher: {self._anzahl_buecher}")
        print()

    def buch_hinzufuegen(self, anzahl=1):
        """Fügt Bücher zur Anzahl hinzu"""
        self._anzahl_buecher += anzahl

    def __del__(self):
        """Destruktor (optional)"""
        print(f"Autor {self.vollstaendiger_name()} wird gelöscht...")

    def voller_name(self):
        """Gibt den Vor- und Nachnamen als einen String zurück."""
        return f"{self._vorname} {self._nachname}"

# 📚 **Beispiel: 5 Autoren instanziieren**
print("=" * 50)
print("BEISPIEL 1: 5 AUTOREN INSTANZIIEREN")
print("=" * 50)

# Autoren erstellen (Instanzen der Klasse Autore)
autor1 = Autore("Johann Wolfgang", "von Goethe", "Deutsch", 1749, 1832, "Drama", 30)
autor2 = Autore("Franz", "Kafka", "Österreichisch", 1883, 1924, "Roman", 12)
autor3 = Autore("Hermann", "Hesse", "Deutsch", 1877, 1962, "Roman", 25)
autor4 = Autore("Thomas", "Mann", "Deutsch", 1875, 1955, "Roman", 18)
autor5 = Autore("Friedrich", "Schiller", "Deutsch", 1759, 1805, "Drama", 22)

# Autoren in einer Liste speichern
autoren_liste = [autor1, autor2, autor3, autor4, autor5]

# Alle Autoren anzeigen
for autor in autoren_liste:
    autor.info()


# 🔍 **Beispiel 2: Abfragen (wie SQL-Abfragen)**
print("\n" + "=" * 50)
print("BEISPIEL 2: ABFRAGEN (WIE SQL)")
print("=" * 50)

# 1. Alle deutschen Autoren anzeigen
print("\n1. DEUTSCHE AUTOREN:")
deutsche_autoren = [a for a in autoren_liste if a.nationalitaet == "Deutsch"]
for autor in deutsche_autoren:
    print(f"  - {autor.vollstaendiger_name()}")

# 2. Autoren nach 1800 geboren
print("\n2. AUTOREN GEBOREN NACH 1800:")
nach_1800 = [a for a in autoren_liste if a.geburtsjahr > 1800]
for autor in nach_1800:
    print(f"  - {autor.vollstaendiger_name()} ({autor.geburtsjahr})")

# 3. Autoren mit mehr als 20 Büchern
print("\n3. AUTOREN MIT >20 BÜCHERN:")
viel_buecher = [a for a in autoren_liste if a.anzahl_buecher > 20]
for autor in viel_buecher:
    print(f"  - {autor.vollstaendiger_name()}: {autor.anzahl_buecher} Bücher")

# 4. Autoren nach Genre suchen
print("\n4. AUTOREN MIT GENRE 'ROMAN':")
roman_autoren = [a for a in autoren_liste if a.lieblingsgenre == "Roman"]
for autor in roman_autoren:
    print(f"  - {autor.vollstaendiger_name()} ({autor.lieblingsgenre})")

# 5. Statistik nach Nationalität
print("\n5. STATISTIK NACH NATIONALITÄT:")
nationalitaeten = {}
for autor in autoren_liste:
    nat = autor.nationalitaet
    if nat not in nationalitaeten:
        nationalitaeten[nat] = {"anzahl": 0, "buecher_summe": 0}
    nationalitaeten[nat]["anzahl"] += 1
    nationalitaeten[nat]["buecher_summe"] += autor.anzahl_buecher

for nat, stats in nationalitaeten.items():
    durchschnitt = stats["buecher_summe"] / stats["anzahl"]
    print(f"  {nat}: {stats['anzahl']} Autoren, Ø {durchschnitt:.1f} Bücher")
