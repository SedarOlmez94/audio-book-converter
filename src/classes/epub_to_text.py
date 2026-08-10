"""
Module for converting EPUB files to plain text.
Date 10/08/2026
"""

import io
from pathlib import Path

import ebooklib
from ebooklib import epub


class EPUBToTextConverter:

    def __init__(self, epub_path: str) -> None:
        self.epub_path = epub_path
