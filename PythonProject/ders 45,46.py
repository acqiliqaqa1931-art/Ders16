# class Adam:
#     def __init__(self,ad):
#         self.name=ad
#
# a1=Adam("Covdet")
# print(a1.name)
#
# a1.name="Siyavuw"
# print(a1.name)


# class Telebe:
#     def __init__(self,ad):
#         self._ad=ad
#
# class Magistr(Telebe):
#     def goster(self):
#         print(f"Magistr adi:{self._ad}")
# t1=Magistr("Mugdat")
# t1.goster()



# class Telebe:
    # def __init__(self,ad):
        # self.__ad=ad

    # def goster(self):
        # print(f"Ad:{self.__ad}")

# t1=Telebe("Eli")
# t1.goster()

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self,amount):
#         if amount>0 and amount<=self.__balance:
#             self.__balance-=amount
# hesab=BankAccount(1000)
# print(hesab.get_balance())
# hesab.deposit(500)
# print(hesab.get_balance())
# hesab.withdraw(600)
# print(hesab.get_balance())




# class BankHesabi:
#     def __init__(self,sahib,balans,pin):
#         self.sahib=sahib
#         self.__balans=balans
#         self.__pin=pin
#     def balans_goster(self):
#         daxil_pin=int(input("Pini daxil et:"))
#         if daxil_pin==self.__pin:
#             print(f"Balans:{self.__balans}AZN")
#         else:
#             print("Yanlis Pin!")
#     def pul_artir(self):
#         daxil_pin=int(input("Pini daxil et:"))
#         if daxil_pin==self.__pin:
#             mebleg=int(input("Ne qeder elave edeceksiniz?"))
#             if mebleg>0:
#                 self.__balans+=mebleg
#                 print(f"Yeni hesab:{self.__balans}")
#             else:
#                 print("Mebleg menfi ola bilmez")
#         else:
#             print("Yanlis Pin")
#     def pul_cixar(self):
#         daxil_pin = int(input("Pini daxil et:"))
#         if daxil_pin == self.__pin:
#             mebleg = int(input("Ne qeder elave edeceksiniz?"))
#             if 0 < mebleg < self.__balans:
#                 self.__balans -= mebleg
#                 print(f"Qalan hesab:{self.__balans}")
#             else:
#                 print("Mebleg duzgun deil kifayet qeder pulunuz yoxdur")
#         else:
#             print("Yanlis Pin")
#
# hesab=BankHesabi("Ferid",150,1234)
# while True:
#     print("------Bank Emeliyyatlari------")
#     print("1.Balans yoxla")
#     print("2.Balans artir")
#     print("3.Balans cixar")
#     print("4.Cixis")
#     secim=int(input("Emeliyyat nomresini daxil edin:"))
#     if secim==1:
#         hesab.balans_goster()
#         break
#     elif secim==2:
#         hesab.pul_artir()
#         break
#     elif secim==3:
#         hesab.pul_cixar()
#         break
#     elif secim==4:
#         print("Proqramdan cix")
#         break

# class Heyvan:
#     def __init__(self,ad):
#         self.ad=ad
#
#     def ses_cixar(self):
#         print(f"{self.ad} Ses cixar")
#
# class It(Heyvan):
#     def __init__(self,ad,cins):
#         Heyvan.__init__(self,ad)
#         self.cins=cins
#     def salamla(self):
#         print(f"{self.ad} size salam verir")


# class Ilan(Heyvan):
#     def __init__(self,ad2,cins2):
#         Heyvan.__init__(self,ad2)
#         self.ad=ad2
#         self.cins2=cins2
#     def sanc(self):
#         print(f"{self.ad} sancdi")

# it1=It("Qargabas","Alman cobani")
# it1.ses_cixar()
# it1.salamla()

# il1=Ilan("Qara_Mamba","Zeherli")
# il1.sanc()
# il1.ses_cixar()