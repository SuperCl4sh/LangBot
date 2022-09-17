from asyncio import wait_for
from asyncore import poll
from utils import *



def query(audio_file):
    upload_response = upload_file(audio_file)
    transcript_response = request_transcript(audio_file)
    polling_endpoint = make_polling_endpoint(transcript_response)
    wait_for_completion()
    transcript = get_paragraphs(polling_endpoint)
"""def query():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print(res)"""
