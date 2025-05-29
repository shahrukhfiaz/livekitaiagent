import requests
import config

def synthesize_speech(
    text,
    model="aura-asteria-en",      # Default Deepgram voice model (check Deepgram docs for latest)
    encoding="linear16",          # "linear16" for PCM/WAV, "mp3" for compressed
    sample_rate=24000             # You can adjust as needed
):
    """
    Synthesize speech from text using Deepgram TTS.
    Returns: Raw audio bytes.
    """
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
        return response.content  # Audio data (WAV or MP3)
    else:
        raise Exception(f"Deepgram TTS Error: {response.status_code} {response.text}")
