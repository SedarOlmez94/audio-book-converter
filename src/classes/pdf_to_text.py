'''
Description: This module provides functionality to convert PDF files to text.
Author: Sedar Olmez
Date: 09/08/2026
'''

import pymupdf



class PDFToTextConverter:



    def __init__(self, pdf_path: str) -> None:
        """
        Initializes the PDFToTextConverter with the path to the PDF file.

        :param pdf_path: Path to the PDF file to be converted.
        """
        self.pdf_path = pdf_path



    def convert_to_text(self) -> str:
        text = ""
        doc = pymupdf.open(self.pdf_path)
        for page in doc:
            text += page.get_text()
        return text