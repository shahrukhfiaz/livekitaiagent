from fastapi import FastAPI, Request
from stt_handler import stream_transcribe
from llm_handler import get_llm_response
from tts_handler import synthesize_speech
import tempfile
import asyncio

app = FastAPI()

@app.post("/sip/inbound")
async def inbound_sip(request: Request):
    data = await request.json()
    audio_stream_url = data.get("audio_stream_url")
    if not audio_stream_url:
        return {"error": "Missing audio_stream_url in request."}
    # Transcribe the audio stream
    transcript = None
    async for t in stream_transcribe(audio_stream_url):
        transcript = t
        break
    if not transcript:
        return {"error": "No transcript."}
    response_text = get_llm_response(transcript)
    response_audio = synthesize_speech(response_text)
    # For demo: Save response audio to temp file (in real case, stream back to caller)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        temp_wav.write(response_audio)
        temp_wav_path = temp_wav.name
    return {
        "transcript": transcript,
        "response_text": response_text,
        "audio_file": temp_wav_path  # For demo only
    }

@app.post("/test_tts")
async def test_tts(request: Request):
    data = await request.json()
    text = data.get("text", "Hello, this is a test of Deepgram TTS.")
    audio = synthesize_speech(text)
    return {
        "text": text,
        "audio_bytes": audio.hex()
    }
