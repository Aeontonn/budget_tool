from rich.console import Console
from src import file_handler, finance, ui
from src.utils import config_loader
from src.core.logger import BudgetLogger

console = Console()

def main():
    try:
        #   ladda config och initiera logger
        config = config_loader.load_config()
        logger = BudgetLogger(config["log_path"])
        logger.log_event("Applikationen startades.")
        
        #   ladda data
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
                amount = ui.get_valid_number("Pris? ")

                expenses = finance.add_expenses(expenses, desc, amount, cat)
                file_handler.save_data(expenses)
                
                console.print("[green]Utgift sparad![/green]")
                logger.log_event(f"Ny utgift: {desc}, {amount}kr")

            elif choice == "2":
                ui.display_expenses(expenses)

            elif choice == "3":
                total = finance.calculate_total(expenses)
                console.print(f"\n[bold green]Totala utgifter: {total} kr[/bold green]")
                logger.log_event(f"Visade total: {total}kr")

            elif choice == "4":
                console.print("Hejdå!")
                logger.log_event("Applikationen avslutades.")
                break
            else:
                console.print("[red]Ogiltigt val, försök igen![/red]")
                logger.log_error(f"Ogiltigt val: {choice}")
                
    except Exception as e:
        console.print(f"[bold red]Kritiskt fel: {e}[/bold red]")
        if "logger" in locals():
            logger.log_error(f"Krasch: {e}")
            
if __name__ == "__main__":
    main()
