class Mitarbeiter:
    def __init__(self, name, alter, position):
        self.name = name
        self.alter = alter
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.alter} Jahre alt, Position: {self.position}"