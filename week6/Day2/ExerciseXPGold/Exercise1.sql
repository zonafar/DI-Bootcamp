-- Exercise 1: DVD Rental
-- Instructions
-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
select * from film;
-- Find out how many films there are for each rating.
SELECT count(*) AS number_of_film,rating FROM film GROUP BY rating;
-- Get a list of all the movies that have a rating of G or PG-13.
SELECT * FROM film WHERE rating = 'G' OR rating = 'PG-13';
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT * FROM film WHERE (rating = 'G' OR rating = 'PG-13')
AND film.length < 120
AND film.rental_rate < 3.00
ORDER BY film.title ASC
;
-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer 
SET first_name = 'Abdoul Gafar',
last_name = 'ZONGO',
email = 'abdoul.gafar@gmail.com',
create_date = '2022/09/29'
WHERE customer_id = 7
RETURNING *;
-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
SELECT * FROM address 
WHERE address.address_id = (select address_id from customer where customer_id = 7); 

UPDATE address
SET address = 'Rue 16 saint-etienne',
address2 = '360 Rue 24',
district = 'Houet',
postal_code = '987456'
WHERE address_id = (select address_id from customer where customer_id = 7)
RETURNING *;

