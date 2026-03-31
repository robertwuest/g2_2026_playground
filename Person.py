from datetime import datetime
from dateutil.relativedelta import relativedelta

class Adresse:
    def __init__(
            self,
            strassenname,
            strassennummer,
            plz,
            ort,
    ):
        self.strassenname = strassenname,
        self.strassennummer = strassennummer,
        self.plz = plz,
        self.ort = ort,

class KontaktInformation:
    def __init__(
        self,
        email,
        telefon,
    ):
        self.email = email,
        self.telefon = telefon,

class Person:
    def __init__(
        self,
        vorname,
        nachname,
        geburtstag,
        kontakt_information: KontaktInformation,
        adresse: Adresse
    ):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtstag = datetime.strptime(geburtstag, '%Y-%m-%d')
        self.kontakt_information = kontakt_information
        self.adresse = adresse

    def get_age(self) -> int:
        return relativedelta(datetime.now(), self.geburtstag).years
