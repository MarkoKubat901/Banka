from models.banka import Banka
from models.enums import TipKorisnika
from models.korisnik import Korisnik, Radnik, Klijent, Direktor


class ServisRegistracija():
    def __init__(self):
        self.banka=Banka()
    _factory:dict[TipKorisnika,type[Korisnik]] = {
        TipKorisnika.RADNIK:Radnik,
        TipKorisnika.KLIJENT:Klijent,
        TipKorisnika.DIREKTOR:Direktor,

    }

    def registracija(self,ime:str,prezime:str,username:str,lozinka:str,tip:TipKorisnika,**kwargs)->Korisnik:
        klasa=self._factory.get(tip)
        if klasa is None:
            raise ValueError(f"Klasa ne postoji")
        nov_korisnik=klasa(ime=ime,prezime=prezime,username=username,lozinka=lozinka,**kwargs)
        self.banka.dodaj_korisnika(nov_korisnik)
        return nov_korisnik

    def login(self,username:str,lozinka:str)->bool:
        for korisnik in self.banka.korisnici:
            if korisnik.username==username and korisnik.get_lozinka()==lozinka:
                return True
        return False



