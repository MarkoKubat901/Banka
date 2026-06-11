from models.transakcija import Transakcija
from models.enums import TipRacuna,Valuta,StatusRacuna,TipKorisnika
from models.korisnik import Korisnik, Direktor, Klijent
from models.racun import TipRacuna, TekuciRacun,PoslovniRacun,StatusRacuna,Racun,StedniRacun
from models.banka import Banka
from services.servis_racuna import ServisiRacuna
from services.servis_banka import ServisBanka
from services.servis_korisnika import ServisiKorisnik
banka1 = Banka()
racun1=StedniRacun("Pera","Kvrzica",Valuta.EUR,70000)
racun2=StedniRacun("Marko","Kubat",Valuta.RSD,500)

korisnik=Klijent("Marko","Kubat","okram901",123)
servis=ServisiRacuna()

servis.otvori_racun("Dejan","Bora",TipRacuna.POSLOVNI,Valuta.RSD,5620)
servis.otvori_racun("Marko","Kubat",TipRacuna.STEDNI,Valuta.EUR,500)
servis.otvori_racun("Marko","Kubat",TipRacuna.STEDNI,Valuta.EUR,600)
servis_banka=ServisBanka()
servis_banka.ukupno_stanje_po_valutama()
print(banka1)










