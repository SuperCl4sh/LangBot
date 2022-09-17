# https://github.com/AssemblyAI-Examples/assemblyai-and-python-in-5-minutes/blob/main/transcribe.py

import argparse
import os
import utils


def main(audio_file):
    # Create header with authorization along with content-type
    header = {
        'authorization': os.getenv("AAI_API_KEY"),
        'content-type': 'application/json'
    }
    
    upload_url = utils.upload_file(audio_file, header)

    # Request a transcription
    transcript_response = utils.request_transcript(upload_url, header)

    # Create a polling endpoint that will let us check when the transcription is complete
    polling_endpoint = utils.make_polling_endpoint(transcript_response)

    # Wait until the transcription is complete
    utils.wait_for_completion(polling_endpoint, header)

    # Request the paragraphs of the transcript
    paragraphs = utils.get_paragraphs(polling_endpoint, header)

    return [para['text'] for para in paragraphs]