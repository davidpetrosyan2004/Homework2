import random
from Homework2.Library.student import Student

class Library:
    domen = "@polytechnic.am"

    def __init__(self, library_name):
        self.library_name = library_name
        self.students = set()
        self.books = set()

    def __str__(self):
        return "{0}, {1}...".format(*self.students if self.students else ("No", "students"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.library_name!r})"

    def add_student(self, student):
        student.email = self.generate_email(student)
        student.ID = self.generate_ID()
        student.library = self
        self.students.add(student)

    def remove_student(self, ID):
        for student in self.students:
            if student.ID == ID:
                return self.students.remove(student)

        raise Exception(f"No such a student({ID}) in Library of {self.library_name}")

    def add_book(self, book):
        self.books.add(book)

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return self.books.remove(book)

        raise Exception(f"No such a book({ISBN}) in Library of {self.library_name!r}")

    def change_borrowing_limit(self, value):
        Student.borrowing_limit = int(value)

    @property
    def available_books(self):
        _available_books = set()
        for book in self.books:
            if book.available_copybooks:
                _available_books.add(book)
        return _available_books

    def get_book_by_criteria(self, title, *criterias):
        criterias = {criteria for criteria in criterias}
        criterias.add(title)
        for book in self.books:
            if criterias <= book.book_criterias:
                return book
        raise Exception(f"Can't find this book in library")

    def generate_email(self, student):
        dup_count = 0
        for stud in self.students:
            if student == stud:
                dup_count += 1
        message = (
            f"{student.name}.{student.surname}{dup_count}.y{self.domen}"
            if dup_count != 0
            else f"{student.name}.{student.surname}{self.domen}"
        )

        return message

    @staticmethod
    def generate_ID():
        ID = ""
        for i in range(12):
            ID += str(random.randint(0, 1000))

        return ID[:12]


if __name__ == "__main__":
    pass
