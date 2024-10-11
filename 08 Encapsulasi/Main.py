# rules :
# - buat semua variable -> private
# - use Getter dan Setter
# - ketika program berjalan, tidak ada value yang boleh berubah
# - merubah nilai melalui setter

class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attack = attackPower
    
    # getter (mengambil nilai private variable)
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter (mengubah nilai private variable)
    def diserang(self,serangan):
        self.__health -= serangan


# awal dari game
sniper = Hero("sniper",100,10)

print(sniper.__dict__)

# game berjalan
print(sniper.getName())
print(sniper.getHealth())
sniper.diserang(5)
print(sniper.getHealth())




# print(sniper.__name) # tidak dapat mengakses private variable



