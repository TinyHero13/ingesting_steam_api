import requests

def extract_data():
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json'

    response = requests.get(url).json()['applist']['apps']
    return response