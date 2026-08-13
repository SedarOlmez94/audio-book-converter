"""
Module for converting text to speech.
Date 10/08/2026
Updated: 13/08/2026
"""


import os

import torchaudio as ta
import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS
from dotenv import load_dotenv
load_dotenv()

# The Hugging Face Hub reads the token from HF_TOKEN, not the name used in .env,
# so forward it explicitly. Without this the download can hang at 0.00B.
hf_token = os.getenv("HUGGING_FACE_ACCESS_TOKEN")
if hf_token:
    os.environ["HF_TOKEN"] = hf_token
# hf_transfer often stalls downloads at "Fetching ... 0%" / 0.00B; disable it
# so the standard, reliable downloader is used.
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

class VerbalReader:

    def __init__(self) -> None:
        self.model = ChatterboxTurboTTS.from_pretrained(device="cpu")

    def play_new_voice(self, voice_ref: str) -> any:
        wav = self.model.generate(self.text, audio_prompt_path=voice_ref)
        return wav

    def set_text_to_read(self, text: str) -> None:
        self.text = text



    
                      
