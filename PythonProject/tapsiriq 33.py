# reqemler=[]
# cut_list=[]
# tek_list=[]
# s=int(input("Nece eded daxil etmek isteyirsen:"))
# for i in range(s):
#     for j in reqemler:
#      deyer=input("Daxil edin:")
#      if deyer%2==0:
#         cut_list.append(reqemler)
#      if deyer%2!=0:
#         tek_list.append(reqemler)
# print("Cut ededler:",cut_list)
# print("Tek ededler:",tek_list)


# cut_list=[]
# tek_list=[]
# s=int(input("Nece eded daxil etmek isteyirsen:"))
# for reqem in range(s):
#     a=int(input("Eded daxil et:"))
#     if a % 2 == 0:
#         cut_list.append(a)
#     if a%2!=0:
#         tek_list.append(a)
# print("Cut ededler:",cut_list)
# print("Tek ededler:",tek_list)





c=[]
max_list=[]
min_list=[]
sum_list=[]

s=int(input("Nece eded daxil etmek isteyirsen:"))

for i in range(s):
    a=int(input("Eded daxil et:"))
    c.append(a)
cox=max(c)
az=min(c)
cem=sum(c)
max_list.append(cox)
min_list.append(az)
sum_list.append(cem)
print(max_list)
print(min_list)
print(sum_list)




# a=[]
#
# s=int(input("Nece eded daxil etmek istiyirsen:"))
# for i in range(s):
#     try:
#         c=int(input("Eded daxil et:"))
#         a.append(c)
#     except ValueError:
#         print("Xeta")
#         break
# print("Cavab",a)

