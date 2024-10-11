class Hero:

    # class variable (public)
    jumlah = 0
    # class variable (public)
    __privateJumlah = 0

    def __init__(self,inputName,inputHealth):
        # instance public variable
        self.name = inputName
        self.health = inputHealth

        # instance private variable
        self.__private = "private"

        # instance protected variable (bersifat public)
        self._protected = "protected"

azka = Hero("azka", 100)
maqil = Hero("maqil", 100)

print(azka.__dict__)
print(azka.name)
print(azka._protected) # bisa akses karena bersifat public
azka._protected = "testing"
print(azka.__dict__)
print(azka._protected)
print("\n")
print(Hero.jumlah)
print(Hero.__privateJumlah)


# private -> tidak bisa diakses
# protected -> bisa diakses tetapi tidak boleh diubah