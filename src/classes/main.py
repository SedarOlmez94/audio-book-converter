"""
Description: This module is the main entry point for the application. It initialises and runs the necessary components of the program.
Author: Sedar Olmez
Date: 09/08/2026
"""

from epub_to_text import EPUBToTextConverter
from verbal_reader import VerbalReader
from page_extractor import PageExtractor


def epub_to_text(epub_path: str, output_path: str) -> None:
    """
    Converts an EPUB file to plain text and saves it to the specified output path.

    :param epub_path: The path to the EPUB file.
    :param output_path: The path where the converted text will be saved.
    """
    epub_converter = EPUBToTextConverter(epub_path)
    epub_book = epub_converter.get_ebook()
    epub_converter.download_book_as_text(epub_book, output_path)

def verbal_read_text(text: str) -> None:
    """
    Reads the provided text aloud using the VerbalReader.

    :param text: The text to be read aloud.
    """
    verbal_reader = VerbalReader()
    verbal_reader.set_text_to_read(text)
    verbal_reader.play_new_voice("../../data/gandalf.wav")
    verbal_reader.save_audio("../../data/output.wav")

def extract_pages_from_book(book_location_in_text: str, target_size: int = 3000) -> None:
    """
    Extracts pages from a text document and prints them.

    :param book_location_in_text: The path to the text file containing the book.
    :param target_size: Target character count per page (default 3000 chars ≈ 8-10 min audio).
    """
    page_extractor = PageExtractor(book_location_in_text, target_size=target_size)
    pages = page_extractor.create_bite_sized_pages()
    
    for page in pages:
        print(f"Page {page['page_num']} (Chapter: {page['chapter']}, Char Count: {page['char_count']}):")
        print(page['content'])
        print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    # pdf_converter = PDFToTextConverter("../../docs/test-paper.pdf")
    text = "My name is Gandalf the Grey. I am a wizard and a member of the Istari order. I have a daughter named Nicola who is a powerful sorceress. I have been alive for over a thousand years and have seen many things in my time. I have fought against the forces of darkness and have helped to protect the people of Middle-earth from evil. I am a wise and powerful wizard, and I will continue to fight for what is right until the end of my days."

    # text = pdf_converter.convert_to_text()
    # pdf_converter.build_book_from_pdf()

    # print(pdf_converter.get_book(2))

    # epub_to_text("../../docs/shelley-frankenstein.epub", "shelley-frankenstein.txt")
    # WE have to get each page of the book and read it aloud - TODO
    # verbal_read_text(text)

    extract_pages_from_book("../../docs/shelley-frankenstein.txt", target_size=3000)
