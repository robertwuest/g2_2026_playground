from Kunden import Kunde
from Mitarbeiter import Mitarbeiter, Kundenbetreuung, Position
from Person import Adresse, KontaktInformation


id1, firstname1, name1, date_of_birth1, position1 = 1230, "Alice", "Aliceson", "2001-01-28", "Bibliothekarin"
id2, firstname2, name2, date_of_birth2, position2 = 1231, "Bob", "Gustavson", "2005-12-26", Position.SECRETARY
id3, firstname3, name3, date_of_birth3, position3 = 1232, "Charlie", "Peterson", "1992-12-26", Position.CUSTOMER_SERVICE
stub_address = Adresse("stub street", 1, 8000, "stub_location")
stub_contact_information = KontaktInformation("email@stub.com", "+1234567890")

employee1 = Mitarbeiter(id1, firstname1, name1, date_of_birth1, position1, stub_contact_information, stub_address)
employee2 = Mitarbeiter(id2, firstname2, name2, date_of_birth2, position2, stub_contact_information, stub_address)
employee3 = Mitarbeiter(id3, firstname3, name3, date_of_birth3, position3, stub_contact_information, stub_address)

id4, firstname4, name4, date_of_birth4 = 1, "Bruce", "Bruceson", "2001-01-28"
id5, firstname5, name5, date_of_birth5 = 2, "Frederik", "Frederikson", "2001-01-28"

customer_1 = Kunde(
    id4, firstname4, name4, date_of_birth4, stub_contact_information, stub_address
)

customer_2 = Kunde(
    id5, firstname5, name5, date_of_birth5, stub_contact_information, stub_address
)

betreuung_1 = Kundenbetreuung(employee2, customer_1)
betreuung_2 = Kundenbetreuung(employee3, customer_2)

print(employee1 == employee2)
print(employee1 == employee1)
print(employee1)
