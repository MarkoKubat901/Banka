from models.banka import Banka
from models.racun import Racun
from models.enums import Valuta


class ServisBanka():
    def __init__(self):
        self.banka=Banka()

    def pregled_svih_racuna(self):
        return self.banka.racuni

    def pregled_svih_transakcija(self):
        return self.banka.transakcije

    def pregled_svih_klijenata(self):
        return self.banka.klijenti

    def ukupno_stanje_po_valutama(self):
        for racun in self.banka.racuni:
            if racun.valuta==Valuta.EUR:
                self.banka.suma_eur+=racun.get_stanje()
            if racun.valuta==Valuta.USD:
                self.banka.suma_usd+=racun.get_stanje()
            if racun.valuta==Valuta.RSD:
                self.banka.suma_rsd+=racun.get_stanje()