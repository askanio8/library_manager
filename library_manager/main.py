from library_manager.library import Library


def main():
    library = Library()

    while True:
        command = input("Enter command (add, remove, find, list, change, exit): ").strip()

        if command == "add":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            year_input = input("Enter publication year: ").strip()

            if not title or not author or not year_input:
                print("All fields must be filled in.")
            elif not year_input.isdigit():
                print("Publication year must be a number.")
            else:
                year = int(year_input)
                if year < 1000 or year > 9999:  # Assuming a reasonable year range
                    print("Publication year must be a valid year.")
                else:
                    library.add_book(title, author, year)
                    print("Book added successfully.")

        elif command == "remove":
            book_id = input("Enter book ID: ").strip()
            if library.remove_book(book_id):
                print("Book successfully removed.")
            else:
                print("No book found with that ID.")

        elif command == "find":
            key = input("Enter search field (title, author, year): ").strip()
            if key in ["title", "author"]:
                value = input("Enter value: ").strip()
                books = library.find_books(**{key: value})
                if books:
                    for book in books:
                        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
                else:
                    print("No books found matching the criteria.")
            elif key == "year":
                value = input("Enter value: ").strip()
                if value.isdigit():
                    value = int(value)
                    if value < 1000 or value > 9999:
                        print("Invalid year.")
                    else:
                        books = library.find_books(**{key: value})
                        if books:
                            for book in books:
                                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
                        else:
                            print("No books found matching the criteria.")
                else:
                    print("Invalid year.")
            else:
                print("Invalid search field.")

        elif command == "list":
            books = library.list_books()
            if books:
                for book in books:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            else:
                print("No books in the library.")

        elif command == "change":
            book_id = input("Enter book ID: ").strip()
            new_status = input("Enter new status (available, checked out): ").strip()
            if new_status in ["available", "checked out"]:
                if library.change_status(book_id, new_status):
                    print("Book status updated successfully.")
                else:
                    print("No book found with that ID.")
            else:
                print("Invalid status.")

        elif command == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
