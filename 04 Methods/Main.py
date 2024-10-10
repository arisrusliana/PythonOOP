class Hero:
    # class variable
    jumlah_hero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    # void function / method tanpa return
    def siapa(self):
        print("Nama saya adalah " + self.name) # display method
    
    # method dengan argumen
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

# object
hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mirana", 90, 5,10)

# memanggil method tanpa return
hero1.siapa()
hero2.siapa()
# memanggil method dengan argumen tanpa return
hero1.healthUp(50)


# display method dengan argumen tanpa return
print("Health " + hero1.name + " menjadi " + str(hero1.health))
# display method dengan return
print("Health " + hero1.name + " menjadi " + str(hero1.getHealth()))


