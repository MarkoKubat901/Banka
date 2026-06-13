from enum import Enum

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, FloatPrompt, Prompt

from CLI.pomocne_metode import prikazi_racune, prikazi_transakcije
from models.enums import TipRacuna, Valuta
from models.korisnik import Korisnik
from models.racun import Racun
from services.servis_korisnika import ServisiKorisnik
from services.servis_banka import ServisBanka
from services.servis_racuna import ServisiRacuna

console = Console()

def meni_klijent(servis_banka:ServisBanka,servis_racuna:ServisiRacuna,korisnik:Korisnik)->None:

    console.rule("[bold yellow][/bold yellow]")
    while True:

        console.print(Panel(
                            "[bold white]1.[/bold white]Prikazi racune\n"
                            "[bold white]2.[/bold white]Uplata na racun\n"
                            "[bold white]3.[/bold white]Isplata na racun\n"
                            "[bold white]4.[/bold white]Transfer na racun\n"
                            "[bold white]5.[/bold white]Pregeld istorije transakcija za svoje racune\n"
                            "[bold white]6.[/bold white]Promena lozinke\n"
                            "[bold white]7.[/bold white]exit\n",

                            title="[bold white]Meni-Klijent[/bold white]",
                            border_style="white",


        ))
        izbor=IntPrompt.ask("Odaberite opciju", choices=["1", "2", "3","4","5","6","7","8"])

        if izbor==1:
            meni_prikazi_racune(servis_banka,korisnik)
        elif izbor==2:
            meni_uplata(servis_racuna, servis_banka, korisnik)
        elif izbor==3:
            meni_isplata(servis_racuna, servis_banka, korisnik)
        elif izbor==4:
            pass
        elif izbor==5:
            meni_pregled_istorije_transakcija_racuna(servis_banka, korisnik)
        elif izbor==6:
            meni_promena_lozinke(korisnik)
        elif izbor==7:
            break

def meni_prikazi_racune(servis_banka:ServisBanka,korisnik:Korisnik):
    console.rule(f"[bold white]Prikaz racuna[/bold white]")
    racuni = servis_banka.get_racuni_korisnika(korisnik.ime, korisnik.prezime)
    if not racuni:
        console.print("[red] Ovaj korisnik nema otvoren racun[/red]")
        return
    console.print(prikazi_racune(racuni))
    izbor = IntPrompt.ask("Kliknite 1 da izadjete")
    if izbor==1:
        return
    else:
        console.print(f"[red]Uneli ste pogresan broj[/red]")

def meni_promena_lozinke( korisnik:Korisnik):
    console.rule(f"[bold white]Promena lozinke[/bold white]")
    nova_lozinka=Prompt.ask("Unesite novu lozinku ")
    console.print(f"Vas nova lozinka : {nova_lozinka}")
    izbor=IntPrompt.ask("Kliknite [bold green] 1 [/bold green]za potvrdu\n"
                        "Kliknite [bold red] 2 [/bold red] da otkazete\n")
    if izbor==1:
        korisnik.set_lozinka(nova_lozinka)
    elif izbor==2:
        return
    else:
        console.print(f"[red] Uneli ste neispravan broj[/red]")


def meni_pregled_istorije_transakcija_racuna( servis_banka, korisnik:Korisnik):
    console.rule(f"[bold white]Pregled istorije transakcija racuna[/bold white]")
    racuni = servis_banka.get_racuni_korisnika(korisnik.ime, korisnik.prezime)
    if not racuni:
        console.print("[red] Ovaj korisnik nema otvoren racun[/red]")
        return
    console.print(prikazi_racune(racuni))

    izbor = IntPrompt.ask("Unestie broj racuna")
    if izbor < 0 or izbor >= len(racuni):
        console.print("[red] Neispravan broj racuna[/red]")
        return

    racun = racuni[izbor]
    transakcije=racun.transakcije
    if not transakcije:
        console.print("[red] Ovaj racun nema izvrsene transakcije[/red]")
        return

    console.print(prikazi_transakcije(transakcije))






def meni_isplata(servis_racuna:ServisiRacuna,servis_banka:ServisBanka,korisnik:Korisnik)->None:
    console.rule(f"[bold white]Isplata[/bold white]")
    racuni=servis_banka.get_racuni_korisnika(korisnik.ime,korisnik.prezime)
    if not racuni:
        console.print("[red] Ovaj korisnik nema otvoren racun[/red]")
        return
    console.print(prikazi_racune(racuni))

    izbor=IntPrompt.ask("Unestie broj racuna")
    if izbor<0 or izbor>=len(racuni):
        console.print("[red] Neispravan broj racuna[/red]")
        return

    racun = racuni[izbor]
    console.print(f"Trenutno stanje racuna[bold yellow]: {racun.get_stanje()} {racun.valuta}[/bold yellow]")

    iznos=FloatPrompt.ask("Unestie iznos koji zelite da isplatite sa racuna")


    uspeh=servis_racuna.isplata_na_racun(racun,iznos)
    if uspeh:
        console.print(f"[bold green]Uspesno ste isplatili sumu. Novo stanje : {racun.get_stanje()}{racun.valuta.value}[/bold green]")
    else:
        console.print(f"[red]Isplata neuspesna[/red]")


def meni_uplata(servis_racuna:ServisiRacuna,servis_banka:ServisBanka,korisnik:Korisnik)->None:
    console.rule(f"[bold white]Uplata[/bold white]")

    racuni=servis_banka.get_racuni_korisnika(korisnik.ime,korisnik.prezime)

    if not racuni:
        console.print("[red] Ovaj korisnik nema otvoren racun[/red]")
        return
    console.print(prikazi_racune(racuni))

    izbor=IntPrompt.ask("Unestie broj racuna")
    if izbor<0 or izbor>=len(racuni):
        console.print("[red] Neispravan broj racuna[/red]")
        return
    racun = racuni[izbor]

    console.print(f"Trenutno stanje racuna[bold yellow]: {racun.get_stanje()} {racun.valuta}[/bold yellow]")
    iznos=FloatPrompt.ask("Unestie iznos koji zelite da uplatite sa racuna")

    uspeh=servis_racuna.uplata_na_racun(racun,iznos)
    if uspeh:
        console.print(f"[bold green]Uspesno ste uplatili sumu. Novo stanje : {racun.get_stanje()}{racun.valuta.value}[/bold green]")
    else:
        console.print(f"[red]Uplata neuspesna[/red]")

