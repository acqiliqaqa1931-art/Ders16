#Tapsiriq 1...

# def uzunluq(a,b,c):
#     return len(a),len(b),len(c)
#
# print(uzunluq("gavali","alma","meyveli"))
# siyahi = ["gavali","alma","meyveli"]
# print(list(map(lambda x:len(x),siyahi)))




#Tapsiriq 2...


# ededler=[1,2,3,4,5]
# def tek(b):
#     return b%2!=0
# print(list(filter(tek,ededler)))
# print(list(filter(lambda x:x%2!=0,ededler)))

#Tapsiriq 3...

# from functools import reduce
# def en_kicik(siyahi):
#     return min(siyahi)
#
# ededler = [4, 9, 2, 7, 1]
# a=en_kicik(ededler)
# print(a)
#
# print(reduce(lambda x,y:x if x<y else y,ededler))