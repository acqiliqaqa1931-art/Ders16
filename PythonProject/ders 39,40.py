# a=int(input("Eded daxil et:"))
# b=int(input("Eded daxil et:"))
# def vur(a,b):
#     return a*b
# print(vur(a,b))


#
# def topla(a,b,c,):
#     return (a+b+c)/3
# a=int(input("Eded daxil et:"))
# b=int(input("Eded daxil et:"))
# c=int(input("Eded daxil et:"))
# print(topla(a,b,c))




# ededler=[1,2,3,4,5]
#
# def cem(siyahi):
#     return sum(siyahi)/len(siyahi)
# print(cem(ededler))


#
# ededler=[1,2,3,4,5]
#
# def enboyuk(siyahi):
#     return max(ededler)
# print(enboyuk(ededler))



# def a(*args):
#     print(args)
# a("Salam","Necesen",2025,29)

# def cem(*reqemler):
#     toplam=0
#     for i in reqemler:
#         toplam+=i
#     return toplam
# print(cem(1,2,3))

# def sozler(*soz):
    # for i in soz:
       # print(i.upper(),end=" ")
# sozler("salam","necesen")




# def melumat(**bilgi):
#     for acar, deyer in bilgi.items():
#         print(acar,"=",deyer)
# melumat(Ad="Ferid",Yas=15,Kend="Astara")

# def yas_tap(**melumat):
#     if "yas" in melumat:
#         print("Yas:",melumat["yas"])
#     else:
#         print("Yas daxil edilmeyib")
#
# yas_tap(ad="Ferid",yas=15,kend="Astara")
# yas_tap(ad="Ferid",seher="Ulanbator")

# def salamla(ad="qonaq"):
#     print("Salam",ad)
#
# salamla()
# salamla("Ferid")




# def hesabla(a,b=10):
#     print(a+b)
# hesabla(2)


# def funksiya(ad="Ferid",dil="az"):
#     if dil=="az":
#         print("Salam",ad)
#     elif dil=="en":
#         print("Hello",ad)
#     else:
#         print("Bonjour",ad)
#
# funksiya("Ferid","en")


# yasin = int(input("Yas daxil et:"))
# def a(yas):
#     if yas == 18:
#         print("Qesey gedsen esgerliyee")
#     elif yas>18:
#         print("boyumusen haa")
#     elif yas<18:
#         print("kisi balasan hele")
# a(yasin)



# def faktorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*faktorial(n-1)
# print(faktorial(5))



# def ters(s):
#     if len(s)==0:
#         return ""
#     else:
#         return s[-1]+ters(s[:-1])
# print(ters("salam"))



# def sozler(*soz):
#     for i in soz:
#        print(i.lower(),end=" ")
# sozler("SALAM","NECESEN")



# def yas_tap(**melumat):
#     if "soyad" in melumat:
#         print("Soyad:",melumat["soyad"])
#     else:
#         print("Soyad daxil edilmeyib")
#
# yas_tap(ad="Ferid",soyad="Memmedzade",yas=15,kend="Astara")


# n=int(input("Eded daxil et:"))
# def eded(reqem):
#     if n>0:
#         eded(n-1)
#         print(n)


# def a(n):
#     if n>0:
#         a(n-1)
#     print(n)
#
# n=int(input("Eded daxil et:"))
# a(n)


# def hesabla(a, b, emel="+"):
#     if emel == "+":
#         print("Cem:", a + b)
#     elif emel == "-":
#         print("Ferq:", a - b)
#     elif emel == "/":
#         print("Qismet:", a / b)
#     elif emel =="*":
#         print("Hasil:", a * b)
#
# hesabla(15, 3)
# hesabla(15, 3, "-")
# hesabla(15,3,"/")
# hesabla(15,3,"*")



# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# a=int(input("Eded daxil et:"))
# for i in range(a):
#     print(fib(i),end=" ")

# def loop():
#     print("Hello")
#     loop()
# loop()


# def kvadrat(x):
#     return x*x
# print(kvadrat(5))
#
# a=((lambda a:a*a)(4))
# print(a)
# print((lambda a,b:a+b)(10,15))
#
# sozler=["Alma","Armud","Alca"]
# print(list(map(str.upper,sozler)))




# ededler=[1,2,3,4,5]
# def vur(x):
#     return x*2
# netice=list(map(vur,ededler))
# print(netice)
#
# print(list(map(lambda x:x*2,ededler)))



# eded=[1, 2, 3, 4, 5]
# def topla(x):
#     return x+20
# c=list(map(topla, eded))
# print(c)
# print(list(map(lambda a:a+20, eded)))



# bos=[]
# n=int(input("Uzunluq:"))
# for i in range(n):
#     a=int(input("Ededler daxil et:"))
#     bos.append(a)
# print(bos)
# print(list(map(lambda x:x,bos)))




# ededler=[1,2,3,4,5]
# def cut(a):
#     return a%2==0
# def tek(b):
#     return b%2!=0
# print(list(filter(cut,ededler)))
# print(list(filter(tek,ededler)))
# print(list(filter(lambda x:x%2==0,ededler)))



#
# def cem(x,y):
#     return x+y
# ededler=[1,2,3,4,5]
# print(reduce(cem,ededler))
# print(reduce(lambda x,y:x+y,ededler))
# print(reduce(lambda x,y:x if x>y else y,ededler))
from functools import reduce

ededler=[1,2,3,4,5,6,7,8,9,10]
def vur(a):
    return a*4
a=(list(map(vur,ededler)))
print(a)
b=(list(filter(lambda b:b%3==0,a)))
print(b)
c=(reduce(lambda a,b:a+b,b))
print(c)
