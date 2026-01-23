# Budgetkollen $$$

Ett CLI baserat verktyg för att hantera personlig ekonomi. 
Programmet låter användaren registrera utgifter, kategorisera dem och spara allt lokalt i en JSON-fil.
Projektet är byggt med fokus på modulär struktur och ren kod.

## 📦 Funktioner

* **Lägg till utgifter:** Spara belopp, beskrivning och kategori.
* **Visa lista:** Snygg tabellöversikt över alla sparade utgifter (använder biblioteket `rich`).
* **Beräkna total:** Summerar snabbt alla kostnader.
* **Persistent lagring:** All data sparas automatiskt i `data/expenses.json`.
* **Loggning:** Händelser och fel loggas till `data/app.log`.
* **Konfiguration:** Inställningar laddas från `data/settings.json`.

## 🛠 Installation

För att köra projektet lokalt, följ dessa steg:

1. **Klona repot:**
   ```bash
   git clone [https://github.com/DITT_ANVÄNDARNAMN/budget_tool.git](https://github.com/DITT_ANVÄNDARNAMN/budget_tool.git)
   cd budget_tool
   ```
2. **Skapa en virtuell miljö (.venv):**
   * Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * Mac/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
   ```
3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```
## Hur man kör programmet

Se till att du står i projektets rotmapp och att din virituella miljö är aktiverad.

**Starta verktyget:**
```bash
python -m src.main
```

För Windows-användare (Git Bash)
Om du använder Git Bash och inte kan skriva in text, använd detta kommando istället:
```bash
PYTHONIOENCODING=utf-8 winpty python -m src.main
```



## 📂 Projektstruktur

```text
stocksimulator/
│
├── data/                 # Stores portfolio files (JSON) and logs
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point (CLI Menu)
│   ├── market.py         # Fetches market data from Yahoo Finance (API)
│   ├── portfolio.py      # Core logic for cash, holdings, and trades
│   ├── storage.py        # Handles data persistence (Save/Load JSON)
│   ├── analysis.py       # Analytics using Pandas (Calculates Profit/Loss)
│   └── utils.py          # Utility functions (Input validation, etc.)
├── tests/
│   ├── test_portfolio.py
│   ├── test_market.py
│   └── ...
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── .github/workflows/python-app.yml  # CI/CD configuration
```

## 📝 Författare
Skapat av Anton Hergefeldt som en del av inlämningsuppgift i Python-kursen.
