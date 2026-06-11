from dataclasses import dataclass, field
from models.racun import Racun
from datetime import datetime
from models.enums import Valuta

@dataclass
class Transakcija():
    racun:str
    vlasnik:str
    tip:str
    iznos:float
    valuta:Valuta
    vreme:datetime=field(default_factory=datetime.now)

    def __str__(self)->str:
        return f"{self.racun} {self.vlasnik} {self.tip} {self.iznos}"









