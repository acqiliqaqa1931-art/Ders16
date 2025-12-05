# for herf in "Salam":
#     print(herf)
#
#
#
#
#
#
#
#
#
#
#
# meyveler=['alma','armud','banan']
# for meyve in meyveler:
#     print(meyve)


# for i in range(5,10,2):
#     print(i)



# sum=0
# for i in range(1,7):
#     if i%2==0:
#         i-=1
#         print(i)


# ilk isare toplayir ikinci isare menimsedir
# a=5
# print(a)
# a+=6
# print(a)
#
#
# b=4
# print(b)
# b-=3
#
#
# c=6
# print(c)
# c*=2
#
#
# d=8
# print(d)
# d/=2
# print(d)






# car=input("Adi qeyd et:")
# pulum=120000
#
#
# for carr in car:
#     if carr=='Audi':
#         pulum+=5000
#     elif carr=='Porsche':
#         pulum+=80000
#     elif carr=='RangeRover':
#         pulum+=200000
#     elif carr=='BMW':
#         pulum+=120000
#
# for i in carr:
#     if i=="Audi":
#         print("Audi:",pulum)





# start=int(input(" Ilk deyer:"))
# end=int(input(" Son deyer:"))
#
# for i in range(start,end):
#     i+=5
#     print(i)

# for i in  range(1,10):
#       if i>10:
#           print(i)
#
#



# correct_login="Ferid15"
# correct_password="1234@"
# for a in range(3):
#     login=input("Logini daxil et:")
#     password=input("Passwordu daxil et:")
#     if correct_login==login and correct_password==password:
#         print("Ugurlu emeliyyat sisteme giris")
#         break
#     else:
#         sans=2-a
#         if sans>=0:
#             print(f"Sehv giris,Qalan sans:{sans}")
#         if sans==0:
#             print("3 defe sehv giris hesab bloklandi")





























# a=int(input("Ededi daxil et:"))
# if a < 1 or a >100:
#     print("Error")
# else:
#     if a%3==0:
#         print("Fizz")
#
#     elif a%5==0:
#         print("Buzz")
#
#     elif a%3==0 and a%5==0:
#         print("Fizz Buzz")
#
#     elif a%3!=0 and a%5!=0:
#         print("ERROR")
#
#
#
#
#
#
#
#
#
#
#
#
#
# a=int(input("Ededi daxil et:"))
# b=int(input("Quvveti daxil et:"))
#
# if b >= 0 and b <= 7:
#     cavab=a ** b
#     print("Cavab:", cavab)
#








































# siyahi=["Adem",12,7.8,True]
#
# for x in siyahi:
#     print(x)



# yazi="Homosapiens"
#
# for i in yazi:
#     print(i)





















# for i in range (1,11):
#     print(i,"->",i**2)

























#5 ededin ededi ortasini tapin ekrana cap edin.
# cem=0
#
# for i in range(5):
#     eded=int(input("Eded daxil et:"))
#     cem+=eded
# print("Ededi orta",cem/5)

























# reqemler=[12,15,24,35,1,25,56]
# en_boyuk=reqemler[0]
#
# for i in reqemler:
#     if i>en_boyuk:
#         en_boyuk=i
# print("En boyuk:",en_boyuk)















# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("Ededler:",i)







# for i in range(1,6):
#     print("*"*i)






















# for i in range(3):#xarici dovr
#     for j in range(2):#daxili dovr
#         print("i:",i,"j:",j)
#











# for j in range(2):
#     for i in range(3):
#           print("j:",j,"i:",i)















#ededleri cedvel seklinde toplanmasi.
# for i in range (1,4):
#     for j in range(1,4):
#         print(i,"+",j,"=",i+j)
#     print("---------")
#













# for i in range(3):
#     for j in range(3):
#         if j==1:
#             break
#         print(i,j)













# for i in range(5):
#     print(i,end=" ")














# for i in range(1,4):
#     for j in range(1,4):
#         print(i,"+",j,"=",i+j,end="  ")
#     print()










































# for i in range(5):
#     for j in range(4):
#         print("*",end="")
#     print()












































# h=5
# for i in range(1,h+1):
#     print(" "*(2*i+1)+"*" * (h+1))









































# a=int(input("Eded daxil et:"))
# b=int(input("Ikinci ededdi daxil et:"))
#
# for i in range(a,b):
#     if a%a==1 and b%b==1:
#         print(i)
























# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j,)
#     print()
















# h=5
# for i in range(1,h+1):
#     print(" "*(2*i+1)+"*" * (h+1))
















# a=int(input("Ededi daxil et:"))
# b=int(input("Ikinci ededi daxil et:"))
#
# for i in range (a,b):
#     for j in range(a,b):
#         print(i,"*",j,"=",i*j)
#     print("---------")




















# for i in range(1,6):
#     print("*"*i)