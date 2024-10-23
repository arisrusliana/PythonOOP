# magic method
class Mangga:
    def __init__(self,name,jumlah):
        self.name = name
        self.jumlah = jumlah
    
    # method __repr__ digunakan ketika debuging
    def __repr__(self):
        return "debug - Mangga {} dibeli dengan jumlah {}".format(self.name, self.jumlah)
    
    # method __str__ digunakan ketika produksi
    def __str__(self):
        return "Mangga {} dibeli dengan jumlah {}".format(self.name, self.jumlah)
    
    # method __add__ untuk menjumlahkan objek 1 dan objek 2
    def __add__(belanja1, belanja2): # --> penamaan parameter itu bebas, tidak terikat
        return belanja1.jumlah + belanja2.jumlah
    
    @property  # menggunakan decorator untuk me-replace nilai dari __dict__
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga("arum manis", 10)
belanja2 = Mangga("gedong gincu", 12)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)