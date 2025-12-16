--Daily challenge: Tables Relationships

-- You are going to practice tables relationships

-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have thecolumns : id, isLoggedIn DEFAULT 
-- false (a Boolean), customer_id (a reference to the Customer table)

CREATE TABLE customer(
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(100) NOT NULL
);

CREATE TABLE customer_profile(
customer_profile_id SERIAL,
isLoggedIn BOOLEAN DEFAULT False,
customer_id INT UNIQUE, --UNIQUE so no two profiles can point to the same customer
PRIMARY KEY (customer_profile_id),
FOREIGN KEY
(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

--2. Insert those customers: John, Doe | Jerome, Lalu | Lea, Rive
INSERT INTO customer (first_name,last_name)
VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

--3. Insert those customer profiles, use subqueries John is loggedIn | Jerome is not logged in
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
(TRUE,(SELECT customer_id FROM customer WHERE first_name ='John')),
(FALSE,(SELECT customer_id FROM customer WHERE first_name ='Jerome'));

--4. Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers

SELECT customer.first_name
FROM customer
INNER JOIN customer_profile  --using INNER JOIN since it will return those where there is a match and there is a relation
ON customer.customer_id = customer_profile.customer_id
WHERE isLoggedIn = True;


-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT customer.first_name, customer_profile.isLoggedIn
FROM customer
LEFT JOIN customer_profile
ON customer.customer_id = customer_profile.customer_id; --we don't need a condition since we want to show everyone even if they don't have a profile

-- The number of customers that are not LoggedIn
SELECT COUNT (*) AS not_logged_in_customers
FROM customer
INNER JOIN customer_profile 
ON customer.customer_id = customer_profile.customer_id
WHERE isLoggedIn = FALSE; --as the first one but using count to see which customers are NOT log in


----
-- Part II:

--1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, 
-- title NOT NULL, author NOT NULL
CREATE TABLE Book(
book_id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
author VARCHAR(100) NOT NULL
);

--2. Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
INSERT INTO Book (title,author)
VALUES
('Alice In Wonderland','Lewis Carroll'),
('Harry Potter','J.K Rowling'),
('To kill a mockingbird','Harper Lee');

--3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age.
-- Make sure that the age is never bigger than 15 (Find an SQL method);
CREATE TABLE Student(
student_id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL UNIQUE,
age INTEGER CHECK (Age <= 15) NOT NULL
);

--4. Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14
INSERT INTO Student (name, age)
VALUES
('John',12),
('Lera',11),
('Patrick',10),
('Bob',14);

--5. Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

CREATE TABLE Library(
book_fk_id INTEGER NOT NULL,
student_fk_id INTEGER NOT NULL,
borrowed_date DATE NOT NULL,
PRIMARY KEY (book_fk_id, student_fk_id),
FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

--6. Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

INSERT INTO Library (student_fk_id,book_fk_id,borrowed_date)
VALUES
(
(SELECT student_id FROM Student WHERE name='John'),
(SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
'02/15/2022'),
(
(SELECT student_id FROM Student WHERE name='Bob'),
(SELECT book_id FROM Book WHERE title='To kill a mockingbird'),
'03/03/2021'),
(
(SELECT student_id FROM Student WHERE name='Lera'),
(SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
'05/23/2021'),
(
(SELECT student_id FROM Student WHERE name='Bob'),
(SELECT book_id FROM Book WHERE title='Harry Potter'),
'08/12/2021');

--7. Display the data
-- Select all the columns from the junction table
SELECT * FROM Library;

-- Select the name of the student and the title of the borrowed books
SELECT Student.name,Book.title
FROM Library
INNER JOIN Student ON Library.student_fk_id = Student.student_id
INNER JOIN Book ON Library.book_fk_id = Book.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT avg(student.age) AS average_age
FROM Library
INNER JOIN Student ON Library.student_fk_id = Student.student_id
INNER JOIN Book ON Library.book_fk_id = Book.book_id
WHERE Book.title iLike '%Alice in Wonderland%'; --using iLike since doing it with = returns Null, meaning no student actually matches all conditions

-- Delete a student from the Student table, what happened in the junction table?
DELETE FROM Student WHERE name= 'John';
SELECT * FROM Library; --by deleting John from the Student Table, it deleted his row also on the Library Table


