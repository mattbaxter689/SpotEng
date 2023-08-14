import os

import psycopg2.extras as p
from dotenv import load_dotenv
from spotify import SpotifyConnection, SpotifyHelper
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
    help = SpotifyHelper(sp_conn=sp_conn)
    songs = help.get_saved_id()

    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(
            curr,
            """
             INSERT INTO songs.names (
                    VALUES(
                        %(id)s, 
                        %(name)s
                    )
                )
            """,
            songs,
        )

if __name__ == "__main__":
    run()
