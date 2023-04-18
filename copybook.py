import datetime
from library import Library


class BookCopy:
    def __init__(self, book, copy_ID, loan=False):
        self.book = book
        self.copy_ID = copy_ID
        self.loan = loan
        self.condition_rating = 10
        self.borrower = None
        self.borrowed_date = None
        self._due_date = 14
        self.book.available_copybooks.add(self)
        self.book.copybooks.add(self)

    def __str__(self):
        return f"{self.book!s}(copy)"

    def __repr__(self):
        return "{0}({1!r},{2!r},{3!r})".format(
            self.__class__.__name__, *list(self.__dict__.values())
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.book == other.book

    def __hash__(self):
        return int(Library.generate_ID())

    def borrow_copy(self, student):
        for copybook in student.copybooks:
            if copybook.book == self.book:
                raise Exception(f"You already have a book named {self.book.title!r}")
        self.borrowed_date = datetime.datetime.now()
        self.borrower = student.name + student.surname
        student.copybooks.add(self)

    @property
    def due_date(self):
        self._due_date -= (datetime.datetime.now() - self.borrowed_date).days
        return self._due_date


if __name__ == "__main__":
    pass
