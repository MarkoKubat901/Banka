from abc import abstractmethod, ABC

from models import korisnik
from models.banka import Banka
from models.korisnik import Korisnik,Klijent
from services.servis_banka import ServisBanka


class ServisiKorisnik(ABC):
    def __init__(self):
        self.banka_servis=ServisBanka()

    def registracija_klijenta(self,ime:str,prezime:str,username:str,lozinka:str):
        nov_klijent=Klijent(ime=ime,prezime=prezime,username=username,lozinka=lozinka)
        self.banka_servis.dodaj_klijenta(nov_klijent)









