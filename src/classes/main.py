"""
Description: This module is the main entry point for the application. It initialises and runs the necessary components of the program.
Author: Sedar Olmez
Date: 09/08/2026
"""

from pdf_to_text import PDFToTextConverter

if __name__ == "__main__":
    pdf_converter = PDFToTextConverter("../../docs/test-paper.pdf")
    # text = pdf_converter.convert_to_text()
    pdf_converter.build_book_from_pdf()

    print(pdf_converter.get_book(2))
