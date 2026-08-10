"""
Description: This module is the main entry point for the application. It initialises and runs the necessary components of the program.
Author: Sedar Olmez
Date: 09/08/2026
"""

from pdf_to_text import PDFToTextConverter
from epub_to_text import EPUBToTextConverter
from verbal_reader import VerbalReader

if __name__ == "__main__":
    pdf_converter = PDFToTextConverter("../../docs/test-paper.pdf")
    # text = pdf_converter.convert_to_text()
    # pdf_converter.build_book_from_pdf()

    # print(pdf_converter.get_book(2))

    # OBJECTS
    epub_object = EPUBToTextConverter("../../docs/shelley-frankenstein.epub")
    verbal_reader = VerbalReader()

    epub_book = epub_object.get_ebook()
    epub_metadata = epub_object.get_metadata(epub_book)
    print(epub_metadata)
    epub_script = epub_object.get_script(epub_book)
    # print(epub_script)
    verbal_reader.read_text(
        "Hello, this is a test of the verbal reader module. The text is being read aloud using the pyttsx3 library."
    )
