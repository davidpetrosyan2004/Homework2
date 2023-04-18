import datetime
import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)


class Student:
    def __init__(self, name, surname, borrowing_limit=5):
        self.name = name
        self.surname = surname
        self.copybooks = set()
        self.borrowing_limit = borrowing_limit
        self.email = None
        self.ID = None
        self.library = None

    def __str__(self):
        return f"{self.name}(ID:{self.ID})"

    def __repr__(self):
        return "{0}({1!r},{2!r},{3!r},{4!r},{5!r})".format(
            self.__class__.__name__, *self.__dict__.values()
        )

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.surname == other.surname

    def __hash__(self):
        return 1

    def borrow_book(self, title):
        if self.valid_student:
            book = self.library.get_book_by_criteria(title)
            if book.available_copybooks:
                copybook = book.available_copybooks.pop()
                copybook.borrow_copy(self)
                return copybook

            raise Exception(f"There is not available books named {title!r}")

        raise Exception("Your limit has been reached or u have expired books")

    def books_status(self):
        if self.copybooks:
            message = "\n".join(
                [
                    f"{copybook!s} - {copybook.due_date} days"
                    for copybook in self.copybooks
                ]
            )
        else:
            message = "There is no books"
        logging.info(message)

    @property
    def valid_student(self):
        if len(self.copybooks) < self.borrowing_limit:
            count = 0
            for copybook in self.copybooks:
                if copybook.due_date >= 0:
                    count += 1
            return count == len(self.copybooks)

        return False


if __name__ == "__main__":
    pass
