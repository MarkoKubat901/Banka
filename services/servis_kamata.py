from abc import ABC, abstractmethod
from models.racun import Racun,StedniRacun
from models.enums import TipRacuna
from typing import Protocol

#Ovde se primenjuje strategy design pattern
#Ovo je blueprint kasnije dodaj parametre  za formule za obe strategije,pitaj kako se primenjuje kamatat

class KamataStrategy(ABC):
    @abstractmethod
    def primena(self,glavnica:float,kamatna_stopa:int,godine:int)->float:
        pass

class ProstaKamata(KamataStrategy):

    def primena(self,glavnica:float,kamatna_stopa,godine:int)->float:
        iznos=glavnica+((glavnica*kamatna_stopa*godine)/100)
        return iznos


class SlozenaKamata(KamataStrategy):

    def primena(self,glavnica:float,kamatna_stopa:int,godine:int)->float:
        q=1+kamatna_stopa/100
        iznos=glavnica*(q**godine)
        return iznos

class IzracunajKamatuProces():
    def __init__(self, racun: StedniRacun, godine: int, strategy: type[KamataStrategy]) -> None:
        self.strategy = strategy
        self.racun = racun
        self.godine = godine

    def set_strategy(self, strategy: type[KamataStrategy]) -> None:
        self.strategy = strategy

    def izvrsi_strategy(self):
        return self.strategy.primena(self.racun.get_stanje(),self.racun.kamatna_stopa,self.godine)

class ServisKamata():
    def izracunaj_kamatu(self,racun: StedniRacun, godine: int, strategy: type[KamataStrategy]):
       return IzracunajKamatuProces(racun, godine, strategy).izvrsi_strategy()







