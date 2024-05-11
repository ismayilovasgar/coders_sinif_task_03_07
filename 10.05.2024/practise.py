class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added '{book.title}' to the library."

    def display_available_books(self):
        if self.books:
            available_books = [str(book) for book in self.books if book.available]
            if available_books:
                return "Available Books:\n" + "\n".join(available_books)
            else:
                return "No books available in the library."
        else:
            return "No books available in the library."

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return f"Borrowed '{book.title}' from the library."
        return f"Book '{title}' is either unavailable or does not exist in the library."


    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return f"Returned '{book.title}' to the library."
        return f"Book '{title}' was not borrowed or does not exist in the library."


    def display_borrowed_books(self):
        borrowed_books = [str(book) for book in self.books if not book.available]
        if borrowed_books:
            return "Borrowed Books:\n"+"\n".join(borrowed_books)
        else:
            return "No books are currently borrowed."


library = Library()

# Adding books to the library
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display available books
print(library.display_available_books())

# # Borrow a book
print(library.borrow_book("Harry Potter and the Philosopher's Stone"))
print(library.borrow_book("To Kill a Mockingbird"))

print(library.borrow_book("Homo Sapiens"))


# # # Display borrowed books
print(library.display_borrowed_books())

# # # Return a borrowed book
print(library.return_book("Harry Potter and the Philosopher's Stone"))
