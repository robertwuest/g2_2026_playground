from Kunden import Kunde
from Person import Person


class Mitarbeiter(Person):
    def __init__(self, id, name, alter, position):
        super().__init__(name, alter)
        self.mitarbeiter_id = id
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.alter} Jahre alt, Position: {self.position}"

    def __eq__(self, mitarbeiter2: "Mitarbeiter"):
        if self.mitarbeiter_id == mitarbeiter2.mitarbeiter_id:
            return True
        else:
            return False


class Kundenbetreuung:
    def __init__(self, mitarbeiter, kunde: Kunde):
        self.mitarbeiter = mitarbeiter
        self.kunde = kunde

    def __str__(self):
        return f"{self.mitarbeiter.name} betreut {self.kunde}."
