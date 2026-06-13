from abc import ABC ,abstractmethod
from uuid import uuid4
from models.enums import StatusRacuna,Valuta,TipRacuna
class Racun(ABC):
    def __init__(self,vlasnik:str,tip: TipRacuna,valuta: Valuta,stanje:float=0.0,) -> None:
        self.id=uuid4()
        self.vlasnik=vlasnik
        self.tip=tip
        self.valuta=valuta
        self._stanje=stanje
        self._status=StatusRacuna.AKTIVAN
        self.transakcije=[]



    def get_status(self) :
        return self._status

    def set_status(self,novi_status:StatusRacuna):
        self._status=novi_status

    def get_stanje(self) :
        return self._stanje

    def set_stanje(self,novo_stanje:float):
        self._stanje=novo_stanje


    @abstractmethod
    def __str__(self)->str:
        return f"{self.vlasnik}{self.tip} {self.valuta} {self.get_stanje()}"

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


class TekuciRacun(Racun):

    def __init__(self, vlasnik: str, valuta: Valuta, stanje: float = 0.0, ) -> None:
        super().__init__(vlasnik, TipRacuna.TEKUCI,valuta,stanje)

    def __str__(self) -> str:
        return f"{self.vlasnik}  {self.tip} {self.valuta} {self.get_stanje()}  {self._status}"

    def isplata(self,iznos:float):
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

    def uplata(self,iznos:float)->bool:
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False


class StedniRacun(Racun):

    def __init__(self, vlasnik: str, valuta: Valuta, stanje:float = 0.0, kamatna_stopa=3) -> None:
        super().__init__(vlasnik,TipRacuna.STEDNI,valuta,stanje)
        self.kamatna_stopa=kamatna_stopa

    def __str__(self) -> str:
        return f"{self.vlasnik} {self.tip} {self.valuta} {self.get_stanje()} {self._status} Kamatna stopa : {self.kamatna_stopa}"


    def isplata(self, iznos:float)->bool:
        try:
            if iznos > self._stanje:
                raise ValueError("Ne mozete isplatiit iznos koji je veco od trenutnog stanja")
            if iznos <= 0:
                raise ValueError("Isplate ne moze biti manja ili jednaka od nule")
            self._stanje -= iznos
            return True
        except ValueError as e:
            print(e)
            return False

    def uplata(self,iznos:float)->bool:
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False

class PoslovniRacun(Racun):

    def __init__(self, vlasnik: str, valuta: Valuta, stanje: float = 0.0,dozvoljeni_minus=50000 ) -> None:
        super().__init__(vlasnik,TipRacuna.POSLOVNI,valuta,stanje)
        self.dozvoljeni_minus=dozvoljeni_minus

    def __str__(self) -> str:
        return f"{self.vlasnik}  {self.tip} {self.valuta} {self.get_stanje()} {self._status} Dozvoljeni minus : {self.dozvoljeni_minus}"

    def isplata(self, iznos:float)->bool:

        try:
            if iznos > self._stanje+self.dozvoljeni_minus:
                raise ValueError("Prekoracili ste minus")
            if iznos <= 0:
                raise ValueError("Isplate ne moze biti manja ili jednaka od nule")
            self._stanje -= iznos
            return True
        except ValueError as e:
            print(e)
            return False

    def uplata(self,iznos:float)->bool:
        try:
            if iznos<=0:
                raise ValueError("Ne mozete uplatiti negativnu vrednost")
            self._stanje+=iznos
            return True
        except ValueError as e:
            print(e)
            return False