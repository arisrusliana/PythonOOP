# class / template
class Hero:
    pass

hero1 = Hero() #object / instance (instanciate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "Azka"
hero1.health = 9

hero2.name = "Maqil"
hero2.health = 4

hero3.name = "Fani"
hero3.health = 32

print(hero1)
print(hero1.__dict__)
print(hero1.name)
