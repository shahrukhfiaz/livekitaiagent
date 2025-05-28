import requests
import config

def synthesize_speech(text, model="aura-asteria-en", encoding="linear16", sample_rate=24000):
    url = "https://api.deepgram.com/v1/speak"
    headers = {
        "Authorization": f"Token {config.DEEPGRAM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model": model,
        "encoding": encoding,
        "sample_rate": sample_rate
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content  # Raw audio (WAV/PCM/MP3)
    else:
        raise Exception(f"Deepgram TTS Error: {response.text}")
