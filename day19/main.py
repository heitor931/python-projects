class Zap:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def life_number(self):
        lfe_number = self.age + len(self.name)
        return lfe_number

heitor = Zap("Heitor", 34)
mudumane = Zap("Mudumane", 33)

#print(heitor.age, heitor.name, heitor.life_number())
print(mudumane.age, mudumane.name, mudumane.life_number())


