from utils.config import get_warehouse_creds
from dotenv import load_dotenv
<<<<<<< HEAD
from spotify import SpotifyHelper
=======
from spotify import SpotifyData
>>>>>>> parent of aae0c7c (starting docker containers, adding spotify data)
import os

load_dotenv()

<<<<<<< HEAD
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
    
=======
print(get_warehouse_creds())

def run():
    spot = SpotifyData(token=str(os.environ["SPOTIFY_CLIENT"]))
    print(spot.extract(days=10))
>>>>>>> parent of aae0c7c (starting docker containers, adding spotify data)

if __name__ == "__main__":
    run()

