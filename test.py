from models.transakcija import Transakcija
from models.enums import TipRacuna,Valuta,StatusRacuna,TipKorisnika
from models.korisnik import Korisnik, Direktor, Klijent
from models.racun import TipRacuna, TekuciRacun,PoslovniRacun,StatusRacuna,Racun,StedniRacun
from models.banka import Banka
from services.servis_kamata import ServisKamata, ProstaKamata
from services.servis_banka import ServisBanka
from services.servis_registracija import ServisRegistracija
from services.servis_korisnika import ServisiKorisnik
from CLI.meni_pocetni import meni

servis=ServisRegistracija()
meni(servis)












