
class Banka():
    instance=None
    def __new__(cls):
        if cls.instance == None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self,):
        if not hasattr(self,'_inicijalizovana'):
            self._inicijalizovana=True
            self.racuni=[]
            self.klijenti=[]
            self.korisnici=[]
            self.transakcije=[]
            self.suma_rsd=0.0
            self.suma_eur=0.0
            self.suma_usd=0.0





