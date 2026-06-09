from models.banka import Banka
from models.enums import TipKorisnika
from abc import ABC, abstractmethod
from models.enums import StatusRacuna
from models.racun import Racun



class Korisnik(ABC):
    def __init__(self,ime,prezime,username,lozinka,tip:TipKorisnika):
        self.ime=ime
        self.prezime=prezime
        self.username=username
        self._lozinka=lozinka
        self.tip=tip
    @abstractmethod
    def promeni_lozinku(self,nova_lozinka):
        self._lozinka=nova_lozinka


class Direktor(Korisnik):

    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.DIREKTOR)
        self.banka=Banka()

    def promeni_lozinku(self,nova_lozinka):
        self._lozinka=nova_lozinka



class Radnik(Korisnik):

    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.RADNIK)

    def promeni_lozinku(self,nova_lozinka):
        self._lozinka=nova_lozinka



class Klijent(Korisnik):
    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.KLIJENT)

    def promeni_lozinku(self,nova_lozinka):
        self._lozinka=nova_lozinka






