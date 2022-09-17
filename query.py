from asyncio import wait_for
from asyncore import poll
from utils import *
from transcribe import main as M
import psycopg2
import os

HEADER = ''

def query(audio_file):
    # TODO: Cache results to minimize API queries
    return M('Videos/1.mp3')

def db_query():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print(res)
