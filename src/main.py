import sys
from src import file_handler, finance, ui
from rich.console import Console

console = Console()

def main():
    expenses = file_handler.load_data()
    
    while True:
        console.print("\n[bold]--- BUDGETKOLLEN ---[/bold]")
        console.print("1. Lägg till utgift")
        console.print("2. Visa alla utgifter")
        console.print("3. Visa total kostnad")
        console.print("4. Avsluta")
        
        choice = console.input("\nVälj (1-4)")
        
        if choice == "1":
            desc = console.input("Vad har du köpt? ")
            cat = console.input("Kategori (Mat/Nöje/Hyra/Prenumerationer)? ")
            amount = console.input("Pris? ")
            
            expenses = finance.add_expenses(expenses, desc, amount, cat)
            file_handler.save_data(expenses)
            console.print("[green]Utgift sparad![/green]")
            
        elif choice == "2":
            ui.display_expenses(expenses)
            
        elif choice == "3":
            total = finance.calculate_total(expenses)
            console.print(f"\n[bold green]Totala utgifter: {total} kr[/bold green]")
    
        elif choice == "4":
            console.print("Hejdå!")
            break
        else:
            console.print("[red]Ogiltigt val, försök igen![/red]")
            
if __name__ == "__main__":
    main()
