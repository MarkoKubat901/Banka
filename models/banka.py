from dataclasses import dataclass

from models.korisnik import Klijent
from models.racun import Racun
from models.transakcija import Transakcija


class Banka():
    instance=None
    def __new__(cls):
        if cls.instance == None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self,):
        if not hasattr(self,'_inicijalizovana'):
            self._inicijalizovana=True
            self.racuni=[]
            self.klijenti=[]
            self.transakcije=[]
            self.suma_rsd=0.0
            self.suma_eur=0.0
            self.suma_usd=0.0

    def __str__(self):
        return f"Stanje u RSD: {self.suma_rsd} Stanje u EUR: {self.suma_eur} Stanje u USD: {self.suma_usd}"

    def dodaj_racun(self,racun:Racun):
        self.racuni.append(racun)

    def dodaj_klijenta(self,klijent:Klijent):
        self.klijenti.append(klijent)
    def doda_transakciju(self,transakcija:Transakcija):
        self.transakcije.append(transakcija)
