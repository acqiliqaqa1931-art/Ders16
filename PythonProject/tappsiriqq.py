saysistem=input("Secimini daixl et(2/8/10/16)")
eded=int(input("Ededi qeyd et:"))
eded2=int(input("Diger ededi daxil et:"))

if saysistem=="2":
    print("Ikilik say sistemi",bin(eded),bin(eded2))

elif saysistem=="8":
    print("Sekkizlik say sistemi",oct(eded),oct(eded2))

elif saysistem=="10":
    print("Onluq say sistemi",oct(eded),oct(eded2))

elif saysistem=="16":
    print("Onaltiliq say sistemi",hex(eded),hex(eded2))

else:
    print("Bele bir say sistemi ola bilmez!")

if eded>eded2:
    print(f"En boyuk eded: {eded}")

elif  eded2>eded:
    print(f"En boyuk eded: {eded2}")

elif eded==eded2:
    print("Ededler beraberdir")
