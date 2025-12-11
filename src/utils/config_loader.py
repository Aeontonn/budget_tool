import json
import os

SETTINGS_PATH = "data/settings.json"

def load_config():
    if not os.path.exists(SETTINGS_PATH):
        raise FileNotFoundError(f"Kunde inte hitta config filen: {SETTINGS_PATH}")
    
    with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
