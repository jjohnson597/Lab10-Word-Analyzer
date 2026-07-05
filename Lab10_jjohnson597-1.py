"""
Program: Lab 10 Word Analyzer
Author: Jaylen Johnson
Purpose: Analyze selected text files and count word frequencies using OOP, pathlib, and string processing.
Starter code: No starter code was used.
Date: 7/5/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    """Analyze a text file and count the frequency of each word."""

    def __init__(self, filepath):
        """Initialize the analyzer with a file path and empty frequency dictionary."""
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Read the file and count the frequency of each word."""
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            remove_punctuation = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(remove_punctuation)
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath}' was not found.")
            return False
         
    def print_report(self):
        """Print the word frequency report in alphabetical order."""
        words = sorted(self.__frequencies.keys())

        for word in words:
            print(f"{word:<15} :: {self.__frequencies[word]}")   

    def main():
        """Display the menu and allow the user to analyze text files."""

        files = {
            "1": ("Princess Mars", Path("princess_mars.txt")),
            "2": ("Tarzan", Path("Tarzan.txt")),
            "3": ("Treasure Island", Path("treasure_island.txt")),
            "4": ("Monte Cristo", Path("monte_cristo.txt"))
            }
        
