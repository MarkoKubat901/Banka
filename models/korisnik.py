import string

from models.racun import Racun
from models.banka import Banka
from models.enums import TipKorisnika,Valuta
from abc import ABC, abstractmethod

from models.racun import Racun


class Korisnik(ABC):
    def __init__(self,ime,prezime,username,lozinka,tip:TipKorisnika):
        self.ime=ime
        self.prezime=prezime
        self.username=username
        self.lozinka=lozinka
        self.tip=tip
    @abstractmethod
    def promena_lozinke(self, nova: string):
        self.lozinka = nova
        return True

class Direktor(Korisnik):
    banka_racuni=Banka().racuni
    banka_klijenti=Banka().klijenti
    banka_transakcije=Banka().transakcije
    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.DIREKTOR)

    def promena_lozinke(self, nova: string):
        self.lozinka = nova
        return True
    def pregled_racuna(self):
        return self.banka_racuni
    def pregled_transakcija(self):
        return self.banka_transakcije
    def blokirnaje_racuna(self,racun:Racun):
        pass
    def odblokirnaje_racuna(self,racun:Racun):
        pass
    def pregled_klijenata(self):
        return self.banka_klijenti
    def izvestaj(self,valuta:Valuta):
        stanje=0
        for racun in self.banka_racuni:
            if racun.valuta==valuta:
                stanje==racun.stanje

