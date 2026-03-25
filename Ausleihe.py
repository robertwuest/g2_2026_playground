from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Kunden import Kunde
    from Mitarbeiter import Mitarbeiter


class Ausleihe:
    def __init__(
        self,
        ausleihe_id: int,
        buch_titel: str,
        mitglied_name: str,
        ausleihdatum: date,
        rueckgabedatum: date = None,
    ):
        self.ausleihe_id = ausleihe_id
        self.buch_titel = buch_titel
        self.mitglied_name = mitglied_name
        self.ausleihdatum = ausleihdatum
        self.rueckgabedatum = rueckgabedatum
        self.zurueckgegeben = False

    def __init__(self, kunde: Kunde, mitarbeiter: Mitarbeiter):
        self.kunde = kunde
        self.mitarbeiter = mitarbeiter

    def zurueckgeben(self, datum: date):
        self.rueckgabedatum = datum
        self.zurueckgegeben = True

    def __str__(self):
        status = "zurückgegeben" if self.zurueckgegeben else "ausgeliehen"
        return f"Ausleihe #{self.ausleihe_id} | {self.buch_titel} | {self.mitglied_name} | {status}"
