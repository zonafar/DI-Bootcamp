-- Exercise 1 : DVD Rentals
-- Instructions
-- Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
SELECT * FROM rental WHERE return_date ISNULL
-- Get a list of all customers who have not returned their rentals. Make sure to group your results.
SELECT customer.first_name,customer.last_name FROM rental
JOIN customer ON rental.customer_id = customer.customer_id
WHERE return_date ISNULL
GROUP BY customer.first_name,customer.last_name
-- Get a list of all the Action films with Joe Swank.
SELECT film.title,film.description,film.rating,film.length FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'Action'
AND actor.first_name = 'Joe'
AND actor.last_name = 'Swank';
-- Before you start, could there be a shortcut to getting this information? Maybe a view?
