"""
Module for converting text to speech.
Date 10/08/2026
Updated: 13/08/2026
"""

import os

# huggingface_hub 1.x uses the Xet backend by default (hf_xet). On macOS this can
# hang downloads at "Reconstructing (incomplete total...)" / 0.00B. Disable Xet so
# the standard HTTP downloader is used. Must be set before huggingface_hub is imported.
os.environ["HF_HUB_DISABLE_XET"] = "1"

import torchaudio as ta
import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS
from utils.config import authenticate_hf, get_hf_token


class VerbalReader:

    def __init__(self) -> None:
        authenticate_hf()
        
        self.model = ChatterboxTurboTTS.from_pretrained(device="cpu")

    def play_new_voice(self, voice_ref: str) -> any:
        wav = self.model.generate(self.text, audio_prompt_path=voice_ref)
        return wav

    def set_text_to_read(self, text: str) -> None:
        self.text = text
