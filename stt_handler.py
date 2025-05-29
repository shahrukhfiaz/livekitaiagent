import aiohttp
import config
from deepgram import DeepgramClient, PrerecordedOptions, FileSource

# Initialize the Deepgram client using your API key from config.py
dg_client = DeepgramClient(config.DEEPGRAM_API_KEY)

async def stream_transcribe(audio_url):
    """
    Downloads audio from a URL, sends it to Deepgram for transcription,
    and yields the transcript (async generator).
    """
    # Download the audio file as bytes
    async with aiohttp.ClientSession() as session:
        async with session.get(audio_url) as resp:
            audio_bytes = await resp.read()
    
    # Prepare file source for Deepgram
    source = FileSource(buffer=audio_bytes)
    
    # Set transcription options
    options = PrerecordedOptions(
        model='nova-2',         # Use 'nova-2' or another supported model
        language='en-US',       # Change as needed
        punctuate=True
    )
    
    # Send to Deepgram for transcription
    response = await dg_client.listen.prerecorded(source, options)
    
    # Extract and yield transcript
    transcript = response.results.channels[0].alternatives[0].transcript
    yield transcript
