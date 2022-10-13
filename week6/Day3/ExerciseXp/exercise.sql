-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.

SELECT language.name 
FROM film JOIN language ON film.language_id = language.language_id
GROUP BY language.name;
-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
SELECT film.title,film.description,language.name 
FROM film JOIN language ON film.language_id = language.language_id ;
-- Get all films, even if they don’t have languages.
SELECT film.title
FROM film LEFT JOIN language ON film.language_id = language.language_id ;
-- Get all languages, even if there are no films in those languages.
SELECT language.name
FROM film RIGHT JOIN language ON film.language_id = language.language_id ;
-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
DROP TABLE IF EXISTS new_film;
CREATE TABLE new_film(
	new_film_id SERIAL PRIMARY KEY,
	name varchar(255) NOT NULL
);
INSERT INTO new_film (name)
VALUES ('The outlier'),
	('Les trois lascars'),
	('The alchemist'),
	('DIEU n''estpas un parent');
	
-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
DROP TABLE IF EXISTS customer_review;
CREATE TABLE customer_review(
	review_id SERIAL NOT NULL,
	film_id INTEGER,
	language_id INTEGER NOT NULL,
	title VARCHAR(255) NOT NULL,
	score SMALLINT NOT NULL CHECK (score > 0 and score < 11),
	review_text TEXT,
	last_update TIMESTAMP,
	PRIMARY KEY(review_id),
	FOREIGN KEY (film_id) REFERENCES new_film (new_film_id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language (language_id) ON DELETE CASCADE
);
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id,language_id,title,score,review_text)
VALUES ((select new_film_id from new_film where name = 'The alchemist'),
	   (select language_id from language where name = 'English'),
		'Dream story',
		9,
		'This wonderful story is about the legend ofyoung shepherd who will later become an alchemist'
	   ),
	   ((select new_film_id from new_film where name = 'Les trois lascars'),
	   (select language_id from language where name = 'French'),
		'Nominee Fespaco',
		6,
		'Les trois lascars une réalisation de boubacar Diallo'
	   );
-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE name = 'The alchemist';
select * from customer_review;


-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id  = (select language_id from language where name = 'French')
WHERE film_id > 5 AND film_id < 15;

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
	
	-- Response : Customer_address_id_fkey is defined for the customer table. We need to give the right adress_id when we do insert

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE IF EXISTS customer_review;
-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT count(*) 
FROM rental WHERE return_date ISNULL;
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film.title 
FROM film JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IN (select inventory_id from rental where return_date isnull)
ORDER BY film.rental_rate DESC LIMIT 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
	-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT film.film_id,film.title,film.description FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.description ILIKE '%sumo wrestler%'
AND actor.last_name ILIKE '%Monroe%'
AND actor.first_name ILIKE '%Penelope%';
	-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT film.film_id,film.title,film.description FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.length < 60
AND film.rating ='R'
AND category.name = 'Documentary';
	-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT film.film_id,film.title,film.description FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON customer.customer_id = rental.customer_id
WHERE customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND film.rental_rate > 4
AND rental.return_date > '2005-07-28'
AND rental.return_date < '2005-08-01';
	-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT film.film_id,film.title,film.description,film.replacement_cost FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON customer.customer_id = rental.customer_id
WHERE customer.first_name = 'Matthew'
AND customer.last_name = 'Mahan'
AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
ORDER BY film.replacement_cost DESC LIMIT 1



