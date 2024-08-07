class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def __str__(self):
        return (f"{self.name} {self.author} {self.year}")



book1 = Book("Евгений Онегин", "Пушкин",  "1833")
book2 = Book("Война и мир", "Лев Толстой", "1867" )

print(book1, book2)

class Library:

    def __init__(self, name, author, year):
        self.name = []
        self.author = author
        self.year = year
    def add_(self, name, author, year):



