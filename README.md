# 📚 Library Management System

## 🚀 Description
This is a console application for managing a book library. It allows you to add, remove, search for, display books, and change their status. Books are stored in a JSON file, allowing data to be saved and loaded when the application starts.

## 🛠️ Features
- **Add a Book**: Add a new book with a unique identifier.
- **Remove a Book**: Remove a book by its unique identifier.
- **Search for a Book**: Search for books by title, author, or publication year.
- **List Books**: Display all books in the library.
- **Change Book Status**: Change the status of a book (available or checked out).

## 📜 Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/askanio8/library_manager.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd project-name
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## 📋 Commands
Enter one of the following commands in the console:

- `add`: Add a book. Prompts for title, author, and publication year.
- `remove`: Remove a book. Prompts for book ID.
- `find`: Find books by the specified field (title, author, year).
- `list`: Show all books in the library.
- `change`: Change a book's status. Prompts for book ID and new status.
- `exit`: Exit the application.

## 🔧 Example Usage

1. **Adding a Book**:
    ```
    Enter command (add, remove, find, list, change, exit): add
    Enter title: The Lord of the Rings
    Enter author: J. R. R. Tolkien
    Enter publication year: 1954
    ```

2. **Removing a Book**:
    ```
    Enter command (add, remove, find, list, change, exit): remove
    Enter book ID: 123e4567-e89b-12d3-a456-426614174000
    ```

3. **Finding a Book**:
    ```
    Enter command (add, remove, find, list, change, exit): find
    Enter search field (title, author, year): author
    Enter value: J. R. R. Tolkien
    ```

4. **Listing Books**:
    ```
    Enter command (add, remove, find, list, change, exit): list
    ```

5. **Changing Book Status**:
    ```
    Enter command (add, remove, find, list, change, exit): change
    Enter book ID: 123e4567-e89b-12d3-a456-426614174000
    Enter new status (available, checked out): checked out
    ```

## 📄 License
This project is licensed under the [MIT License](LICENSE).

