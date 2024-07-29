import requests
import os
from dotenv import load_dotenv

from elevenlabs import play
from elevenlabs.client import ElevenLabs


load_dotenv()
elevenlabsAPI =  os.getenv('ELEVENLABS')

# voice_id set to Rachel:  EXAVITQu4vr4xnSDxMaL


def texttoaudio(llm_response_text, output_filename = 'output.mp3'):

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": elevenlabsAPI
    }

    data = {
        "text": llm_response_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open(output_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)