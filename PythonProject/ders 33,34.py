# numbers=[]
#
# n=int(input("Listin uzunlugunu daxil et:"))
# for i in  range(n):
#     num=int(input("Ededleri daxil edin:"))
#     numbers.append(num)
# print("Daxil etdiyin ededler:",numbers)


# numbers=[]
# i=0
# n=int(input("Liste nece eded elave etmek isteyirsen:"))
#
# while i<n:
#     num=int(input("Liste daxil olacaq ededleri daxil et:"))
#     numbers.append(num)
#     i+=1
# print(numbers)



# reqemler=[20,3,15,8,7,16,1,0,0,544]
# boyuk10=[]
#
# for reqem in reqemler:
#     if reqem>10:
#         boyuk10.append(reqem)
# print(boyuk10)


# reqemler=[1,4,5,6,3,18,2,19,35]
# cut_list=[]
# tek_list=[]
#
# for reqem in reqemler:
#     if reqem%2==0:
#         cut_list.append(reqem)
#     if reqem%2!=0:
#         tek_list.append(reqem)
# print("Cut ededler:",cut_list)
# print("Tek ededler:",tek_list)


# a=[]
# palindromlar=[]
# s=int(input("Nece eded daxil etmek isteyirsen:"))
# for i in range(s):
#     deyer=input("Daxil edin:")
#     a.append(deyer)
# for deyer in a:
#     if deyer==deyer[::-1]:
#         palindromlar.append(deyer)
# print(a)
# print(palindromlar)


# def test():
#     x=5
#
# print(test())


# a=[1,2,3]
# a.append("salam")
# print(a)
# a=None
# print(a)


# my_tuple=(5,10,15)
# my_list=list(my_tuple)
# my_list.append(25)
# print(my_tuple)
# print(my_list)


# #set list tipine benzerdir.
# #{} bu morterize ile yazilir.
# #set pythonda tekrarlanmayan unikal elementlerden ibaret verilenler toplusudur.
# set={1,2,3,4,4}
# print(set)
# #add bir elementi elave etmek ucun istifafde olunur.
# set.add("gavali")
# print(set)
# #update birden cox element elave etmek ucun istifade olunur.
# set.update("nar","alca")
# print(set)
# #set tekrarlanmayan melumat tipidir.
# #frozensetin icindeki elementler deyisdirile bilmez.
# fs=frozenset({1,2,3})
# print(fs)

#dictionaryde her bir melumatin bir adi ona uygun deyeri olur
# telebe={
#     "ad":"Ali",
#     "yas":20
# }
# print(telebe["ad"])

