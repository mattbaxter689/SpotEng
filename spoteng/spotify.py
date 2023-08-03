from pandas import DataFrame
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import spotipy

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
        results = self.sp_conn.current_user_saved_tracks()
        saved = results['items']

        while results['next']:
            results = self.sp_conn.next(results)
            saved.extend(results['items'])

        saved_tracks = []
        for i in range(len(saved)):
            saved_tracks.append({
                'id': saved_tracks[i]['track']['id'],
                'name': saved_tracks[i]['track']['name']
            })

        songs_pd = DataFrame(saved_tracks)
        return songs_pd
