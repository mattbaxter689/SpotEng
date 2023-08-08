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
    for song in songs:
        with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
            #might replace this list here to just loop through records in songs
            #and write to database. Not efficient but itll work hopefully
            curr.execute("""
                         INSERT INTO songs.names (
                                VALUES(
                                    %(id)s, 
                                    %(name)s
                                )
                            )
                         """, song)
    

if __name__ == "__main__":
    run()

