class Book:
    def __init__(self, title, authors, year, ISBN, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.copybooks = set()
        self.available_copybooks = set()
        self.book_criterias = {title, authors, year, ISBN, genre}

    def __str__(self):
        return f"{self.title!r}(Authors:{self.authors}, Genre:{self.genre})"

    def __repr__(self):
        return "{0}({1!r},{2!r},{3!r},{4!r},{5!r})".format(
            self.__class__.__name__, *self.__dict__.values()
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.ISBN == other.ISBN

    def __hash__(self):
        return 1

    # def __contains__(self, item):
    #     lst = [copybook.title for copybook in self.available_copybooks]
    #     return item.title in lst


if __name__ == "__main__":
    print([Book("Title", "n12416", 2, 4, 5)])
