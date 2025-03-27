# PUBG Stats Tracker

Ein kleines Python-Projekt zur Abfrage von Statistiken deines PUBG-Accounts

## 🚀 Features
- Abfragen auf die PUBG-API
- Daten abrufen, tranformieren & abspeichern

(unten findet Ihr außerdem wie ihr die Statistiken in eure Streams mit OBS einbauen könnt)

## 📁 Projektstruktur
```text
pubgstats/ 
├── main.py
├── input/
├── output/
└── scripts/
```

## ⚙️ Installation
Vorraussetzungen: 
git,pip und python ist installiert

```bash
git clone https://github.com/timturowski36/pubgstats.git
pip install requests
```
(es werden außerdem die Pakete json, os, time und datetime verwendet, diese sind aber Teil der Standardbibilothek von Python)

Ihr könnt den Projektordner natürlich auch so herunterladen, dann bekommt ihr jedoch keine Updates & Bugfixes.

## 🔑 Abrufen deines API-Tokens
Hier findet ihr die Doku der PUBG-API: https://documentation.pubg.com/en/introduction.html

1. Ihr müsst euch als Developer im PUBG-Portal anmelden: https://developer.pubg.com/#open-login-modal
2. Dann müsst ihr eine App erstellen, meine heißt bspw. "Discord Bot", da meine App ursprünglich ein Discord Bot werden sollte
3. Dann bekommt ihr einen API-Token der euch 10 RPM (requests per minute) erlaubt

## 🐍 Einrichtung von Python
1. Repository wie bei "⚙️ Installation" beschrieben runterladen
2. Im Verzeichnis "Input", müsst ihr eine txt-Datei anlegen die api_key.txt heißt: input\api_key.txt
3. In diese Datei kopiert ihr den API-Code aus dem Developer-Portal (Achtet dabei bitte darauf, dass nur der Key abgespeichert wird und keine Leerzeichen oder sonst was in dem File mitgespeichert werden)
4. main.py in einem Code-Editor eurer Wahl aufrufen (bspw. VSCode)

```python
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
```

Folgende Zeilen müssen einmalig mit euren Accountnamen gefüllt werden und auskommentiert werden:
```python
print("Starte PUBG-Stats-Monitor. Alle 2 Minuten wird aktualisiert.\nDrücke [Strg + C] zum Beenden.")
while True:
    fetch_and_save_account_id("brotrustgaming", "steam")
    fetch_and_save_account_id("brotrustgaming", "psn")
    #fetch_and_write_psn_wins()
    #fetch_and_write_steam_wins()
    #write_12h_summary()

    print("Warte 2 Minuten...\n")
    time.sleep(120)
```
4. Code ausführen und mit Ctr+C beenden (dann müssten eure Accountinformationen in den entsprechenden Files liegen (siehe input-Ordner)
5. main.py wieder auf Ursprungszustand (s.O.) zurücksetzen und und erneut ausführen

Jetzt werden alle 2 min eure Statistiken in die txt-Datein geschrieben.

## 🎥 Einrichtung von OBS
1. OBS öffnen
2. Neue Quelle hinzufügen mit "+" → Text (GDI+) → Haken setzen bei "Aus Datei auslesen" → Datei angeben (../steam_stats.txt) → "Okay" → der Quelle einen eindeutigen Namen geben, wie "PUBG Wins Stream" bspw.
3. Zahl an entsprechende Stelle im Stream verschieben

Die Panels habe ich mit https://streamlabs.com/ erstellt. Auf der Seite könnt ihr euch kostenlos mit eurem Twitch-Account anmelden und Pannels erstellen, runterladen und 
1. Streamlabs öffnen
2. Dashboard → Panel Maker → Panels erstellen
3. Panels runterladen
4. OBS öffnen
5. Neue Quelle hinzufügen mit "+" → Bild → Datei angeben (../PUBG-WINS STEAM.png) → "Okay" → der Quelle einen eindeutigen Namen geben, wie "PUBG Wins Stream Panel" bspw.
6. Bild an entsprechende Stelle im Stream verschieben
7. Ich hab bei mir noch die Deckkraft runtergeschraubt mit: Rechtsklick auf das Bild → Filter → Neuen Filter hinzufügen mit "+" → Farbkorrektur → Namen vergeben → Deckkraft festlegen → "Okay"
