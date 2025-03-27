import requests
import os
from scripts.api_utils import load_api_key, load_account_id

def fetch_total_wins(platform, account_id, api_key):
    url = f'https://api.pubg.com/shards/{platform}/players/{account_id}/seasons/lifetime'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/vnd.api+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        game_mode_stats = data['data']['attributes']['gameModeStats']
        return sum(mode.get('wins', 0) for mode in game_mode_stats.values())
    else:
        print(f"[{platform.upper()}] Fehler {response.status_code}: {response.text}")
        return None

def fetch_and_write_steam_wins():
    api_key = load_api_key()
    steam_id = load_account_id("steam_accountid.txt")
    wins = fetch_total_wins("steam", steam_id, api_key)
    if wins is not None:
        output_file = "output/steam_stats.txt"
        with open(output_file, 'w') as f:
            f.write(f"{wins}")
        print(f"[STEAM] Aktuelle Wins: {wins}")
