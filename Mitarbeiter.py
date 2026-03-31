from datetime import datetime
from Kunden import Kunde
from Person import Person
from enum import Enum
from dateutil.relativedelta import relativedelta

class Position(Enum):
    SECRETARY = ('secretary', 1)
    CUSTOMER_SERVICE = ('customer service', 5)
    DEV = ('dev', 10)
    MANAGER = ('manager', -10)

    def __new__(cls, position_name: str, aging_constant: int):
        obj = object.__new__(cls)
        obj._value_ = position_name # enum key
        obj.position_name = position_name
        obj.aging_constant = aging_constant
        return obj


class Mitarbeiter(Person):
    def __init__(self, id, name, date_of_birth, position):
        super().__init__(name, date_of_birth)
        self.mitarbeiter_id = id
        self.position = position

    def __str__(self):
        return f"{self.name}, Ist aufgrund seiner Position gefühlt {self.get_age()} Jahre alt, Position: {self.position}"

    def __eq__(self, mitarbeiter2: "Mitarbeiter"):
        if self.mitarbeiter_id == mitarbeiter2.mitarbeiter_id:
            return True
        else:
            return False

    def get_age(self) -> int:
        perceived_age = super().get_age()
        match self.position:
            case Position.SECRETARY:
                added_age_due_to_someone_in_the_office_still_sends_documents_by_fax = Position.SECRETARY.aging_constant
                perceived_age += added_age_due_to_someone_in_the_office_still_sends_documents_by_fax
            case Position.CUSTOMER_SERVICE:
                added_age_due_to_handling_raging_customers = Position.CUSTOMER_SERVICE.aging_constant
                perceived_age += added_age_due_to_handling_raging_customers
            case Position.DEV:
                added_age_due_to_non_agile_release_cycles = Position.DEV.aging_constant
                perceived_age += added_age_due_to_non_agile_release_cycles
            case Position.MANAGER:
                added_age_due_to_feeling_young_and_dynamic_like_a_manager = Position.MANAGER.aging_constant
                perceived_age += added_age_due_to_feeling_young_and_dynamic_like_a_manager
                if perceived_age <= 0:
                    # even with a manager attitude you can not feel that young and dynamic
                    perceived_age = super().get_age()
            case _:
                pass
        return perceived_age
        

class Kundenbetreuung:
    def __init__(self, mitarbeiter, kunde: Kunde):
        self.mitarbeiter = mitarbeiter
        self.kunde = kunde

    def __str__(self):
        return f"{self.mitarbeiter.name} betreut {self.kunde}."
