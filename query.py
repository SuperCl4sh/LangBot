from asyncio import wait_for
from asyncore import poll
from utils import *
from transcribe import main as M
import psycopg2
import os

def query(audio_file):
    res = M(audio_file)
    return res

def get_points(user):
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    statements = [
        # 'CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, points INT)',
        'SELECT * FROM accounts WHERE id = {}'.format(user)
    ]
    with conn.cursor() as cur:
        for statement in statements:
            cur.execute(statement)
            if len(res): res = cur.fetchall()[0]
        if not len(res):
            cur.execute("INSERT INTO accounts (id, points) VALUES ({},{})".format(user, 0))
            res = tuple(user, 0)
    user, res = res
    conn.commit()
    return res

def update_points(user, increment):
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    
    points = get_points(user) + increment
    statements = [
        'CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, points INT);',
        'UPDATE accounts SET points = {} WHERE id = {}'.format(points, user)
    ]
    with conn.cursor() as cur:
        for statement in statements:
            cur.execute(statement)
    conn.commit()
    return
