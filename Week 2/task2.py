import json
import os


class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["is_issued"]
        )


class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = {}  # HashMap-like dict {book_id: Book}
        self.load_data()

    # -------------------------
    # Add Book
    # -------------------------
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists!")
            return
        self.books[book_id] = Book(book_id, title, author)
        self.save_data()
        print("Book added successfully.")

    # -------------------------
    # Search Book
    # -------------------------
    def search_by_title(self, title):
        results = [book for book in self.books.values()
                   if title.lower() in book.title.lower()]
        return results

    def search_by_author(self, author):
        results = [book for book in self.books.values()
                   if author.lower() in book.author.lower()]
        return results

    # -------------------------
    # Issue Book
    # -------------------------
    def issue_book(self, book_id):
        if book_id in self.books and not self.books[book_id].is_issued:
            self.books[book_id].is_issued = True
            self.save_data()
            print("Book issued successfully.")
        else:
            print("Book not available.")

    # -------------------------
    # Return Book
    # -------------------------
    def return_book(self, book_id):
        if book_id in self.books and self.books[book_id].is_issued:
            self.books[book_id].is_issued = False
            self.save_data()
            print("Book returned successfully.")
        else:
            print("Invalid book ID or book not issued.")

    # -------------------------
    # Reports
    # -------------------------
    def total_books(self):
        return len(self.books)

    def issued_count(self):
        return sum(book.is_issued for book in self.books.values())

    # -------------------------
    # File Handling
    # -------------------------
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(
                {book_id: book.to_dict() for book_id, book in self.books.items()},
                f,
                indent=4
            )

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for book_id, book_data in data.items():
                    self.books[book_id] = Book.from_dict(book_data)


# -------------------------
# Simple CLI Menu
# -------------------------
def main():
    library = Library()

    while True:
        print("\n===== Library Book Inventory Manager =====")
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Reports")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            title = input("Enter title: ")
            results = library.search_by_title(title)
            for book in results:
                print(book.book_id, book.title, book.author, book.is_issued)

        elif choice == "3":
            author = input("Enter author: ")
            results = library.search_by_author(author)
            for book in results:
                print(book.book_id, book.title, book.author, book.is_issued)

        elif choice == "4":
            book_id = input("Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "5":
            book_id = input("Book ID to return: ")
            library.return_book(book_id)

        elif choice == "6":
            print("Total Books:", library.total_books())
            print("Issued Books:", library.issued_count())

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()