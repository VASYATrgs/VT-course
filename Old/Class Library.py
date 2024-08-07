from Book import Book


class Library:

    def __init__(self):
        self.list_of_book = []

    def add_book (self, book):
        self.list_of_book.append(book)

    def remove_book (self):
        self.list_of_book.pop()

    def __str__(self):
        return str([str(book) for book in self.list_of_book])
    def find_book(self, name):
        for book in self.list_of_book:
            if name in book.name:
                return book

    @staticmethod
    def get_library_hours():
        return "09:00-18:00"

Library1 = Library()
book1 = Book("Алиса в стране чудес", "Льюис Карлтон", "1779")
book3 = Book("Ревизор", "Гоголь", "1839")
Library1.add_book(book1)
Library1.add_book(book3)
Library1.remove_book()

print(Library1)
print(Library1.find_book("Алиса в стране чудес"))

print(Library1.get_library_hours())