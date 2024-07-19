import json
import os
from typing import List
from library_manager.book import Book


def load_books() -> List[Book]:
    """
    Load and return a list of Book objects from a JSON file.

    Returns:
        List[Book]: List of Book objects.

    Raises:
        FileNotFoundError: If the JSON file is missing.
        json.JSONDecodeError: If the JSON is invalid.
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'books.json')
    with open(file_path, 'r') as file:
        books_data = json.load(file)
        return [Book(**book) for book in books_data]


def save_books(books: List[Book]) -> None:
    """
    Save a list of Book objects to a JSON file.

    Args:
        books (List[Book]): List of Book objects to save.

    Raises:
        IOError: If there is an error writing the file.
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'books.json')
    with open(file_path, 'w') as file:
        json.dump([book.__dict__ for book in books], file, ensure_ascii=False, indent=4)
