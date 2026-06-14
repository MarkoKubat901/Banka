from abc import abstractmethod, ABC

from models import korisnik
from models.banka import Banka
from models.korisnik import Korisnik,Klijent
class ServisiKorisnik(ABC):
    def __init__(self):
        self.banka=Banka()



    def registracija_klijenta(self,ime:str,prezime:str,username:str,lozinka:str):
        nov_klijent=Klijent(ime=ime,prezime=prezime,username=username,lozinka=lozinka)
        self.banka.dodaj_klijenta(nov_klijent)









