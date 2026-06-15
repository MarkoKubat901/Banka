from rich.table import Table


def prikazi_racune(racuni:list)->Table:
    tabela=Table(title="[bold]Lista racuna[/bold]")
    tabela.add_column("id",style="dim")
    tabela.add_column("Vlasnik")
    tabela.add_column("Tip")
    tabela.add_column("Stanje",style="white")
    tabela.add_column("Valuta")
    tabela.add_column("Status")
    for i,racun in enumerate(racuni):
        tabela.add_row(str(i),
                       racun.vlasnik,
                       racun.tip.value,
                       str(racun.get_stanje()),
                       racun.valuta.value,
                       racun.get_status().value

        )
    return tabela

def prikazi_izvestaj(stanje_RSD,stanje_EUR,stanje_USD)->Table:
    tabela=Table(title="[bold] Izvestaj[/bold]")
    tabela.add_column("Ukupno stanje u RSD",style="dim")
    tabela.add_column("Ukupno stanje u EUR", style="dim")
    tabela.add_column("Ukupno stanje u USD", style="dim")
    tabela.add_row(str(stanje_RSD),str(stanje_EUR),str(stanje_USD))
    return tabela


def prikazi_klijente(klijenti:list)->Table:
    tabela=Table(title="[bold]Lista klijenta[/bold]")
    tabela.add_column("id",style="dim")
    tabela.add_column("Ime")
    tabela.add_column("Prezime")
    tabela.add_column("Username",style="white")
    tabela.add_column("lozinka")
    tabela.add_column("Tip")
    for i,klijent in enumerate(klijenti):
        tabela.add_row(str(i),
                       klijent.ime,
                       klijent.prezime,
                       klijent.username,
                       klijent.get_lozinka(),
                       klijent.tip.value,

        )
    return tabela

def prikazi_transakcije(transakcije:list)->Table:
    tabela = Table(title="[bold]Lista transakcija[/bold]")
    tabela.add_column("#", style="dim")
    tabela.add_column("Racun id", style="dim")
    tabela.add_column("Vlasnik")
    tabela.add_column("Tip")
    tabela.add_column("Iznos", style="white")
    tabela.add_column("Valuta")
    tabela.add_column("Vreme")
    for i, transakcija in enumerate(transakcije):
        tabela.add_row(str(i),
                       str(transakcija.racun_id),
                       transakcija.vlasnik,
                       transakcija.tip,
                       str(transakcija.iznos),
                       transakcija.valuta.value,
                       str(transakcija.vreme)

                       )
    return tabela



