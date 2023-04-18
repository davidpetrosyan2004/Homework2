from copybook import BookCopy
from book import Book
from library import Library
from student import Student


def main():
    library = Library("Polytechnic University of Armenia")

    # Initializing students
    student_1 = Student("David", "Petrosyan")
    student_2 = Student("David", "Petrosyan")

    student_3 = Student("Mher", "Petrosyan")
    student_4 = Student("Mher", "Petrosyan")

    # Initializing books
    book_1 = Book(
        "The Little Prince", "Antoine de Saint-Exupéry", 1943, "11111111111", "story"
    )
    book_2 = Book(
        "War and Peace", "Leo Tolstoy", 1869, "22222222222", "Historical novel"
    )
    book_3 = Book(
        "The Adventures of Sherlock Holmes",
        "Arthur Conan Doyle",
        1892,
        "33333333333",
        "Detective fiction",
    )
    book_4 = Book(
        "Harry Potter and the Philosopher's Stone",
        "	J. K. Rowling",
        1997,
        "44444444444",
        "Fantasy",
    )
    book_5 = Book(
        "Jonathan Livingston Seagull", "Richard Bach", 1970, "55555555555", "Novella"
    )
    book_6 = Book(
        "She: A History of Adventure",
        "H. Rider Haggard",
        1887,
        "66666666666",
        "Adventure",
    )

    # Initializing copybooks
    copybook_1 = BookCopy(book_1, "00128765237")
    copybook_2 = BookCopy(book_2, "10128765230")
    copybook_3 = BookCopy(book_3, "20128765232")
    copybook_4 = BookCopy(book_4, "30121245676")
    copybook_5 = BookCopy(book_5, "4128761245")
    copybook_5 = BookCopy(book_6, "512128761245")

    # Adding books to library
    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    library.add_book(book_4)
    library.add_book(book_5)
    library.add_book(book_6)

    # Adding students to library
    library.add_student(student_1)
    library.add_student(student_2)

    library.add_student(student_3)
    library.add_student(student_4)

    # print(student_1.email, student_1.ID)
    # print(student_2.email, student_2.ID)
    #
    # print(student_3.email, student_3.ID)
    # print(student_4.email, student_4.ID)
    #
    # library.remove_student("012985727213")
    # library.remove_book("129837236871")

    # book = library.get_book_by_criteria("127673781982")

    copybook1 = student_1.borrow_book("The Little Prince")
    copybook2 = student_1.borrow_book("The Adventures of Sherlock Holmes")
    copybook3 = student_1.borrow_book("Harry Potter and the Philosopher's Stone")
    copybook4 = student_1.borrow_book("Jonathan Livingston Seagull")
    copybook5 = student_1.borrow_book("She: A History of Adventure")
    copybook6 = student_1.borrow_book("War and Peace")

    print(student_1.copybooks)

    # student_1.books_status()


if __name__ == "__main__":
    main()
