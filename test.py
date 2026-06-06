from models import banka
from models.enums import TipRacuna,Valuta,StatusRacuna,TipKorisnika
from models.korisnik import Korisnik,Direktor
from models.racun import TipRacuna, TekuciRacuna,PoslovniRacuna,StatusRacuna
from models.banka import Banka

direktor=Direktor("Marko","Kubat","maki901","1234")
banka1=Banka()
print(direktor.pregled_transakcija())
