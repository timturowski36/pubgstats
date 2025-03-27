"""
Dateiname: main.py
Beschreibung: 
Dieses Skript führt alle 2 Minuten eine Schleife aus, die PUBG-Statistiken durch Unterskripte abruft 
und diese in txt-Datein abspeichert

Autor: timturowski36
Datum: 2025-03-27
"""

# 🔧 Standardbibliotheken
import time
import os

# 📄 Hilfsfunktionen
from scripts.psn_win_parser import fetch_and_write_psn_wins
from scripts.steam_win_parser import fetch_and_write_steam_wins
from scripts.win_kd_parser_12h import write_12h_summary
from scripts.account_id_fetcher import fetch_and_save_account_id

# 🚀 Hauptfunktion
print("Starte PUBG-Stats-Monitor. Alle 2 Minuten wird aktualisiert.\nDrücke [Strg + C] zum Beenden.")
while True:
    fetch_and_save_account_id("brotrustgaming", "steam")
    fetch_and_save_account_id("brotrustgaming", "psn")
    fetch_and_write_psn_wins()
    fetch_and_write_steam_wins()
    write_12h_summary()

    print("Warte 2 Minuten...\n")
    time.sleep(120)