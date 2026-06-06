from models.racun import Racun
class Banka():
    instance=None
    def __new__(cls):
        if cls.instance == None:
            cls.instance=super().__new__(cls)
        return cls.instance
    def __init__(self,):
        if not hasattr(self,'_inicijalizovana'):
            self._inicijalizovana=True
            self.racuni=[Racun]
            self.klijenti=[]
            self.transakcije=[]
