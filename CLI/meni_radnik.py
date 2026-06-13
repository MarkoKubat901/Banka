
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, FloatPrompt, Prompt

from CLI.meni_klijent import meni_promena_lozinke
from CLI.pomocne_metode import prikazi_racune, prikazi_klijente
from models.enums import TipRacuna, Valuta
from services.servis_korisnika import ServisiKorisnik
from services.servis_banka import ServisBanka
from services.servis_racuna import ServisiRacuna
console = Console()

def meni_radnik(korisnik):
    while True:
        servis_racuna = ServisiRacuna()
        servis_banka = ServisBanka()
        servis_korisnik = ServisiKorisnik()
        console.rule("[bold yellow][/bold yellow]")

        console.print(Panel(
                            "[bold white]1.[/bold white]Otvori racun\n"
                            "[bold white]2.[/bold white]Blokiraj racun\n"
                            "[bold white]3.[/bold white]Odblokiraj racun\n"
                            "[bold white]4.[/bold white]Registruj klijenta\n"
                            "[bold white]5.[/bold white]Pregled klijenta i njihovih racuna\n"
                            "[bold white]6.[/bold white]Promena lozinke\n"
                            "[bold white]7.[/bold white]exit\n",

                            title="[bold white]Meni-Radnik[/bold white]",
                            border_style="white",

                            ))
        izbor = IntPrompt.ask("Odaberite opciju", choices=["1", "2", "3", "4", "5", "6", "7", "8"])
        if izbor==1:
            meni_otvori_racun(servis_racuna,)
        elif izbor==2:
            meni_blokiraj_racun(servis_racuna,servis_banka)
        elif izbor==3:
            meni_odblokiraj_racun(servis_racuna,servis_banka)
        elif izbor==4:
            meni_registruj_klijenta(servis_korisnik,servis_banka)
        elif izbor==5:
            meni_pregled_klijenata_i_njihovih_racuna(servis_banka)
        elif izbor==6:
            meni_promena_lozinke(korisnik)
        elif izbor==7:
            break


def meni_pregled_klijenata_i_njihovih_racuna(servis_banka:ServisBanka)->None:
    console.rule(f"[bold white]Pregled-Racuna-Klijenta[/bold white]")
    klijenti=servis_banka.banka.klijenti
    if not klijenti:
        console.print(f"[white]Trenutno banka nema klijenata   [/white]")
        return
    console.print(prikazi_klijente(klijenti))
    unos=IntPrompt.ask("Unesite broj klijenta za kojeg zelite da izvrsite pregled racuna")
    klijent=servis_banka.banka.klijenti[unos]
    racuni=servis_banka.get_racuni_korisnika(klijent.ime,klijent.prezime)
    if not racuni:
        console.print(f"[white]Ovaj klijent nema otvoren racuna[/white]")
        return
    console.print(prikazi_racune(racuni))





def meni_registruj_klijenta(servis_korisnik:ServisiKorisnik,servis_banka:ServisBanka)->None:
    console.rule(f"[bold white]Registracija klijenta[/bold white]")
    ime=Prompt.ask("Ime klijenta")
    prezime=Prompt.ask("Prezime klijenta")
    username=Prompt.ask("Username klijenta")
    lozinka=Prompt.ask("Lozinka klijenta")
    servis_korisnik.registracija_klijenta(ime,prezime,username,lozinka)
    console.print(f"[green]Uspesno ste registrovali klijenta")

def meni_otvori_racun(servis_racuna:ServisiRacuna)->None:

    console.rule("[bold blue]Otvaranje novog racuna[/bold blue]")
    vlasnik=Prompt.ask("Ime i prezime vlasnika")
    tipovi=[t.value for t in TipRacuna]
    console.print(f"Dostupni tipovi: {', '.join(f'[cyan]{t}[/cyan]' for t in tipovi)}")
    tip_unos=Prompt.ask("Tipovi racuna",choices=tipovi)
    tip=TipRacuna(tip_unos)

    valute=[v.value for v in Valuta]
    console.print(f"Dozvoljene valute:{', '.join(f'[cyan]{v}[/cyan]' for v in valute)}")
    valuta_unos=Prompt.ask("Valuta racuna",choices=valute)
    valuta=Valuta(valuta_unos)

    pocetni_iznos=FloatPrompt.ask("Pocetni iznos",default=0.0)
    racun=servis_racuna.otvori_racun(vlasnik,tip,valuta,pocetni_iznos=pocetni_iznos)
    console.print(f"[green]Racun uspesno otvoren za {racun.vlasnik}-{racun.tip.value}-{racun.valuta.value}[/green]")

def meni_blokiraj_racun(servis_racuna:ServisiRacuna,servis_banka:ServisBanka,)->None:
    console.rule(f"[bold white]Meni-Blokiraj-racun[/bold white]")
    racuni =servis_banka.banka.racuni
    if not racuni:
        console.print("[red] Trenutno nema otvorenih racuna[/red]")
        return
    console.print(prikazi_racune(racuni))

    izbor = IntPrompt.ask("Unestie broj racuna")
    if izbor < 0 or izbor >= len(racuni):
        console.print("[red] Neispravan broj racuna[/red]")
        return

    racun = racuni[izbor]

    uspeh=servis_racuna.blokiranje_racuna(racun)
    if uspeh:
        console.print(f"[bold green]Racun je uspesno blokiran[/bold green]")
        console.print(prikazi_racune(racuni))
    else:
        console.print(f"Racun ne moze da se  blokira")

def meni_odblokiraj_racun(servis_racuna:ServisiRacuna,servis_banka:ServisBanka,)->None:
    console.rule(f"[bold white]Meni-Odblokiraj-racun[/bold white]")
    racuni =servis_banka.banka.racuni
    if not racuni:
        console.print("[red] Trenutno nema otvorenih racuna[/red]")
        return
    console.print(prikazi_racune(racuni))

    izbor = IntPrompt.ask("Unestie broj racuna")
    if izbor < 0 or izbor >= len(racuni):
        console.print("[red] Neispravan broj racuna[/red]")
        return

    racun = racuni[izbor]

    uspeh=servis_racuna.odblokiranje_racuna(racun)
    if uspeh:
        console.print(f"[bold green]Racun je uspesno odblokiran[/bold green]")
        console.print(prikazi_racune(racuni))
    else:
        console.print(f"Racun ne mozeda se  odblokira")


