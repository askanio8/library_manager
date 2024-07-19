import unittest
from library_manager.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        initial_count = len(self.library.books)
        self.library.add_book("Test Title", "Test Author", 2024)
        self.assertEqual(len(self.library.books), initial_count + 1)

    def test_remove_book(self):
        self.library.add_book("To Remove", "Author", 2024)
        book_id = self.library.books[-1].id
        self.library.remove_book(book_id)
        self.assertNotIn(book_id, [book.id for book in self.library.books])


if __name__ == '__main__':
    unittest.main()
