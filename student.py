class Student:
    borrowing_limit = 5
    due_date = 14

    def __init__(self, name, ID, email, copybooks):
        self.name = name
        self.ID = ID
        self.email = email
        self.copybooks = copybooks

    def borrow_book(self, title):
        pass

    def get_book(self):
        pass

    def books_status(self):
        pass


if __name__ == '__main__':
    pass