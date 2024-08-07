class Book(object):
    def __init__(self,
                 title="",
                 authors=[],
                 year=None):
        self.title = title
        self.authors = authors
        self.year = year
    def __add__(self, title, authors, year):
    def __str__(self):
        return str(self.__dict__)



book1 = Book("Евгений Онегин", "Пушкин",  "1833")
book2 = Book("Война и мир", "Лев Толстой", "1867" )

print(Book)
