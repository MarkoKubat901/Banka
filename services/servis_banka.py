from models.banka import Banka
from models.korisnik import Korisnik
from models.racun import Racun
from models.enums import Valuta


class ServisBanka():
    def __init__(self):
        self.banka=Banka()

    def get_korisnik(self, username: str, lozinka: str) -> Korisnik:
        korisnik = next(korisnik for korisnik in self.banka.korisnici if korisnik.get_lozinka() == lozinka and korisnik.username == username)
        return korisnik

    def get_racuni_korisnika(self,ime:str,prezime:str):
        racuni_korisnika=list()
        vlasnik=ime+' '+prezime
        for racun in self.banka.racuni:
            if racun.vlasnik==vlasnik:
                racuni_korisnika.append(racun)
        return racuni_korisnika



    def ukupno_stanje_po_valutama(self):
        for racun in self.banka.racuni:
            if racun.valuta==Valuta.EUR:
                self.banka.suma_eur+=racun.get_stanje()
            if racun.valuta==Valuta.USD:
                self.banka.suma_usd+=racun.get_stanje()
            if racun.valuta==Valuta.RSD:
                self.banka.suma_rsd+=racun.get_stanje()