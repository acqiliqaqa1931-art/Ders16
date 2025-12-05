#Tapsiriq 1...

# def math(siyahi):
#     math=1
#     for i in siyahi:
#         math=math*i
#     return math
# reqemler=[1,2,3,4,5,6]
# print(math(reqemler))



#Tapsiriq 2...

# def enkicik(siyahi):
#     en_kicik=siyahi[0]
#     for i in siyahi:
#         if i<en_kicik:
#             en_kicik=i
#     return en_kicik
# print(enkicik([1,2,3,4,5]))


#Tapsiriq 3...

def reqemler(siyahi):
    ededler=0
    for i in siyahi:
      if i>2:
        for j in range(2,i):
            if i%j==0:
               break
        else:
            ededler+=1


    return ededler
print("Sade ededler:",reqemler([1,2,3,4,5,6,7,8,9,11,13]))


#Tapsiriq 4...

# import math
#
# def reqem(ededler):
#
#     if a < 0:
#         return "Menfi ededlerin koku olmur"
#     else:
#         return math.sqrt(a)
#
#
#
# a = int(input("Eded daxil et:"))
# print(reqem(a))
