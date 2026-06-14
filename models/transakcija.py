from dataclasses import dataclass, field
from datetime import datetime
from models.enums import Valuta

@dataclass
class Transakcija():
    racun_id:str
    vlasnik:str
    tip:str
    iznos:float
    valuta:Valuta
    vreme:datetime=field(default_factory=datetime.now)

    def __str__(self)->str:
        return f"{self.racun_id} {self.vlasnik} {self.tip} {self.iznos}"









