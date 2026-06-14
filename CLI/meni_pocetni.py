from CLI.meni_direktor import meni_direktor
from CLI.meni_klijent import meni_klijent
from CLI.meni_radnik import meni_radnik
from models.enums import TipKorisnika, TipRacuna, Valuta
from services.servis_banka import ServisBanka
from services.servis_racuna import ServisiRacuna
from services.servis_registracija import ServisRegistracija
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, FloatPrompt

console = Console()

def meni_registruj_se(servis:ServisRegistracija)->None :
    console.rule("[bold yellow]Registracija korisnika [/bold yellow]")

    tipovi = [t.value for t in TipKorisnika]

    console.print(f"Izaberite jednog od sledecih tipova korisnika:{','.join(f'[bold cyan]{t}[/bold cyan]' for t in tipovi)}")
    tip_unos=Prompt.ask("Tip korisnika",choices=tipovi)
    tip=TipKorisnika(tip_unos)
    ime=Prompt.ask("Ime")
    prezime=Prompt.ask("Prezime")
    username=Prompt.ask("Username")
    lozinka=Prompt.ask("Lozinka")
    servis.registracija(ime,prezime,username,lozinka,tip)
    console.print("[green]Uspesno ste registrovani [/green]")
    meni(ServisRegistracija())


def meni_loginuj_se(servis:ServisRegistracija)->None :
    servis_banka=ServisBanka()
    servis_racuna=ServisiRacuna()
    console.rule("[bold yellow]Loginuj se[/bold yellow]")
    username=Prompt.ask("Unesite username")
    lozinka=Prompt.ask("Unesite password")
    login=servis.login(username,lozinka)
    if login:
        console.print("[green] Uspesno ste ste loginovali [/green]")
        korisnik=servis_banka.get_korisnik(username,lozinka)

        if korisnik.tip==TipKorisnika.KLIJENT:
            meni_klijent(servis_banka,servis_racuna,korisnik)
        elif korisnik.tip==TipKorisnika.RADNIK:
            meni_radnik(korisnik)
        elif korisnik.tip==TipKorisnika.DIREKTOR:
            meni_direktor(korisnik)
    else:
        console.print("[red] Ovaj korisnik ne postoji[/red]\n")



def meni(servis:ServisRegistracija)->None   :
    while True:
        console.print(Panel(
            "[bold]1.[/bold] Loginuj se\n"
            "[bold]2.[/bold] Registruj se\n"
            "[bold]3.[/bold] Exit\n",

            title="[bold white]Meni[/bold white]",
            border_style="white",

        ))
        izbor=IntPrompt.ask("Odaberite opciju", choices=["1", "2", "3"])

        if izbor==1:
            meni_loginuj_se(servis)
        elif izbor==2:
            meni_registruj_se(servis)
        elif izbor==3:
            console.print("Izla iz menija")
            break

