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


    def get_ebook(self) -> epub.EpubBook:
        """
        Loads the EPUB file and returns an EpubBook object.

        :return: An EpubBook object representing the loaded EPUB file.
        """
        book = epub.read_epub(self.epub_path)
        return book

    def get_metadata(self, book: epub.EpubBook) -> dict:
        """
        Extracts metadata from the EpubBook object.

        :param book: An EpubBook object.
        :return: A dictionary containing the metadata of the EPUB file.
        """
        metadata = {
            "title": book.get_metadata("DC", "title")[0][0] if book.get_metadata("DC", "title") else "Unknown",
            "author": book.get_metadata("DC", "creator")[0][0] if book.get_metadata("DC", "creator") else "Unknown",
            "language": book.get_metadata("DC", "language")[0][0] if book.get_metadata("DC", "language") else "Unknown",
            "publisher": book.get_metadata("DC", "publisher")[0][0] if book.get_metadata("DC", "publisher") else "Unknown",
            "description": book.get_metadata("DC", "description")[0][0] if book.get_metadata("DC", "description") else "No description available.",
        }
        return metadata
    
