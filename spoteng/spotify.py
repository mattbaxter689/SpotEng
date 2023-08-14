# from pandas import DataFrame
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


class SpotifyConnection:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def connect(self, scope: str) -> Spotify:
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri="http://www.google.com",
                scope=scope,
                open_browser=False,
            )
        )


class SpotifyHelper:
    def __init__(self, sp_conn):
        self.sp_conn = sp_conn

    def extend_result(self, results):
        saved = results["items"]
        while results["next"]:
            results = self.sp_conn.next(results)
            saved.extend(results["items"])

        return saved

    def get_saved_id(self) -> list[dict]:
        results = self.sp_conn.current_user_saved_tracks()
        saved = self.extend_result(results)

        saved_tracks = [{"id": song["track"]["id"]} for song in saved]
        return saved_tracks

    def get_top_track_id(self) -> None:
        pass

    def get_track_features(self) -> None:
        pass
