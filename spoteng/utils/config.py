import os
from dotenv import load_dotenv

from utils.db import DBConnection

load_dotenv()

def get_warehouse_creds() -> DBConnection:
    return DBConnection(
            user=os.environ["WAREHOUSE_USER"],
            password=os.environ["WAREHOUSE_PASSWORD"],
            db=os.environ["WAREHOUSE_DB"],
            host=os.environ["WAREHOUSE_HOST"],
            port=int(os.environ["WAREHOUSE_PORT"]),
        )
