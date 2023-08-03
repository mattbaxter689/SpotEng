from utils.config import get_warehouse_creds
from dotenv import load_dotenv
from spotify import SpotifyHelper
import os
import psycopg2

from utils.db import WarehouseConnection

load_dotenv()

def run():
    spot_conn = SpotifyHelper(client_id=os.environ["SPOTIFY_CLIENT"],
                                  client_secret=os.environ["SPOTIFY_CLIENT_SECRET"])
    print(spot_conn.get_saved_id())

    # with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
    #     songs_list = list(songs)
    #     curr.execute("""
    #                  INSERT INTO songs.names (
    #                         VALUES(%s, %s)
    #                     )
    #                  """, songs_list)
    

if __name__ == "__main__":
    run()

