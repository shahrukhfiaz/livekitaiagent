import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LIVEKIT_URL = os.getenv('LIVEKIT_URL')
LIVEKIT_API_KEY = os.getenv('LIVEKIT_API_KEY')
LIVEKIT_API_SECRET = os.getenv('LIVEKIT_API_SECRET')
TWILIO_SIP_DOMAIN = os.getenv('TWILIO_SIP_DOMAIN')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
