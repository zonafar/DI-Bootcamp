-- Daily Challenge: Tables Relationships
-- Instructions
-- You are going to practice tables relationships

-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL

CREATE TABLE customers(
	customer_id SERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(60) NOT NULL,
	last_name VARCHAR(60) NOT NULL
);
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
DROP TABLE IF EXISTS customer_profile;
CREATE TABLE customer_profile (
	customer_profile_id INTEGER NOT NULL,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	CONSTRAINT fk_customer_profile
      FOREIGN KEY(customer_profile_id) 
	  REFERENCES customers(customer_id)
);
-- Insert those customers
-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
INSERT INTO customers (first_name,last_name)
VALUES ('John','Doe'),
		('Jerome','Lalu'),
		('Lea','Rive')
-- Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in
INSERT INTO customer_profile(customer_profile_id,isLoggedIn)
VALUES ((select customer_id from customers where first_name = 'John'),TRUE),
		((select customer_id from customers where first_name = 'Jerome'),FALSE)
		
-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
SELECT customers.first_name FROM customers
JOIN customer_profile ON customer_profile.customer_profile_id = customers.customer_id
WHERE customer_profile.isLoggedIn = TRUE;
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT customers.first_name,customer_profile.isLoggedIn FROM customers
LEFT JOIN customer_profile ON customer_profile.customer_profile_id = customers.customer_id;
-- The number of customers that are not LoggedIn
SELECT count(customers.first_name) FROM customers
JOIN customer_profile ON customer_profile.customer_profile_id = customers.customer_id
WHERE customer_profile.isLoggedIn = FALSE;



-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
CREATE TABLE book (
	book_id SERIAL PRIMARY KEY, 
	title VARCHAR(200) NOT NULL, 
	author VARCHAR(100) NOT NULL 
);
-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
INSERT INTO book (title,author)
VALUES ('Alice In Wonderland','Lewis Carroll'),
		('Harry Potter','J.K Rowling'),
		('To kill a mockingbird','Harper Lee');

-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
CREATE TABLE student (
	student_id SERIAL PRIMARY KEY, 
	name VARCHAR(100) NOT NULL UNIQUE, 
	age INTEGER
);
-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14
INSERT INTO student (name,age)
VALUES ('John',12),
		('Lera',11),
		('Patrick',10),
		('Bob',14);
		
-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

CREATE TABLE library(
	book_id INTEGER NOT NULL,
	student_id INTEGER NOT NULL,
	borrowed_date DATE,
	CONSTRAINT book_fk_id FOREIGN KEY (book_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT student_fk_id FOREIGN KEY (student_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY (book_id,student_id)
);

-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
INSERT INTO library (book_id,student_id,borrowed_date)
VALUES (
	(select book_id from book where title ILIKE '%kill a mockingbird%'),
	(select student_id from student where name = 'Bob'),
	'03/03/2021'),
	((select book_id from book where title ILIKE '%Alice In Wonderland%'),
	(select student_id from student where name = 'Lera'),
	'23/05/2021'),	
	((select book_id from book where title ILIKE '%Harry Potter%'),
	(select student_id from student where name = 'Bob'),
	'12/08/2021'),
	((select book_id from book where title ILIKE '%Alice In Wonderland%'),
	(select student_id from student where name = 'John'),
	'15/02/2022');
	
-- Display the data
-- Select all the columns from the junction table
select * from library;
-- Select the name of the student and the title of the borrowed books
SELECT student.name, student.age,book.title FROM student
JOIN library ON library.student_id = student.student_id
JOIN book ON book.book_id = library.book_id;
-- Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT AVG(student.age) as Age FROM student
JOIN library ON library.student_id = student.student_id
JOIN book ON book.book_id = library.book_id
WHERE book.title ILIKE '%Alice in Wonderland%';

-- Delete a student from the Student table, what happened in the junction table ?
DELETE FROM student
WHERE name ILIKE '%John%';

select *from student;
select *from library;

