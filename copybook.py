class BookCopy:

    def __init__(self, book, copy_ID, borrower=None, borrowed_date=None, loan=False):
        self.book = book
        self.copy_ID = copy_ID
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.loan = loan
        self._condition_rating = 10

    def borrow_copybook(self):
        pass

    def get_copybook(self):
        pass

    @property
    def condition_rating(self):
        pass

    @property.setter()
    def condition_rating(self, value):
        pass


if __name__ == '__main__':
    pass