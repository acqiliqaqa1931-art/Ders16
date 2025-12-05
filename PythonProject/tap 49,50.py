class Company:
    def __init__(self,ad,maas):
        self.ad=ad
        self.__maas=maas
    def a(self):
        print(f"Adi:{self.ad} Maas:{self.__maas}")
class Manager(Company):
    def __init__(self,ad,maas,komanda_bonus):
        super().__init__(ad,maas)
        self.komanda_bonus=komanda_bonus
    def team_bonus(self):
        bonus=self.komanda_bonus*0.02*self._Company__maas
        self._Company__maas+=bonus
        print(f"{bonus} elave edildi.Hal hazirki mebleginiz:{self._Company__maas}")
class Developer(Company):
    def __init__(self,ad,maas,komanda_bonus):
        super().__init__(ad,maas)
        self.komanda_bonus=komanda_bonus
    def team_bonus(self):
        bonus=self.komanda_bonus*0.03*self._Company__maas
        self._Company__maas+=bonus
        print(f"{bonus} elave edildi.Hal hazirki mebleginiz:{self._Company__maas}")
class Intern(Company):
    def maas(self,ad,maas):
        maas.__init__(ad,maas)
        print(self.__maas)


m=Manager("Nihad",1000,15)
d=Developer("Elsen",2000,20)
i=Intern("Ferid",1200)

m.a()
d.a()
i.a()
m.team_bonus()
d.team_bonus()
