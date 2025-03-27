import requests
from datetime import datetime, timedelta, timezone
from scripts.api_utils import load_api_key, load_account_id

def get_last_12h_stats(account_id, api_key, platform="steam"):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Accept': 'application/vnd.api+json'
    }
    url = f"https://api.pubg.com/shards/{platform}/players/{account_id}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("[MATCHES] Fehler beim Abrufen der Spielerinfo")
        return None

    player_data = response.json()
    match_ids = player_data['data']['relationships']['matches']['data']

    stats_12h = {'wins': 0, 'matches': 0, 'kills': 0, 'deaths': 0}
    cutoff = datetime.now(timezone.utc) - timedelta(hours=12)

    for match_ref in match_ids[:30]:
        match_url = f"https://api.pubg.com/shards/{platform}/matches/{match_ref['id']}"
        match_resp = requests.get(match_url, headers=headers)
        if match_resp.status_code != 200:
            continue

        match_data = match_resp.json()
        match_time = datetime.strptime(match_data['data']['attributes']['createdAt'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        if match_time < cutoff:
            continue

        for item in match_data['included']:
            if item['type'] == 'participant' and item['attributes']['stats']['playerId'] == account_id:
                stats = item['attributes']['stats']
                stats_12h['matches'] += 1
                stats_12h['kills'] += stats.get('kills', 0)
                if stats.get('winPlace', 0) == 1:
                    stats_12h['wins'] += 1
                else:
                    stats_12h['deaths'] += 1
                break

    return stats_12h

def write_12h_summary():
    api_key = load_api_key()
    steam_id = load_account_id("steam_accountid.txt")
    stats = get_last_12h_stats(steam_id, api_key, "steam")
    if not stats:
        return

    kd = round(stats['kills'] / stats['deaths'], 2) if stats['deaths'] > 0 else stats['kills']
    wins_str = "-" if stats['wins'] == 0 else str(stats['wins'])

    line = f"{wins_str} / {kd}"
    output_file = "output/daily_win_check.txt"

    with open(output_file, 'w') as f:
        f.write(line + "\n")

    print(f"[STATS] Letzte 12h: {stats['matches']} Matches, {stats['wins']} Wins, {stats['kills']} Kills, {stats['deaths']} Deaths → K/D: {kd}")
