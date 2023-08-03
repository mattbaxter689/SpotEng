import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.client import Spotify
from pandas import DataFrame
import numpy as np

class SpotifyConnection:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def connect(self, scope: str) -> Spotify:
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri="http://www.google.com",
            scope=scope
        ))

class SpotifyHelper:
    def __init__(self, sp_conn):
        self.sp_conn = sp_conn

    def get_saved_id(self) -> DataFrame:
        res = self.sp_conn.current_user_saved_tracks()
        saved = res['items']
        while res['next']:
            res = self.sp_conn.next(res)
            saved.extend(res['items'])
        
        saved_id = list()
        saved_name = list()

        for i in range(len(saved)):
            saved_id.append(saved[i]['track']['id'])
            saved_name.append(saved[i]['track']['name'])

        saved_id_pd = DataFrame(np.column_stack([saved_id, saved_name]), columns=["id","song_name"])

        return saved_id_pd
