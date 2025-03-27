"""
Dateiname: main.py
Beschreibung: 
Dieses Skript ruft alle 2 Minuten automatisiert PUBG-Statistiken ab und speichert die Ergebnisse in entsprechenden Textdateien. Dafür werden mehrere Unterskripte verwendet, um die Übersichtlichkeit und Wartbarkeit zu gewährleisten.

Vor der ersten Nutzung müsst ihr einmalig die Zeilen 24 und 25  aktivieren (Kommentare entfernen), um eure PUBG-Account-IDs automatisch abzurufen und dauerhaft zu speichern. Danach könnt ihr diese Zeilen wieder auskommentieren.

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
    # fetch_and_save_account_id("brotrustgaming", "steam")
    # fetch_and_save_account_id("brotrustgaming", "psn")
    fetch_and_write_psn_wins()
    fetch_and_write_steam_wins()
    write_12h_summary()

    print("Warte 2 Minuten...\n")
    time.sleep(120)