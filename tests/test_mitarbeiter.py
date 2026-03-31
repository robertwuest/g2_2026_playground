from unittest import TestCase
from freezegun import freeze_time

from Mitarbeiter import Mitarbeiter, Position
from Person import Adresse, KontaktInformation

class TestMitarbeiter(TestCase):

    def setUp(self):
        super().setUp()
        id1, firstname1, name1, date_of_birth1, position1 = 1230, "Alice", "Aliceson", "2001-01-28", "Bibliothekarin"
        
        self.stub_address = Adresse("stub street", 1, 8000, "stub_location")
        self.stub_contact_information = KontaktInformation("email@stub.com", "+1234567890")
        self.employee1 = Mitarbeiter(id1, firstname1, name1, date_of_birth1, position1, self.stub_contact_information, self.stub_address)
    
    def test_employee_to_str(self):
        self.assertEqual(str(self.employee1), "Alice Aliceson, Ist aufgrund seiner Position gefühlt 25 Jahre alt, Position: Bibliothekarin")

    def test_employee_for_equality(self):
        id2, firstname2, name2, date_of_birth2, position2 = 1230, "Bob", "Gustavson", "2005-12-26", Position.SECRETARY
        employee2_with_same_id_like_employee1 = Mitarbeiter(id2, firstname2, name2, date_of_birth2, position2, self.stub_contact_information, self.stub_address)
        
        self.assertTrue(self.employee1 == employee2_with_same_id_like_employee1, f"{self.employee1} should not be equal to {employee2_with_same_id_like_employee1} due to identical values in field id.")

    def test_employee_inequality(self):
        id2, firstname2, name2, date_of_birth2, position2 = 1231, "Bob", "Gustavson", "2005-12-26", Position.SECRETARY
        employee2 = Mitarbeiter(id2, firstname2, name2, date_of_birth2, position2, self.stub_contact_information, self.stub_address)
        
        self.assertNotEqual(self.employee1, employee2, f"{self.employee1} should not be equal to {employee2} due to different values in field id.")

    @freeze_time("2026-03-30")
    def test_employee_age_by_position(self):
        # assign
        expected_age_employee1 = 25
        expected_age_employee2 = 21
        expected_age_employee3 = 38
        expected_age_employee4 = 26
        expected_age_employee5 = 40
        
        id2, firstname2, name2, date_of_birth2, position2 = 1231, "Bob", "Gustavson", "2005-12-26", Position.SECRETARY
        id3, firstname3, name3, date_of_birth3, position3 = 1232, "Charlie", "Peterson", "1992-12-26", Position.CUSTOMER_SERVICE
        id4, firstname4, name4, date_of_birth4, position4 = 1233, "Delta", "Hellsingson", "2009-05-17", Position.DEV
        id5, firstname5, name5, date_of_birth5, position5 = 1234, "Epsilon", "Borgson", "1975-10-08", Position.MANAGER
        
        employee2 = Mitarbeiter(id2, firstname2, name2, date_of_birth2, position2, self.stub_contact_information, self.stub_address)
        employee3 = Mitarbeiter(id3, firstname3, name3, date_of_birth3, position3, self.stub_contact_information, self.stub_address)
        employee4 = Mitarbeiter(id4, firstname4, name4, date_of_birth4, position4, self.stub_contact_information, self.stub_address)
        employee5 = Mitarbeiter(id5, firstname5, name5, date_of_birth5, position5, self.stub_contact_information, self.stub_address)
        
        # act
        actual_age_employee1 = self.employee1.get_age()
        actual_age_employee2 = employee2.get_age()
        actual_age_employee3 = employee3.get_age()
        actual_age_employee4 = employee4.get_age()
        actual_age_employee5 = employee5.get_age()

        # assert
        self.assertEqual(expected_age_employee1, actual_age_employee1, f"Employee 1 {self.employee1} should be {expected_age_employee1} but is {actual_age_employee1}.")
        self.assertEqual(expected_age_employee2, actual_age_employee2, f"Employee 2 {employee2} should be {expected_age_employee2} but is {actual_age_employee2}.")
        self.assertEqual(expected_age_employee3, actual_age_employee3, f"Employee 3 {employee3} should be {expected_age_employee3} but is {actual_age_employee3}.")
        self.assertEqual(expected_age_employee4, actual_age_employee4, f"Employee 4 {employee4} should be {expected_age_employee4} but is {actual_age_employee4}.")
        self.assertEqual(expected_age_employee5, actual_age_employee5, f"Employee 5 {employee5} should be {expected_age_employee5} but is {actual_age_employee5}.")
    
    @freeze_time("2026-03-30")
    def test_unrealistic_manager_age(self):    
        expected_age_employee6 = 9
        id6, firstname6, name6, date_of_birth6, position6 = 1235, "Magnus", "Magnusson", "2016-11-28", Position.MANAGER
        employee6 = Mitarbeiter(id6, firstname6, name6, date_of_birth6, position6, self.stub_contact_information, self.stub_address)

        actual_age = employee6.get_age()

        self.assertFalse(actual_age <= 0)
        self.assertEqual(expected_age_employee6, actual_age, f"Employee 6 {employee6} should be {expected_age_employee6} but is {actual_age}.")

    def test_raise_value_error_when_creating_employee_with_date_of_birth_value_of_bad_formatted(self):
        id2, firstname2, name2, date_of_birth2, position2 = 1231, "Bob", "Bobson", "982131343", Position.SECRETARY
        with self.assertRaises(ValueError):
            constructor_call = Mitarbeiter(id2, firstname2, name2, date_of_birth2, position2, self.stub_contact_information, self.stub_contact_information)