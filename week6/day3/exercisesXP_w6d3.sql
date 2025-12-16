-- EXERCISES XP

-- Exercise 1: DVD Rental

--1. Get a list of all the languages, from the language table.
SELECT * FROM language; --this shows the entire LANGUAGE table where we can see the list. 


--2. Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT film.title, film.description, language.name
FROM film
INNER JOIN language
ON film.language_id = language.language_id; -- since on the film table there is the language id, we use that to join to the id on the language table

--3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT film.title, film.description, language.name
FROM film
INNER JOIN language
ON film.film_id = language.language_id;

--4. Create a new table called new_film with the following columns : id, name. 
-- Add some new films to the table.
CREATE TABLE new_film(
newfilm_id SERIAL,
name TEXT,
PRIMARY KEY (newfilm_id)
);

INSERT INTO new_film(name)
VALUES
('The End of the Horizon'),
('Walking on the Moon'),
('City that Sleeps'),
('Working like a Penguin');

-- 5. Create a new table called customer_review, 
-- which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

CREATE TABLE customer_review(
review_id SERIAL,
film_id INTEGER NOT NULL,
language_id INTEGER NOT NULL,
title TEXT,
score INTEGER NOT NULL,
review_text TEXT,
last_update DATE,
PRIMARY KEY (review_id),
FOREIGN KEY (film_id) REFERENCES new_film(newfilm_id) ON DELETE CASCADE, --this will make that if deleted on the parent table, it will also be deleted on the child table
FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE SET NULL -- this makes that if deleted on the language table, it will not be deleted here but turned into a null value
);



--6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update)
VALUES
(
(SELECT newfilm_id FROM new_film WHERE name = 'The End of the Horizon'),
(SELECT language_id FROM language WHERE name = 'English'),
'MUST SEE MOVIE', 9, 'One of the best movies I have ever seen. A true Masterpiece', '12/12/2025'),
(
(SELECT newfilm_id FROM new_film WHERE name = 'Walking on the Moon'),
(SELECT language_id FROM language WHERE name = 'English'),
'AWFUL', 2, 'One of the worst movies I have ever seen. Dont waste your money', '12/05/2025');

SELECT * FROM customer_review;

--7. Delete a film that has a review from the new_film table, 
-- what happens to the customer_review table?

DELETE FROM new_film WHERE name='Walking on the Moon'; --it will also delete the review on the customer review

SELECT * FROM customer_review;




--Exercise 2 : DVD Rental
--1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 2
WHERE language_id = 1
-- this makes all the films where the language was english change to italian

-- 2. Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?

--ANSWER: the customer table has a foreign key on the customer_addressid which means that whenever
--INSERT a values to the customer table, we must make reference to the address table to get the address_id.

-- 3. We created a new table called customer_review. Drop this table. 
-- Is this an easy step, or does it need extra checking?

DROP TABLE customer_review; -- the table was an easy step to drop since it was a child table from the new_film table

--4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT * FROM rental;

SELECT COUNT(*) FROM rental WHERE rental_date != return_date -- by choosing the condition where the rental_date is not the same as the return_date, we can see which are still not returned

--5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT * FROM film;

SELECT replacement_cost
FROM film
WHERE replacement_cost > 20 ORDER BY replacement_cost DESC
FETCH FIRST 30 rows only; -- this will display the 30 most expensive movies in regards to their replacement COST

--6. Your friend is at the store, and decides to rent a movie.
-- He knows he wants to see 4 movies, but he can’t remember their names.
--Can you help him find which movies he wants to rent?

--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

SELECT *
FROM film
WHERE description ILIKE '%sumo wrestler%'; -- this will show us all the films where the word sumo wrestler is shown in the description. we need to narrow it down.

--USING join

SELECT film.title,film.description,actor.first_name,actor.last_name
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id --joins the table film and film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id -- joins the table film_actor and actor
WHERE
    film.description ILIKE '%sumo%' -- searches in the film description
    AND actor.first_name = 'Penelope' -- searches in the actor table
    AND actor.last_name = 'Monroe'; -- searches in the actor table

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT film.title, film.length, film.rating, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id --joins the tables film_category and film
JOIN category ON film_category.category_id = category.category_id -- joins the tables category and film_category
WHERE 
category.name = 'Documentary'
AND film.length < 60
AND film.rating = 'R'; -- using the same logic as before, this will shows us the short docu less than 1 hour and rating r

--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT  film.title, film.rental_rate, rental.return_date
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN payment ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE
customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND payment.amount > 4.00
AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'; --in this case we had to make 4 joins since we needed to see on the customer table, the rental table, the payment table and the film table and we had to choose from customer since that table was going to give us the connections

--The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description,
-- and it looked like it was a very expensive DVD to replace.

SELECT DISTINCT film.title, film.description,film.replacement_cost --by using DISTINCT it will not return duplicates, only uniques
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE
customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND film.title iLIKE '%boat%' OR film.description iLike '%boat%'
AND film.replacement_cost > 20
ORDER BY film.replacement_cost DESC;
--THIS will find all films Matthew Mahan rented, where the word “boat” appears in the title or description, the DVD is expensive to replace and returns the film title(s), sorted by how expensive they are