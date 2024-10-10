class Hero: #template
    # class variable / static variable
    jumlah = 0
    def __init__(self, inputName, inputPower, inputHealth, inputArmor):
        # instance variable
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama " + inputName)

hero1 = Hero("sniper",100,20,9)
print(f"Jumlah hero = {Hero.jumlah}")
hero2 = Hero("mirana",100,15,5)
print(f"Jumlah hero = {Hero.jumlah}")
hero3 = Hero("azka",1000,150,80)
print(f"Jumlah hero = {Hero.jumlah}")
print(Hero.__dict__)
