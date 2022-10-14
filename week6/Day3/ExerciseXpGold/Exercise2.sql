-- Exercise 2 – Happy Halloween
-- Instructions
-- There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:

-- How many stores there are, and in which city and country they are located.
SELECT store.store_id, city.city, country.country FROM store
JOIN address ON address.address_id = store.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id;

-- How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
SELECT sum(film.length) FROM film
JOIN inventory ON inventory.film_id = film.film_id
JOIN store ON store.store_id = inventory.store_id
GROUP BY store.store_id;
-- Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)
DELETE FROM film WHERE film.film_id IN(
SELECT film.film_id FROM film
JOIN inventory ON inventory.film_id = film.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
WHERE rental.return_date ISNULL);
-- A list of all customers in the cities where the stores are located.
SELECT DISTINCT customer.first_name,customer.last_name FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN store ON store.address_id = store.address_id
JOIN city ON city.city_id = address.city_id;

-- A list of all customers in the countries where the stores are located.
SELECT DISTINCT customer.first_name,customer.last_name FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN store ON store.address_id = store.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON city.country_id = country.country_id;
-- Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
-- Hint : use the CHECK contraint
-- words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length)
SELECT film.film_id,film.title,film.description FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE NOT ((film.title ILIKE '%beast%' or film.title ILIKE '%monster%'
		   or film.title ILIKE '%ghost%' or film.title ILIKE '%dead%' or
		   film.title ILIKE '%undead%' or film.title ILIKE '%zombie%' )
		OR (film.description ILIKE '%beast%' or film.description ILIKE '%monster%'
		   or film.description ILIKE '%ghost%' or film.description ILIKE '%dead%' or
		   film.description ILIKE '%undead%' or film.description ILIKE '%zombie%' ))
AND category.name = 'Horror'; 
-- For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).