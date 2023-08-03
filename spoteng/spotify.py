import requests
from pandas import DataFrame
import numpy as np

# class SpotifyConnection:
#     def __init__(self, client_id: str, client_secret: str):
#         self.client_id = client_id
#         self.client_secret = client_secret
#
#     def connect(self, scope: str) -> Spotify:
#         return spotipy.Spotify(auth_manager=SpotifyOAuth(
#             client_id=self.client_id,
#             client_secret=self.client_secret,
#             redirect_uri="http://www.google.com",
#             scope=scope
#         ))

class SpotifyHelper:
    def __init__(self, client_secret: str, client_id: str):
        self.client_secret = client_secret
        self.client_id = client_id
        self.access_token = self.get_token()

    def authorize(self):
        

    def get_token(self):
        response = requests.post(url='https://accounts.spotify.com/api/token',
                                 data={ 'grant_type': 'authorization_code' },
                                 auth=(self.client_id, self.client_secret))
        self.spotify_token = response.json()['access_token']

    def get_saved_id(self) -> DataFrame:
        songs=[]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {token}".format(token = self.spotify_token)
        }       
        url = "https://api.spotify.com/v1/me/tracks"
        while True:
            response = requests.get(url=url, headers=headers)
            results = response.json()
            print(results)

            for song in results["items"]:
                songs.append({
                    'id': song["track"]["id"],
                    'name': song["track"]["name"]
                })

            if results["next"] is not None:
                url = results["next"]
            else:
                break

        songs_pd = DataFrame(songs)
        return songs_pd
