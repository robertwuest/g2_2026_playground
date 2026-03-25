from Ausleihe import Ausleihe
from Person import Person
 
 
class Kunde(Person):
    def __init__(
        self,
        kunden_id,
        vorname,
        nachname,
        geburtstag,
        email,
        telefon,
        strassenname,
        strassennummer,
        plz,
        ort,
    ):
        self.kunden_id = kunden_id
        super().__init__(
            vorname,
            nachname,
            geburtstag,
            email,
            telefon,
            strassenname,
            strassennummer,
            plz,
            ort,
        )
 
    def anzeigen(self):
        print(f"Kunden-ID: {self.kunden_id}")
        print(f"Name: {self.vorname} {self.nachname}")
        print(f"E-Mail: {self.email}")
        print(f"Telefon: {self.telefon}")
        print(f"Adresse: {self.adresse}")
        print(f"Aktiv: {self.aktiv}")
 
    def deaktivieren(self):
        self.aktiv = False
 
