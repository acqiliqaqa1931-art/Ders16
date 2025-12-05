# a=0
#
# while a<=5:
#     print(a)
#     a+=1

#burda while dovru n deyiseninin 10 dan boyuk olmadigi muddetde isleyecek.
#her iterasiyada n deyiseni ceme elave olunacaq.
# ve n deyiseni 11 i gordukde dovr dayanacaq
#ve konsola birden ona olan qeder ededlerin cemi gorsenecek.
# cem=0
# n=1
#
# while n<=10:
#     cem+=n
#     n+=1
#
# print(cem)













#sert duzgun olmursa while dovru hec vaxt icra oluna bilmez.
# i=36
# while i<35:
#     if i%3==0:
#         print(i)
#     i+=1
# print("step it")












#istifadecinin verdiyi eded araliginda hem coxdan aza hemde azdan coxa while dovrunu ekrana cap eden proqram.
# num1=int(input("Diapozonun evveli:"))
# num2=int(input("Diapozonun sonu:"))

# while num1<num2+1:
#     print(num1)
#     num1+=1


# while num1-1<num2:
#     print(num2)
#     num2-=1










#mueyyen meyveni gorene qeder dovru icra edir.erik meyvesini gorerse dovru dayandirir.
# meyveler=["alca","ciyelek","erik"]
#
# for meyve in meyveler:
#     if meyve=="erik":
#         break
#     print(meyve,end=" ")
















#reqemler siyahisinin eger cur ededler varsa continue operatoru onlari atlayir yanliz tek ededleri cap edir
# reqemler=[1,5,7,10,4,2]
#
#
# for reqem in reqemler:
#     if reqem%2==0:
#         continue
#     print(reqem)
















# while True:
#     secim=int(input("Secim et:"))
#     if secim==1:
#         print("Elave et")
#     elif secim==2:
#         print("Sil")
#     elif secim==3:
#         print("Cix")
#         break
#








#1-15 e qeeder dovr edecek 7 ni gordukde dayandiracaq.
# i=0
# while i<15:
#     i+=1
#     if i==7:
#         continue
#     print(i)



















#duzgun parolu yazana qeder bize parol yazmagimizza icaze veren kod.
# correct_password="12345"
# password=input("Parolu daxil et:")
#
# while password!=correct_password:
#     print("Parol yanlisdir!")
#     password = input("Parolu yeniden daxil et:")
#
# else:
#     print("Parol duzdur Xos geldiniz!")
#


























# texmin oyunu:
# 1den 20 e kimi kompyuter random eded secir duz texmin etdikde ekrana tebrikler cixir.
# eks halda reqemi tapana qeder bizden cehd etmeyimizi isteyir
import random

sirr=random.randint(1,20)

while True:
    texmin=int(input("Texmin et:"))
    if texmin==sirr:
        print("Tebrikler qalibsiniz!")
        break
    else:
        print("Zeif yanlis texmin yeniden cehd et:")

