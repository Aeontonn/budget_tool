from rich.console import Console
from rich.table import Table

console = Console()

def get_valid_number(prompt):
    # loopar tills användaren skriver en giltig siffra
    while True:
        value = console.input(f"[bold blue]{prompt}[/bold blue]")
        try:
            return float(value)
        except ValueError:
            console.print(f"[red]Felaktigt format! Måste skriva en siffra (t.ex. 100 eller 150.5).[/red]")
            
def display_expenses(expenses):
    # visar en tabell över utgifter
    if not expenses:
        console.print("[yellow]Inga utgifter registrerade ännu.[/yellow]")
        return
    
    table = Table(title="Mina Utgifter")
    table.add_column("Beskrivning", style="cyan")
    table.add_column("Kategori", style="magenta")
    table.add_column("Belopp", style="green", justify="right")
    
    for item in expenses:
        table.add_row(item['description'], item['category'], f"{item['amount']} kr")
        
    console.print(table)
