from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person:
    def __init__(self, name: str, date_of_birth: str):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_age(self) -> int:
        return relativedelta(datetime.now(), self.date_of_birth).years
