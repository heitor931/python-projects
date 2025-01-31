class Person:
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race
    def future_number(self):
        result = len(self.name) + self.age + len(self.race)
        return result

person1 = Person("heitor", 34, "black")
print(person1.future_number())
