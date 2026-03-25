class Kunde:
    def __init__(self, kunden_id, vorname, nachname, email, telefon, adresse):
        self.kunden_id = kunden_id
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.telefon = telefon
        self.adresse = adresse
        self.aktiv = True

    def anzeigen(self):
        print(f"Kunden-ID: {self.kunden_id}")
        print(f"Name: {self.vorname} {self.nachname}")
        print(f"E-Mail: {self.email}")
        print(f"Telefon: {self.telefon}")
        print(f"Adresse: {self.adresse}")
        print(f"Aktiv: {self.aktiv}")

    def deaktivieren(self):
        self.aktiv = False


class Buchausleihe:
    def __init__(self, ausleihe: "Ausleihe", kunde: "Kunde"):
        self.kunde = kunde
        self.ausleihe = ausleihe

    def kunde_leiht_aus(self):
        print(f"{self.Kunde.name} leiht aus {self.ausleihe}.")
