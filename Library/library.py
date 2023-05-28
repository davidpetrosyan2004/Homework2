import random
from student import Student
from generator import Generator


class Library:
    domen = "@polytechnic.am"

    def __init__(self, library_name):
        self.library_name = library_name
        self.students = set()
        self.books = set()

    def __str__(self):
        student_list = list(self.students)
        if not student_list:
            return "No students"

        return ", ".join(map(str, student_list[:2])) + (
            ", ..." if len(student_list) >= 2 else ""
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.library_name!r})"

    def add_student(self, student):
        student.email = Generator.generate_email(student, self.students, self.domen)
        student.ID = Generator.generate_id()
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

    @staticmethod
    def change_borrowing_limit(student, value):
        student.borrowing_limit = int(value)

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


if __name__ == "__main__":
    pass
