from utils.config import get_warehouse_creds
from dotenv import load_dotenv
from spotify import SpotifyData
import os

load_dotenv()

print(get_warehouse_creds())

def run():
    spot = SpotifyData(token=str(os.environ["SPOTIFY_CLIENT"]))
    print(spot.extract(days=10))

if __name__ == "__main__":
    run()

