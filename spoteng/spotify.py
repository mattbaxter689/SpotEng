import requests
import json
from datetime import datetime, timedelta


class SpotifyData:
    def __init__(self, token: str):
        self.token = token

    def extract(self, days: int):
        today = datetime.now()
        time = today - timedelta(days=days)
        unix_time = int(time.timestamp()) * 1000

        headers = {
                "Accept": "application/json",
                "Content-type": "application/json",
                "Authorization": "Bearer {token}".format(token = self.token)
            }

        r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=unix_time),
                headers = headers)

        return r.json()

