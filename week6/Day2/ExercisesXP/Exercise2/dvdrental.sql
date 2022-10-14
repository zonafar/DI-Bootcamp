-- 🌟 Exercise 2 : Dvdrental Database
-- Instructions
-- Setup
-- We will install a new sample database on our PostgreSQL servers.
-- Download this sample database file

-- There is a single file called dvdrental.tar inside the zip. Extract it to your local directory.
-- Tip : If you are using Mac, after extracting the zip file you will get a folder called dvdrental

-- Go to pgAdmin4, and navigate to Databases on the left panel.

-- Right click > Create > Database…

-- Type in the name of the new database: dvdrental, and click Save. Wait a few moments.

-- Right click on dvdrental under Databases in the left panel.

-- Click Restore….

-- For PC users choose the following format Custom or tar. For Mac Users, choose the following format Directory.

-- Next to Filename, you should see a button with 3 dots on it. Click the button.

-- For PC users: “Find your file in the window”. For Max users: “Find your folder in the window”. (you may have to check Show hidden files and folders?), and click the Select button.

-- If you receive a “Utility not found” Error, you need to change pgadmin binary path. Check out this video

-- If you see any error messages, please save them and get assistance. If not, you should have a new database loaded into your server!

-- Here is a diagram of the tables in the server. Take a look at it and learn about the tables, their columns, and the relationships between the different tables.

-- We will use the newly installed dvdrental database.

-- In the dvdrental database write a query to select all the columns from the “customer” table.
SELECT * FROM customer;
-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT (last_name,first_name) AS full_name FROM customer;
-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT DISTINCT create_date FROM customer;
-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT * FROM customer ORDER BY first_name DESC;
-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate;
-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT address,phone FROM address INNER JOIN customer ON address.address_id = customer.address_id;
-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM film WHERE film_id=15 OR film_id = 150;
-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE '%Turn star%' ;
-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'The%' ;
-- Write a query which will find the 10 cheapest movies.
SELECT film_id,title,description,film.length,rental_rate,replacement_cost FROM film ORDER BY replacement_cost DESC LIMIT 10;
-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
SELECT film_id,title,description,film.length,rental_rate,replacement_cost FROM film ORDER BY replacement_cost DESC LIMIT 10 OFFSET 10;
-- Bonus: Try to not use LIMIT.

-- Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT film.film_id,film.title FROM film,inventory WHERE film.film_id != inventory.film_id;
-- Write a query to find which city is in which country.
SELECT city.country_id,city.city,country.country_id,country.country FROM city INNER JOIN country ON city.country_id = country.country_id; 
-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT customer.customer_id,customer.first_name,customer.last_name,payment.amount,payment.payment_date,payment.staff_id
FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id
ORDER BY payment.staff_id; 
-- 
-- UPDATE film SET title = 'The fault in our stars' WHERE film_id = 1 RETURNING title,description;
