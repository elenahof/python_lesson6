class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Employee: {self.name} {self.surname}")

    def get_total_income(self):
        print("Premium income: ", self._income["wage"] + self._income["bonus"])

emp1 = Position("John", "Doe", "Manager", 80000, 25000)
print(emp1.get_full_name(), emp1.get_total_income())

emp2 = Position("Alice", "Bart", "Designer", 120000, 30000)
print(emp2.get_full_name(), emp2.get_total_income())