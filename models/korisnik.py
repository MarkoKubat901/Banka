
from models.enums import TipKorisnika
from abc import ABC


class Korisnik(ABC):
    def __init__(self,ime,prezime,username,lozinka,tip:TipKorisnika):
        self.ime=ime
        self.prezime=prezime
        self.username=username
        self._lozinka=lozinka
        self.tip=tip

    def __str__(self):
        return f"{self.ime} {self.prezime} {self.username} {self._lozinka} "

    def get_lozinka(self):
        return self._lozinka
    def set_lozinka(self,nova_lozinka):
        self._lozinka=nova_lozinka

class Direktor(Korisnik):

    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.DIREKTOR)



class Radnik(Korisnik):

    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.RADNIK)


class Klijent(Korisnik):
    def __init__(self,ime,prezime,username,lozinka,):
        super().__init__(ime,prezime,username,lozinka,TipKorisnika.KLIJENT)







