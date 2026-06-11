
from models.enums import Valuta,StatusRacuna
from models.racun import TipRacuna, PoslovniRacun, TekuciRacun, StedniRacun, Racun

from models.banka import Banka

class ServisiRacuna():
    def __init__(self,):
        self.banka=Banka()
#Ovde se primenjuje Factory design pattern
    _factory : dict[TipRacuna,type[Racun]]={
        TipRacuna.TEKUCI:TekuciRacun,
        TipRacuna.STEDNI:StedniRacun,
        TipRacuna.POSLOVNI:PoslovniRacun,
    }
    def otvori_racun(self,ime:str,prezime:str,tip:TipRacuna,valuta:Valuta,pocetni_iznos:float=0.0,**kwargs) -> Racun:
        klasa=self._factory.get(tip)
        if klasa is None:
            raise ValueError("Ovaj racun ne postoji")
        racun=klasa(ime=ime,prezime=prezime,valuta=valuta,stanje=pocetni_iznos,**kwargs)
        self.banka.dodaj_racun(racun)
        return racun




#Da li je ovo korektna upotrba state patterna,ako se sistem skalira ovaj nacin sadrzi puno if/elif

    def uplata_na__racun(self,racun:Racun,iznos:float)->Racun:
        if racun.get_status()==StatusRacuna.ZATVOREN:
            raise ValueError("Na ovaj racun se ne moze izvrsiti uplata")
        racun.uplata(iznos=iznos)
        return racun

    def isplata_na__racun(self,racun:Racun,iznos:float)->Racun:
        try:
            if racun.get_status()==StatusRacuna.BLOKIRAN or StatusRacuna.ZATVOREN:
                 raise ValueError("Na ovaj racun ne moze da se izvrsi isplatu")
            racun.isplata(iznos=iznos)
            return racun
        except ValueError as e:
                print(e)
        return racun

    def blokiranje_racuna(self,racun:Racun)->Racun:
        try:
            if not racun.get_status().moze_prelaz(StatusRacuna.BLOKIRAN):
                raise ValueError(f"Ovaj racun ne mozeda se blokira ili je vec blokiran")
            racun.set_status(StatusRacuna.BLOKIRAN)
        except ValueError as e:
                print(e)
        return racun

    def odblokiranje_racuna(self,racun:Racun)->Racun:
        try:
            if not racun.get_status().moze_prelaz(StatusRacuna.AKTIVAN):
                raise ValueError(f"Ovaj racun ne mozeda se odblokira ili je vec odblokiran")
            racun.set_status(StatusRacuna.AKTIVAN)
        except ValueError as e:
             print(e)
        return racun





