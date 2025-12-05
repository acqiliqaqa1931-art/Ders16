# import math
#
# print(math.pow(2,3))
# print(math.sqrt(25))
# print(math.exp(2))
# print(math.log(10,10))
# print(math.sin(math.pi/2))
# print(math.factorial(5))
# print(math.fabs(5))


# import random
# random 0, ile 1 arasinda random eded verir.
# print(random.random())
# randint ise verdiyimiz ededler arasinda random eded verir.
# print(random.randint(1,10))
#uniform ise verdiyimiz ededler arasinda random onluq ededler verir.
# print(random.uniform(5,10))

# colors=["sari","mavi","qirmizi"]
#choice listin icinden random reng secib cixarir.
# print(random.choice(colors))
#choices ise listden nece dene reng cixardacagini secmeye imkan verir.
# print(random.choices(colors,k=2))



# import re

metn="Salam Dunya Menim Nomrem 463634646"

# netice=re.search(r"\d+",metn)
# print(netice.group())

metn1="Python 12 , Java 9, C++ 11"
#reqemleri siyahi halina salir.
# reqemler=re.findall(r"\d+",metn1)
# print(reqemler)
#match baslangicda bu sozun oldugunu dogrulayir.
# print(re.match(r"Python",metn1))
#reqemleri ulduzlamaq ucun istifade olunur.
# yeni=re.sub(r"\d+","*********",metn)
# print(yeni)
#D herflernen isleyir d reqemlerle isleyir.

#hem reqem hem herfi sihayi kimi yazir.
# print(re.findall(r"\w+",metn))
#W ancaq simvollari cixarir w ise hem reqem hem herfi cixarir.









# import math
#
#
# ededler=[16,81,36,49]
# cut_eded=[]
# tek_eded=[]
# for i in ededler:
#     kok=math.sqrt(i)
#     if kok%2==0:
#         cut_eded.append(kok)
#     if kok%2!=0:
#         tek_eded.append(kok)
# print(cut_eded)
# print(tek_eded)






# import datetime
#
# while True:
#     try:
#         dogum_il=int(input("Ilinizi daxil edin:"))
#         break
#     except ValueError:
#         print("Zehmet olmasa reqem daxil edin:")
# indiki_il=datetime.datetime.now().year
# yas=indiki_il-dogum_il
# if yas>=18:
#     print("Yetkinsen!")
#
# else:
#     print("Yetkin deilsen!",yas)






# import random
#
#
# a=[]
#
# while len(a)<5:
#     texmini=random.randint(1,50)
#     if texmini%2==0:
#        a.append(texmini)
# print(a)









# import random
#
# texmin=random.randint(1,100)
#
# while True:
#     sirr=int(input("Texmin et:"))
#     if texmin==sirr:
#         print("Tebrikler!")
#         break
#
#     if texmin<sirr:
#         print("Sirrden boyukdur daha asagi eded yaz")
#
#     if texmin>sirr:
#         print("Sirrden kicikdir daha boyuk eded yaz")






