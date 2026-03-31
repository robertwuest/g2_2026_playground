from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person:
    def __init__(
        self,
        vorname,
        nachname,
        date_of_birth,
        email,
        telefon,
        strassenname,
        strassennummer,
        plz,
        ort,
    ):
        self.vorname = vorname
        self.nachname = nachname
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        self.email = email
        self.telefon = telefon
        self.strassenname = strassenname
        self.strassennummer = strassennummer
        self.plz = plz
        self.ort = ort        

    def get_age(self) -> int:
        return relativedelta(datetime.now(), self.date_of_birth).years
