class Book:
    def __init__(self, title, authors, year, ISBN, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.copybooks = set()
        self._available_copybooks = set()
        self.book_criterias = {title, authors, year, ISBN, genre}

    def __str__(self):
        return f"{self.title!s}(Authors:{self.authors}, Genre:{self.genre})"

    def __repr__(self):
        return "{0}({1!r},{2!r},{3!r},{4!r},{5!r})".format(
            self.__class__.__name__, *self.__dict__.values()
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.ISBN == other.ISBN
        return False

    def __hash__(self):
        return hash((self.title, self.authors, self.year, self.ISBN, self.genre))

    @property
    def available_copybooks(self):
        _available_copybooks = set()
        for copybook in self.copybooks:
            if copybook.borrower is None:
                _available_copybooks.add(copybook)
        return _available_copybooks

    @available_copybooks.setter
    def available_copybooks(self, copybooks_lst):
        _available_copybooks = copybooks_lst


if __name__ == "__main__":
    print([Book("Title", "n12416", 2, 4, 5)])
