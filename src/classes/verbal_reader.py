"""
Module for converting text to speech.
Date 10/08/2026
"""

import pyttsx3


class VerbalReader:

    def __init__(self) -> None:
        self.engine = pyttsx3.init()

    def read_text(self, text: str) -> None:
        """
        Reads the provided text aloud.

        :param text: The text to be read aloud.
        """
        self.engine.say(text)
        self.engine.runAndWait()


    def get_current_rate(self) -> int:
        return self.engine.getProperty("rate")

    def set_rate(self, rate: int) -> None:
        self.engine.setProperty("rate", rate)

    def get_current_volume(self) -> float:
        return self.engine.getProperty("volume")

    def set_volume(self, volume: float) -> None:
        self.engine.setProperty("volume", volume)
