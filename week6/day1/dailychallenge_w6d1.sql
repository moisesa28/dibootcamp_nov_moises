-- Daily Challenge: Actors
-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  birth_date DATE NOT NULL,
--  number_oscars SMALLINT
-- )

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970',5);

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES ('Meryl', 'Streep', '04/09/1964', 7);
-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES ('Sandra', 'Bullock', '08/03/1975', 1);

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES
-- ('Marlon', 'Brandon', '02/02/1934',3),
-- ('Al', 'Pacino','07/10/1959', 2),
-- ('Jane','Fonda','08/04/1960',1);


-- SELECT * FROM actors

-- the following tells us how many actors are in our table:
-- SELECT COUNT (*) AS total_actors
-- FROM actors

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- -- VALUES ('Robert', 'De Niro', NULL, NULL) -- here we can't place NULL as the birth_date since it violates the not null constraint
-- VALUES ('Robert','De Niro','06/23/1946', NULL)

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES ('', '','07/15/1956',NULL)

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES ('Denzel', '', '05/15/1959',2)

-- SELECT *FROM actors