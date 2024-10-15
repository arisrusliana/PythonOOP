class Hero: #superclass
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero): #subclass
    pass

class Hero_strength(Hero): #subclass
    pass

lina = Hero('lina', 100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe', 500)

print(lina.name)
print(techies.name)
print(axe.name)
# print(help(axe))