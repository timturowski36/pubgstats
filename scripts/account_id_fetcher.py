import requests
from scripts.api_utils import load_api_key
import os

def fetch_and_save_account_id(player_name, platform):
    api_key = load_api_key()
    url = f"https://api.pubg.com/shards/{platform}/players?filter[playerNames]={player_name}"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/vnd.api+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            account_id = data['data'][0]['id']
            file_path = os.path.join("input", f"{platform}_accountid.txt")
            with open(file_path, "w") as f:
                f.write(account_id)
            print(f"[{platform.upper()}] Account-ID für '{player_name}' gespeichert: {account_id}")
            return account_id
        else:
            print(f"[{platform.upper()}] Keine Daten gefunden für '{player_name}'. Prüfe den Namen.")
    else:
        print(f"[{platform.upper()}] Fehler beim Abrufen der Account-ID: {response.status_code}, {response.text}")