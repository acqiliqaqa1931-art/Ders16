# class BankHesabi:
#     def __init__(self,sahib,hesab):
#         self.sahib=sahib
#         self.__hesab=hesab
#     def Hesabgoster(self):
#         print(f"{self.sahib}in Hesabi:{self.__hesab}AZN")
#     def Hesabartir(self,mebleg):
#         self.__hesab+=mebleg
#         print(f"{mebleg}AZN elave edildi.Yeni hesab:{self.__hesab}AZN")
#     def Hesabazalt(self,mebleg):
#         if mebleg<=self.__hesab:
#             print(f"Hesabdan {mebleg}AZN cixildi.Qalan Hesab:{self.__hesab}AZN")
#         else:
#             print("Kasib senin o qeder puln yoxdur!")
#
# class VIPHesab(BankHesabi):
#     def __init__(self,sahib,hesab,bonus_faiz):
#         BankHesabi.__init__(self,sahib,hesab)
#         self.bonus_faiz=bonus_faiz
#     def Bonus_elave_et(self):
#         bonus=self.bonus_faiz*0.01*self._BankHesabi__hesab
#         self._BankHesabi__hesab+=bonus
#         print(f"Bonus:{bonus} Elave edildi. Yeni balans:{self._BankHesabi__hesab}")
#
# hesab1=BankHesabi("Ferid",1000)
# vip1=VIPHesab("Elsen",10000,20)
#
# hesab1.Hesabgoster()
# hesab1.Hesabartir(500)
#
# vip1.Hesabgoster()
# vip1.Bonus_elave_et()


# class Qida:
#     def __init__(self,ad,terkibi):
#         self.ad=ad
#         self.terkibi=terkibi
#     def melumat(self):
#         print(f"{self.ad}-{self.terkibi}")
#
# class Meyve(Qida):
#     def __init__(self,ad,terkibi,vitaminc):
#         super().__init__(ad,terkibi)
#         self.vitaminc=vitaminc
#     def vitamin(self):
#         print(f"{self.ad} icinde {self.vitaminc} mg var")
#
# meyve1=Meyve("Alma","A vitamini",20)
#
# meyve1.melumat()
# meyve1.vitamin()






#
# class Heyvan:
#     def __init__(self,ad,cins):
#         self.ad=ad
#         self.cins=cins
#     def melumat(self):
#         print(f"{self.ad}-{self.cins}")
# class Qus(Heyvan):
#     def __init__(self,ad,cinsi,qanaduzunlugu):
#         super().__init__(ad,cinsi)
#         self.qanaduzunlugu=qanaduzunlugu
#     def qanadinolcusu(self):
#         print(f"Adi-{self.ad}.Qanadinin uzunlugu:{self.qanaduzunlugu}")
#
# olcu=Qus("Serce","disi",15)
# olcu.qanadinolcusu()
# olcu.melumat()


# class Heyvan:
#     def sescixar(self):
#         print("Heyvan ses cixardir.")
#
# class It(Heyvan):
#     def sescixar(self):
#         print("Hav Hav")
#
# class Pisik(Heyvan):
#     def sescixar(self):
#         print("Miyav Miyav")
#
# h=Heyvan()
# i=It()
# p=Pisik()
# h.sescixar()
# i.sescixar()
# p.sescixar()




# class Masin:
#     def suret(self):
#         print(200)
#
# class Mercedes(Masin):
#     def suret(self):
#         print(250)
#
# class BMW(Masin):
#     def suret(self):
#         print(280)
# class Porsche(Masin):
#     def suret(self):
#         print(320)
#
#
# m=Mercedes()
# b=BMW()
# p=Porsche()
# m.suret()
# b.suret()
# p.suret()



# class Mehsul:
#     def qiymet(self):
#         return 0
#
# class Kitab(Mehsul):
#     def qiymet(self):
#         return 20
#
# class Tv(Mehsul):
#     def qiymet(self):
#         return 1000
#
# m=Mehsul()
# k=Kitab()
# t=Tv()
# print(m.qiymet())
# print(k.qiymet())
# print(t.qiymet())
#
# mehsullar=[m,k,t]
#
# for i in mehsullar:
#     print(i.qiymet())














# class Sekil:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sahe(self):
#         return 0
#
# class Duzbucaqli(Sekil):
#     def sahe(self):
#         return self.a*self.b
#
# class Daire(Sekil):
#     def sahe(self):
#         return self.a*(self.b**2)
#
# class Kvadrat(Sekil):
#     def sahe(self):
#         return self.a**2
#
# d=Duzbucaqli(4,5)
# d1=Daire(3.14,3)
# k=Kvadrat(2,0)
#
# a=[d,d1,k]
# for i in a:
#     print(i.sahe())