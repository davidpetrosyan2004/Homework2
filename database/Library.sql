CREATE TABLE library (
	id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(150)
);

CREATE TABLE students (
	id SERIAL NOT NULL PRIMARY KEY,
	library_id INT REFERENCES library(id),
	first_name VARCHAR(50),
	second_name VARCHAR(50),
	email VARCHAR(50),
	borrowing_limit INT
);

CREATE TABLE authors (
	id SERIAL NOT NULL PRIMARY KEY,
	book_id INT REFERENCES books(id),
	first_name VARCHAR(50),
	second_name VARCHAR(50)
);

CREATE TABLE books (
	id SERIAL NOT NULL PRIMARY KEY,
	title VARCHAR(150),
	year DATE,
	isbn VARCHAR(150),
	genre VARCHAR(150)
);

CREATE TABLE copybooks (
	id SERIAL NOT NULL PRIMARY KEY,
	student_id INT REFERENCES students(id),
	book_id INT REFERENCES books(id),
	loan VARCHAR(150),
	condition_rating INT,
	borrowed_date DATE
);

CREATE TABLE borrows (
	id SERIAL NOT NULL PRIMARY KEY,
	copybook_id INT REFERENCES copybooks(id),
	student_id INT REFERENCES  students(id),
	borrow_date DATE NOT NULL,
	return_date DATE
);

CREATE TABLE books_authors (
	id SERIAL NOT NULL PRIMARY KEY,
	author_id INT NOT NULL REFERENCES authors(id),
	book_id INT NOT NULL REFERENCES books(id)
);