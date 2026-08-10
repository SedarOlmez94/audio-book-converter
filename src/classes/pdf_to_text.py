"""
Description: This module provides functionality to convert PDF files to text.
Author: Sedar Olmez
Date: 09/08/2026
"""

import pymupdf
from typing import List


class PDFToTextConverter:

    def __init__(self, pdf_path: str) -> None:
        """
        Initializes the PDFToTextConverter with the path to the PDF file.

        :param pdf_path: Path to the PDF file to be converted.
        """
        self.pdf_path = pdf_path
        self.saved_book = {}

    def convert_to_text(self) -> str:
        text = ""
        doc = pymupdf.open(self.pdf_path)
        for page in doc:
            text += page.get_text()
        return text

    def build_book_from_pdf(self) -> None:
        doc = pymupdf.open(self.pdf_path)
        i = 0
        for page in doc:
            self.saved_book[i] = page.get_text()
            i += 1

    def get_book(self, page: int) -> dict[int, str]:
        return {
            page: (
                self.saved_book[page] if page in self.saved_book else "Page not found."
            )
        }
        # return some page, within the dict saved_book if page exists in the saved_book object as a key, else return "Page not found."
