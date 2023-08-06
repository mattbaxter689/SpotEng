from pandas import DataFrame
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify

class SpotifyConnection:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def connect(self, scope) -> Spotify:
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri="http://www.google.com",
            scope = scope,
            open_browser=False
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

        saved_tracks = list()
        for i in range(len(saved)):
            saved_tracks.append({
                'id': saved[i]['track']['id'],
                'name': saved[i]['track']['name']
            })

        songs_pd = DataFrame(saved_tracks)
        return songs_pd
