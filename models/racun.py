from abc import ABC ,abstractmethod
from models.enums import StatusRacuna,Valuta,TipRacuna
class Racun(ABC):
    def __init__(self,korisnik:str,tip: TipRacuna,valuta: Valuta,stanje:float=0.0,) -> None:
        self.korisnik=korisnik
        self.tip=tip
        self.valuta=valuta
        self._stanje=stanje
        self.status=StatusRacuna.AKTIVAN
    @property
    def stanje(self):
        return self._stanje
    @abstractmethod
    def isplata(self,iznos):
        pass
    @abstractmethod
    def uplata(self,iznos):
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False





class TekuciRacuna(Racun):
    def __init__(self, korisnik: str, valuta: Valuta, stanje: float = 0.0, ) -> None:
        super().__init__(korisnik, TipRacuna.TEKUCI,valuta,stanje)

    def isplata(self,iznos):
        try:
            if iznos>self._stanje:
                raise ValueError("Ne mozete isplatiit iznos koji je veco od trenutnog stanja")
            if iznos <=0:
                raise ValueError("Isplate ne moze biti manja ili jednaka od nule")
            self._stanje-=iznos
            return True
        except ValueError as e:
            print(e)
            return False

    def uplata(self,iznos):
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False

class StedniRacun(Racun):
    def __init__(self, korisnik: str, valuta: Valuta, stanje: float, ) -> None:
        super().__init__(korisnik,TipRacuna.STEDNI,valuta,stanje)

    def isplata(self, iznos):
        iznos_uz_kamatu=iznos*1.03
        try:
            if iznos_uz_kamatu > self._stanje:
                raise ValueError("Ne mozete isplatiit iznos koji je veco od trenutnog stanja")
            if iznos <= 0:
                raise ValueError("Isplate ne moze biti manja ili jednaka od nule")
            self._stanje -= iznos_uz_kamatu
            return True
        except ValueError as e:
            print(e)
            return False

    def uplata(self,iznos):
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False

class PoslovniRacuna(Racun):
    def __init__(self, korisnik: str, valuta: Valuta, stanje: float, ) -> None:
        super().__init__(korisnik,TipRacuna.POSLOVNI,valuta,stanje)

    def isplata(self, iznos):
        dozvoljen_minus=50000
        try:
            if iznos > self._stanje+dozvoljen_minus:
                raise ValueError("Prekoracili ste minus")
            if iznos <= 0:
                raise ValueError("Isplate ne moze biti manja ili jednaka od nule")
            self._stanje -= iznos
            return True
        except ValueError as e:
            print(e)
            return False

    def uplata(self,iznos):
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False