class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, power_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = power_lawan/self.armor
        print(lawan.name + ' menyerang dengan power ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

hero1 = Hero ("sniper", 100, 10, 5)
hero2 = Hero ("mirana", 100, 20, 10)

hero1.serang(hero2)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)
print("\n")
hero2.serang(hero1)

