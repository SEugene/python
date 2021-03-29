class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


person1 = Position('John', 'Milton', 'SEO', 50000, 25000)
print(f'{person1.get_full_name()}; GROSS total income: {person1.get_total_income():.2f} $ per month')

person2 = Position('Jane', 'Dakota', 'Chief Accountant', 20000, 5000)
print(f'{person2.get_full_name()}; GROSS total income: {person2.get_total_income():.2f} $ per month')
