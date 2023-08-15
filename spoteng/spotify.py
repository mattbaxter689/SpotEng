# from pandas import DataFrame
import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


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

    def get_top_track_id(self) -> list[dict]:
        short_results = self.sp_conn.current_user_top_tracks(time_range="short_term")
        short_saved = self.extend_result(short_results)
        short_list = [{"id": song["id"]} for song in short_saved]


        med_results = self.sp_conn.current_user_top_tracks(time_range="medium_term")
        med_saved = self.extend_result(med_results)
        med_list = [{"id": song["id"]} for song in med_saved]

        long_results = self.sp_conn.current_user_top_tracks(time_range="long_term")
        long_saved = self.extend_result(long_results)
        long_list = [{"id": song["id"]} for song in long_saved]

        return short_list + med_list + long_list

    def get_track_features(self, track_ids: list[dict]) -> None:
        print(pd.DataFrame.head(pd.DataFrame(track_ids)))
