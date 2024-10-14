class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self,name,health):
        self.__name = name
        self.__health = health
        Hero.__jumlah += 1
    
    #method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah

    #method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    #static method (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero('sniper', 100)
# print(sniper.getJumlah()) # untuk object
print(Hero.getJumlah1()) # untuk class
print(Hero.getJumlah2()) # untuk method dan class

bomber = Hero('bomber', 100)
print(Hero.getJumlah1()) # untuk class
print(bomber.getJumlah2()) # untuk method dan class

rider = Hero('rider', 90)
print(Hero.getJumlah3())
print(rider.getJumlah3())


