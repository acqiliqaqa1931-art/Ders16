# Tapsiriq 2...

class masin:
    pass
masin1=masin()
masin1.name1="Mercedes"
masin1.name2="BMW"
masin1.name3="Audi"
print(masin1.name1)
print(masin1.name2)
print(masin1.name3)

#Tapsiriq 1...

class Vur:
    def __init__(self,a,b):
        self.vur1=a
        self.vur2=b
    def vur(self):
        return self.vur1*self.vur2
a=int(input("Enini daxil et:"))
b=int(input("Uzunlugunu daxil et:"))
Hasil=Vur(a, b)
print(Hasil.vur())
