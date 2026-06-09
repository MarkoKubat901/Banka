from models.transakcija import Transakcija
from models.enums import TipRacuna,Valuta,StatusRacuna,TipKorisnika
from models.korisnik import Korisnik,Direktor
from models.racun import TipRacuna, TekuciRacuna,PoslovniRacuna,StatusRacuna
from models.banka import Banka

banka1=Banka()
racun1=TekuciRacuna("marko901",Valuta.RSD,2000)
racun2=TekuciRacuna("marko901",Valuta.EUR,3000)

direktor1=Direktor("Marko","Kubat","marko123","1234")
banka1.racuni.append(racun1)

print(direktor1.pregled_svih_racuna())



