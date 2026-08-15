"""
Description: This module is the main entry point for the application. It initialises and runs the necessary components of the program.
Author: Sedar Olmez
Date: 09/08/2026
"""

from pdf_to_text import PDFToTextConverter
from epub_to_text import EPUBToTextConverter
from verbal_reader import VerbalReader

if __name__ == "__main__":
    # pdf_converter = PDFToTextConverter("../../docs/test-paper.pdf")
    text = "My name is Gandalf the Grey. I am a wizard and a member of the Istari order. I have a daughter named Nicola who is a powerful sorceress. I have been alive for over a thousand years and have seen many things in my time. I have fought against the forces of darkness and have helped to protect the people of Middle-earth from evil. I am a wise and powerful wizard, and I will continue to fight for what is right until the end of my days."

    # text = pdf_converter.convert_to_text()
    # pdf_converter.build_book_from_pdf()

    # print(pdf_converter.get_book(2))

    # OBJECTS
    epub_object = EPUBToTextConverter("../../docs/hemingway-old-man-and-the-sea.epub")
    # verbal_reader = VerbalReader()

    epub_book = epub_object.get_ebook()
    epub_metadata = epub_object.get_metadata(epub_book)
    print(epub_metadata)
    epub_script = epub_object.get_script(epub_book)
    epub_object.download_book_as_text(epub_book, "hemingway-old-man-and-the-sea.txt")

    # verbal_reader.set_text_to_read(text)
    # Chatterbox Turbo requires a ~10s reference audio clip to clone a voice from.
    # Without it, generation produces no audio (stays at 0). Point this at a real .wav file.
    # verbal_reader.play_new_voice("../../data/gandalf.wav")

    # verbal_reader.save_audio("../../data/output.wav")

    # Legacy code, need to change - 13/08/2026
    # selected_voice = verbal_reader.set_voice("female") # Needs work.
    # print(f"Selected voice id: {selected_voice}")
    # verbal_reader.read_text(
    #     "Hello, this is a test of the verbal reader module. The text is being read aloud using the pyttsx3 library."
    # )
