class Book:
    """
    A class representing a book.

    Attributes:
        id (str): Unique identifier of the book.
        title (str): Title of the book.
        author (str): Author of the book.
        year (int): Publication year of the book.
        status (str): Status of the book ("available" or "checked out"). Defaults to "available".
    """

    def __init__(self, id: str, title: str, author: str, year: int, status: str = "available"):
        """
        Initializes a book object.

        Parameters:
            id (str): Unique identifier of the book.
            title (str): Title of the book.
            author (str): Author of the book.
            year (int): Publication year of the book.
            status (str): Status of the book. Defaults to "available".
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
