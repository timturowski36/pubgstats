# PUBG Stats Tracker

Ein kleines Python-Projekt zur Abfrage von Statistiken deines PUBG-Accounts

## 🚀 Features
- API-Abfragen auf die PUBG-API
- Daten abrufen, tranformieren & abspeichern
- Grundstruktur mit input/, output/, scripts/
(unten findet ihre wie ihr die Statistiken in euer OBS einbauen könnt)

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
