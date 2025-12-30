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
budget_tool/
├── data/               # Lagrar JSON-data och loggar
├── src/
│   ├── utils/          # Hjälpfunktioner (Logger, Config)
│   ├── file_handler.py # Hanterar läsning/skrivning av filer
│   ├── finance.py      # Logik och beräkningar
│   ├── ui.py           # Användargränssnitt (Input/Output)
│   └── main.py         # Huvudprogrammet
├── pyproject.toml      # Projektkonfiguration
└── requirements.txt    # Externa bibliotek
```

## 📝 Författare
Skapat av Anton Hergefeldt som en del av inlämningsuppgift i Python-kursen.
