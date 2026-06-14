
from models.enums import Valuta,StatusRacuna
from models.racun import TipRacuna, PoslovniRacun, TekuciRacun, StedniRacun, Racun
from models.banka import Banka
from models.transakcija import Transakcija
from services.servis_banka import ServisBanka


class ServisiRacuna():
    def __init__(self,):
        self.banka_servis=ServisBanka()
#Ovde se primenjuje Factory design pattern
    _factory : dict[TipRacuna,type[Racun]]={
        TipRacuna.TEKUCI:TekuciRacun,
        TipRacuna.STEDNI:StedniRacun,
        TipRacuna.POSLOVNI:PoslovniRacun,
    }
    def otvori_racun(self,vlasnik:str,tip:TipRacuna,valuta:Valuta,pocetni_iznos:float=0.0,**kwargs) -> Racun:
        klasa=self._factory.get(tip)
        if klasa is None:
            raise ValueError("Ovaj racun ne postoji")
        racun=klasa(vlasnik=vlasnik,valuta=valuta,stanje=pocetni_iznos,**kwargs)
        self.banka_servis.dodaj_racun(racun)
        return racun




#Da li je ovo ipravna upotreba state patterna ?,ako se sistem skalira ovaj nacin sadrzi puno if/elif, nije optimalan

    def uplata_na_racun(self,racun:Racun,iznos:float)->bool:
        try:
            if racun.get_status()==StatusRacuna.ZATVOREN:
                raise ValueError("Na ovaj racun se ne moze izvrsiti uplata")
        except ValueError as e:
            print(e)

        uspeh=racun.uplata(iznos)
        if uspeh:
            t = Transakcija(racun_id=racun.id, vlasnik=racun.vlasnik, tip="uplata", iznos=iznos,valuta=racun.valuta)
            racun.transakcije.append(t)
            self.banka_servis.dodaj_transakciju(t)
        return uspeh


    def isplata_na_racun(self,racun:Racun,iznos:float)->bool:
        if racun.get_status()== StatusRacuna.BLOKIRAN or racun.get_status()==StatusRacuna.ZATVOREN:
             raise ValueError("Na ovaj racun ne moze da se izvrsi isplatu")
        uspeh=racun.isplata(iznos)
        if uspeh:
            t=Transakcija(racun_id=racun.id,vlasnik=racun.vlasnik,tip="isplata",iznos=iznos,valuta=racun.valuta)
            racun.transakcije.append(t)
            self.banka_servis.dodaj_transakciju(t)
        return uspeh

    def transfer(self,racun1:Racun,racun2:Racun,iznos)->bool:
        uspeh_isplata=self.isplata_na_racun(racun1,iznos)
        uspeh_uplata=self.uplata_na_racun(racun2,iznos)
        if uspeh_isplata and uspeh_uplata:
            return True
        else:
            return False



    def blokiranje_racuna(self,racun:Racun)->bool:
        uspeh=racun.get_status().moze_prelaz(StatusRacuna.BLOKIRAN)
        if uspeh:
            racun.set_status(StatusRacuna.BLOKIRAN)
        return uspeh


    def odblokiranje_racuna(self,racun:Racun)->bool:
        uspeh=racun.get_status().moze_prelaz(StatusRacuna.AKTIVAN)
        if uspeh:
            racun.set_status(StatusRacuna.AKTIVAN)
        return uspeh






