# class / template
# class Fams:
#     def __init__(self,x): # __init__ akan dijalankan pertama kali ketika program dijalankan
#         print("Hallo", x) # self == fam1, fam2

# # object fam1 dan fam2 memanggil Fams()
# # running program
# fam1 = Fams("Azka")
# fam2 = Fams(500)

# template
class Hero:
    def __init__(self,inputName,inputPower,inputHealth,inputArmor):
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        self.armor = inputArmor


# object (instanciate)
hero1 = Hero("Azka",10,9,8)
hero2 = Hero("Maqil",9,10,8)
hero3 = Hero("Fani",100,80,90)

print(hero1)
print(hero1.name)
print(hero2.health)
print(hero3.__dict__) # __dict__ --> menampilkan all attributes
