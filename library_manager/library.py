import uuid
from typing import List
from library_manager.book import Book
from library_manager.utils import load_books, save_books


class Library:
    """
    A class for managing a book library.

    Attributes:
        books (List[Book]): List of books in the library.
    """

    def __init__(self):
        """
        Initializes the library by loading books from a file.
        """
        self.books = load_books()

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Adds a new book to the library.

        Parameters:
            title (str): Title of the book.
            author (str): Author of the book.
            year (int): Publication year of the book.
        """
        id = str(uuid.uuid4())
        new_book = Book(id, title, author, year)
        self.books.append(new_book)
        save_books(self.books)

    def remove_book(self, book_id: str) -> bool:
        """
        Removes a book from the library by its unique identifier.

        Parameters:
            book_id (str): Unique identifier of the book.

        Returns:
            bool: True if the book was successfully removed, False otherwise.
        """
        if any(book.id == book_id for book in self.books):
            self.books = [book for book in self.books if book.id != book_id]
            save_books(self.books)
            return True
        else:
            return False

    def find_books(self, **kwargs) -> List[Book]:
        """
        Finds books by given criteria.

        Parameters:
            **kwargs: Search criteria (e.g., title, author, year).

        Returns:
            List[Book]: List of books that match the search criteria.
        """
        return [book for book in self.books if all(getattr(book, k) == v for k, v in kwargs.items())]

    def list_books(self) -> List[Book]:
        """
        Gets a list of all books in the library.

        Returns:
            List[Book]: List of all books.
        """
        return self.books

    def change_status(self, book_id: str, new_status: str) -> None:
        """
        Changes the status of a book by its unique identifier.

        Parameters:
            book_id (str): Unique identifier of the book.
            new_status (str): New status of the book ("available" or "checked out").
        """
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                break
        save_books(self.books)
