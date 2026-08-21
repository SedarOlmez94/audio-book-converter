"""
Description: This module provides functionality to extract pages from a text document, from the first page to N.
Author: Sedar Olmez
Date: 21/08/2026
"""

import re
from typing import List, Tuple, Dict


class PageExtractor:
    """
    Extracts pages from a text document.

    Methods:
        extract_pages(text: str, start_page: int, end_page: int) -> str:
            Extracts pages from the given text.
    """

    def __init__(self, book_location_in_text: str, target_size: int = 3000) -> None:
        """
        Initializes the PageExtractor with the location of the book in text format.

        :param book_location_in_text: The path to the text file containing the book.
        """
        self.book_location_in_text = book_location_in_text
        self.target_size = target_size
        self.book_text = self._load_book_text()


    def find_chapter_boundaries(self) -> List[Tuple[int, str]]:
        """
        Finds chapter/section boundaries in the text using common keywords.

        Searches for patterns like: Chapter, Letter, Section, Part, Book, etc.
        Skips Table of Contents by only matching chapters that have substantial 
        content after them (100+ characters before next chapter marker).

        :param text: The text to search for chapter boundaries.
        :return: List of tuples (position, chapter_name) marking where chapters start.
        """
        # Match chapter markers more strictly:
        # "Chapter 1" or "Letter II" or "Section A" (keyword + number/numeral/letter only)
        pattern = r'(?:^|\n)\s*((?:Chapter|Letter|Section|Part|Book|Volume|Act|Scene|Prologue|Epilogue)(?:\s+(?:I{1,3}|V?I{0,3}|[0-9]+|[A-Z]|One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten))?)\s*(?:\n|$)'
        
        all_matches = list(re.finditer(pattern, self.book_text, re.IGNORECASE | re.MULTILINE))
        
        # Filter out TOC entries by checking if substantial content follows
        boundaries = []
        for i, match in enumerate(all_matches):
            chapter_name = match.group(1).strip()
            start_pos = match.start(1)
            
            # Look at content until next chapter marker or end of text
            next_pos = all_matches[i + 1].start(1) if i + 1 < len(all_matches) else len(self.book_text)
            content_length = next_pos - start_pos
            
            # Only include chapters with substantial content (> 200 chars)
            if content_length > 200:
                boundaries.append((start_pos, chapter_name))
        
        return boundaries

    def create_bite_sized_pages(self) -> List[Dict]:
        """
        Splits text into bite-sized pages for audiobook reading.

        Strategy: Tries to respect chapter boundaries while keeping pages close to target_size.
        If text has chapters, each page respects chapter breaks. Otherwise, splits by size.

        :param target_size: Target character count per page (default 3000 chars ≈ 8-10 min audio).
        :param target_size: Target character count per page (default 3000 chars ≈ 8-10 min audio).
        :return: List of dictionaries with keys: 'page_num', 'content', 'chapter', 'char_count'
        """
        boundaries = self.find_chapter_boundaries()
        pages = []
        
        if not boundaries:
            # No chapters found, split by size
            return self._split_by_size(self.book_text)
        
        # Build chapter positions: map each position to the next chapter's position
        chapter_positions = [(pos, name) for pos, name in boundaries]
        
        page_num = 1
        for i, (start_pos, chapter_name) in enumerate(chapter_positions):
            # Find the end: either start of next chapter or end of text
            if i + 1 < len(chapter_positions):
                end_pos = chapter_positions[i + 1][0]
            else:
                end_pos = len(self.book_text)
            
            # Extract chapter content (from the chapter marker to next chapter)
            chapter_text = self.book_text[start_pos:end_pos].strip()
            
            # If chapter is too large, subdivide it
            if len(chapter_text) > self.target_size:
                sub_pages = self._split_by_size(chapter_text)
                for sub_page in sub_pages:
                    pages.append({
                        'page_num': page_num,
                        'content': sub_page['content'],
                        'chapter': chapter_name,
                        'char_count': len(sub_page['content']),
                        'is_subdivided': True
                    })
                    page_num += 1
            else:
                pages.append({
                    'page_num': page_num,
                    'content': chapter_text,
                    'chapter': chapter_name,
                    'char_count': len(chapter_text),
                    'is_subdivided': False
                })
                page_num += 1
        
        return pages

    def _split_by_size(self, text: str) -> List[Dict]:
        """
        Helper method: Splits text into chunks of approximately target_size characters.

        Tries to split on sentence boundaries (periods) to avoid cutting mid-sentence.

        :param text: The text to split.
        :param target_size: Target size per chunk.
        :return: List of dictionaries with 'content' key.
        """
        pages = []
        sentences = text.split('. ')
        
        current_page = ""
        for sentence in sentences:
            if len(current_page) + len(sentence) + 2 < self.target_size:
                current_page += sentence + ". "
            else:
                if current_page:
                    pages.append({'content': current_page.strip()})
                current_page = sentence + ". "
        
        if current_page:
            pages.append({'content': current_page.strip()})
        
        return pages


    def _load_book_text(self) -> str:
        """
        Loads the book text from the specified file location.

        :return: The content of the book as a string.
        """
        with open(self.book_location_in_text, 'r', encoding='utf-8') as file:
            return file.read()