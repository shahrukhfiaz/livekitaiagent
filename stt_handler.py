from deepgram import Deepgram
import config
import asyncio
import aiohttp

dg_client = Deepgram(config.DEEPGRAM_API_KEY)

async def stream_transcribe(audio_url):
    '''
    Streams audio from a URL to Deepgram STT and yields transcript(s).
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(audio_url) as audio_stream:
            response = await dg_client.transcription.prerecorded({
                'buffer': await audio_stream.read(),
                'mimetype': 'audio/wav'
            }, {
                'punctuate': True,
                'language': 'en'
            })
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            yield transcript
