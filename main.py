from Kunden import Kunde
from Mitarbeiter import Mitarbeiter, Kundenbetreuung

mitarbeiter_1 = Mitarbeiter(1232, "Alice", 30, "Bibliothekarin")
mitarbeiter_2 = Mitarbeiter(1233, "Bob", 25, "Ferienjöbbler")
mitarbeiter_3 = Mitarbeiter(1234, "Charlie", 35, "Sekretär")

kunde_1 = Kunde(
    1,
    "Max",
    "Mustermann",
    "max.mustermann@example.com",
    "123456789",
    "Musterstraße 1, 12345 Musterstadt",
)
kunde_2 = Kunde(
    2,
    "Erika",
    "Musterfrau",
    "erika.musterfrau@example.com",
    "987654321",
    "Musterstraße 2, 12345 Musterstadt",
)

betreuung_1 = Kundenbetreuung(mitarbeiter_3, kunde_1)
betreuung_2 = Kundenbetreuung(mitarbeiter_2, kunde_2)

print(mitarbeiter_1 == mitarbeiter_2)
print(mitarbeiter_1 == mitarbeiter_1)
print(mitarbeiter_1)
