import json
import os
DATA_FILE = "data/expenses.json"

def load_data():
    # tar fram data från json filen
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # returnerar en tom lista om filen inte finns
    if not os.path.exists(DATA_FILE):
        return [] 
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] # om filen är korrupt så försöker den igen
    
def save_data(expenses):
    # sparar listan med uppgifter till json
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent = 4)

