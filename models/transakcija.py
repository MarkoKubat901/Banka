
from models.racun import Racun
from datetime import datetime

class Transakcija():
    def __init__(self,posaljilac:Racun,primalac:Racun,iznos:float):
        #Stavio sam da atributi klase budu privatni zbog integriteta
        self._iznos=iznos
        self._posaljilac=posaljilac
        self._primalac=primalac
        #dodao sam datum i vreme transakcija kako bi se vrsila bolja evidencija o transakcijama u izvestaju
        self.datum=datetime.now()

    @property
    def iznos(self):
        return self._iznos

    @property
    def posaljilac(self):
        return self._posaljilac

    @property
    def primalac(self):
        return self._primalac







