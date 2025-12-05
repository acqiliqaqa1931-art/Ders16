# try:
#     num=int(input("Ededi daxil et:"))
#     result=10/num
#     print(result)
# except ZeroDivisionError:
#     print("Sifira bolmek olmaz!")
#
# except ValueError:
#     print("Xeta dogru olmayan deger daxil etdiniz")
#
# except Exception as e:
#     print("Xeta", e)
#
#
# finally:
#     print("Finally blokunun icrasi")


# a=int(input("Eded daxil et:"))
#
# if a!=0:
#     print(10/a)
#
# else:
#     print("Sifira bolmek olmaz!")





#try exceptle sade kalkuliator yaratmaq.
# while True:
#     op=input("Emeliyyat {+,-,*,/} secim {Cixmaq ucun exit}")
#     if op=="exit":
#         break
#     if op not in["+","-","/","*"]:
#         print("Yanlis emeliyyat!")
#         continue
#     try:
#          a=float(input("Ilk eded:"))
#          b=float(input("Ikinci eded:"))
#          if op=="+":print(a+b)
#          elif op=="-": print(a - b)
#          elif op=="*": print(a * b)
#          elif op == "/": print(a / b)
#     except Exception as E:
#         print("Xeta",E)

















#else bloku try blokunda sehv bas vermese isleyir.
# try:
#     a=int(input("Eded daxil et:"))
#     print(10/a)
#
#
# except Exception as b:
#     print("Xeta",b)
#
# else:
#     print("Ela her sey bomba kimidir")
#

#for ile siyahidaki elementlerin tipini yoxla ve ededleri topla.
# element=[1,3,"a","r",6,"asfasf"]
# sum=0
#
# for i in element:
#     try:
#         sum+=i
#     except TypeError:
#         print(f"{i} eded deyil kec")
# print("Cem:", sum)



















# element=[1,2,3,4,5,6,7,8,9,10]
# sum=0
#
# for i in element:
#     try:
#         if i%2==0:
#             sum+=i
#     except:
#         print(f"{i} cut eded deyil.")
#
# print("Cavab:",sum)