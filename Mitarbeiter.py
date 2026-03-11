from Kunden import Kunde

class Mitarbeiter:
    def __init__(self, name, alter, position):
        self.name = name
        self.alter = alter
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.alter} Jahre alt, Position: {self.position}"
    
class Kundenbetreuung:
    def __init__(self, mitarbeiter, kunde: Kunde):
        self.mitarbeiter = mitarbeiter
        self.kunde = kunde

    def betreue_kunden(self):
        print(f"{self.mitarbeiter.name} betreut {self.kunde}.")