# method resolution order / multiple inheritance
class A:
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adalah show B")

class C(A,B): #--> menentukan urutan dari C(A,B) menjadi C,A,B atau C(B,A) menjadi C,B,A
    pass

objek = C()
objek.show()
# help(objek)