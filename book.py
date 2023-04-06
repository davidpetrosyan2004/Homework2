class Book:
    def __init__(self, title, authors, year, ISBN, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.copy_books = []
        self._available_copybooks = []

    def add_copybook(self, copybook):
        pass

    @property
    def available_copybooks(self):
        pass

if __name__ == '__main__':
    pass