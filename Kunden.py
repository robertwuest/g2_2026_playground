from Person import Person
 
 
class Kunde(Person):
    def __init__(
        self,
        kunden_id,
        vorname,
        nachname,
        geburtstag,
        kontakt_information,
        adresse
    ):
        self.kunden_id = kunden_id
        super().__init__(
            vorname,
            nachname,
            geburtstag,
            kontakt_information,
            adresse
        )
 
    def anzeigen(self):
        print(f"Kunden-ID: {self.kunden_id}")
        print(f"Name: {self.vorname} {self.nachname}")
        print(f"E-Mail: {self.kontakt_information.email}")
        print(f"Telefon: {self.kontakt_information.telefon}")
        print(f"Adresse: {self.adresse.strassenname} {self.adresse.strassennummer}, {self.adresse.plz}, {self.adresse.ort}")
        print(f"Aktiv: {self.aktiv}")
 
    def deaktivieren(self):
        self.aktiv = False