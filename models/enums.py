from enum import Enum
from os import name
class TipKorisnika(Enum):
    DIREKTOR='direktor'
    RADNIK='radnik'
    KLIJENT='klijent'



class TipRacuna(Enum):
    TEKUCI="tekuci"
    STEDNI="stedni"
    POSLOVNI="poslovni"

class Valuta(Enum):
    RSD= 'RSD'
    EUR= 'EUR'
    USD= 'USD'

class StatusRacuna(Enum):
    AKTIVAN= 'aktivan'
    BLOKIRAN="blokiran"
    ZATVOREN="zatvoren"

    def dozvoljen_prelaz(self,):
        prelaz ={
            StatusRacuna.AKTIVAN:[StatusRacuna.BLOKIRAN,StatusRacuna.ZATVOREN],
            StatusRacuna.BLOKIRAN:[StatusRacuna.ZATVOREN,StatusRacuna.AKTIVAN],
            StatusRacuna.ZATVOREN:[]
        }
        return prelaz[self]

    def mozne_prelaz(self,novo:StatusRacuna)->bool:
        return True if novo in self.dozvoljen_prelaz() else False


