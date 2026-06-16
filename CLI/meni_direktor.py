
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from CLI.meni_klijent import meni_promena_lozinke
from CLI.meni_radnik import meni_blokiraj_racun, meni_odblokiraj_racun
from CLI.pomocne_metode import prikazi_racune, prikazi_klijente, prikazi_transakcije, prikazi_izvestaj
from models.korisnik import Korisnik
from services.servis_banka import ServisBanka
from services.servis_racuna import ServisiRacuna

console = Console()

def meni_direktor(korisnik:Korisnik):
    while True:
        servis_racuna = ServisiRacuna()
        servis_banka = ServisBanka()
        console.rule("[bold yellow][/bold yellow]")

        console.print(Panel(
            "[bold white]1.[/bold white]Pregled svih racuna\n"
            "[bold white]2.[/bold white]Pregled svih transakcija\n"
            "[bold white]3.[/bold white]Blokiraj racun\n"
            "[bold white]4.[/bold white]Odblokiraj racun\n"
            "[bold white]5.[/bold white]Pregled svih klijenta \n"
            "[bold white]6.[/bold white]Izvestaj\n"
            "[bold white]7.[/bold white]Promena lozinke\n"
            "[bold white]8.[/bold white]exit\n",

            title="[bold white]Meni-Direktor[/bold white]",
            border_style="white",

        ))
        izbor = IntPrompt.ask("Odaberite opciju", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

        if izbor==1:
            meni_pregled_svih_racuna(servis_banka)
        elif izbor==2:
            meni_pregled_svih_transakcija(servis_banka)
        elif izbor==3:
            meni_blokiraj_racun(servis_racuna,servis_banka)
        elif izbor==4:
            meni_odblokiraj_racun(servis_racuna,servis_banka)
        elif izbor==5:
            meni_pregled_klijenata(servis_banka)
        elif izbor==6:
            meni_izvestaj(servis_banka)
        elif izbor==7:
            meni_promena_lozinke(korisnik)
        elif izbor==8:
            break

def meni_izvestaj(servis_banka):
    console.rule("[bold yellow][/bold yellow]")
    servis_banka.ukupno_stanje_po_valutama()
    stanje_RSD = servis_banka.banka.suma_rsd
    stanje_EUR = servis_banka.banka.suma_eur
    stanje_USD = servis_banka.banka.suma_usd
    console.print(prikazi_izvestaj(stanje_RSD, stanje_EUR, stanje_USD))



def meni_pregled_klijenata(servis_banka:ServisBanka):
    console.rule("[bold yellow][/bold yellow]")
    klijenti = servis_banka.banka.klijenti
    if not klijenti:
        console.rule("[bold yellow]U banci trenutno nema izvrsenih transakcija[/bold yellow]")
        return
    console.print(prikazi_klijente(klijenti))
    izbor=IntPrompt.ask("Kliknite[cyan] 1 [/cyan]da izadjete")
    if izbor==1:
        return


def meni_pregled_svih_transakcija(servis_banka):
    console.rule("[bold yellow][/bold yellow]")
    transakcije = servis_banka.banka.transakcije
    if not transakcije:
        console.rule("[bold yellow]U banci trenutno nema izvrsenih transakcija[/bold yellow]")
        return
    console.print(prikazi_transakcije(transakcije))
    izbor = IntPrompt.ask("Kliknite[cyan] 1 [/cyan]da izadjete")
    if izbor == 1:
        return


def meni_pregled_svih_racuna(servis_banka):
    console.rule("[bold yellow][/bold yellow]")
    racuni = servis_banka.banka.racuni
    if not racuni:
        console.rule("[bold yellow]U banci trenutno nema racuna[/bold yellow]")
        return
    console.print(prikazi_racune(racuni))
    izbor = IntPrompt.ask("Kliknite[cyan] 1 [/cyan]da izadjete")
    if izbor == 1:
        return
