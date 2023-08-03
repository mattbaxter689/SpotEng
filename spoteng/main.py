from utils.config import get_warehouse_creds
from utils.db import WarehouseConnection
from dotenv import load_dotenv
from spotify import SpotifyHelper, SpotifyConnection
import os

load_dotenv()

def run():
    spot = SpotifyConnection(client_id=os.environ["SPOTIFY_CLIENT"],
                                  client_secret=os.environ["SPOTIFY_CLIENT_SECRET"])

    scope = "user-library-read user-follow-read user-top-read playlist-read-private"
    sp_conn = spot.connect(scope = scope)
    help = SpotifyHelper(sp_conn=sp_conn)
    songs = help.get_saved_id()

    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        songs_list = list(songs)
        curr.execute("""
                     INSERT INTO songs.names (
                            VALUES(%s, %s)
                        )
                     """, songs_list)
    

if __name__ == "__main__":
    run()

