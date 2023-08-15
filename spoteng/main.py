import os

import psycopg2.extras as p
from dotenv import load_dotenv
from spotify.spotify import SpotifyConnection, SpotifyFeatures
from utils.config import get_warehouse_creds
from utils.db import WarehouseConnection

load_dotenv()


def run():
    spot = SpotifyConnection(
        client_id=os.environ["SPOTIFY_CLIENT"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    )

    scope = "user-library-read user-follow-read user-top-read playlist-read-private"
    sp_conn = spot.connect(scope=scope)
    help = SpotifyFeatures(sp_conn=sp_conn)
    saved_songs = help.get_saved_id()
    top_songs = help.get_top_track_id()
    songs = saved_songs + top_songs
    help.get_track_features(songs)

    # with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
    #     p.execute_batch(
    #         curr,
    #         """
    #          INSERT INTO songs.names (
    #                 VALUES(
    #                     %(id)s,
    #                     %(name)s
    #                 )
    #             )
    #         """,
    #         songs,
    #     )


if __name__ == "__main__":
    run()
