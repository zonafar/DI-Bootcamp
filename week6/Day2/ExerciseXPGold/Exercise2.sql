-- Exercise 3 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Part I

-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer

ALTER TABLE customers ADD CONSTRAINT pk_customer PRIMARY KEY (customer_id);
ALTER TABLE items ADD CONSTRAINT pk_item PRIMARY KEY (item_id);
CREATE TABLE purchase (
	pursache_id SERIAL PRIMARY KEY,
	customer_id INT,
	item_id INT,
	quantity_purchased integer,
	CONSTRAINT fk_customer_purchase FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
	CONSTRAINT fk_item_purchase FOREIGN KEY(item_id) REFERENCES items(item_id)
);

-- Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bougth two small desks
-- The table purchases should look like this:

-- id	customer_id	item_id	quantity_purchased
-- 1	3	3	1
-- 2	5	2	10
-- 3	1	1	2


-- Here is the explanation of the first row:

-- id = 1, this is the auto-incrementing primary key
-- customer_id = 3, because the id of Scott Scott in the customers table is 3
-- item_id = 3, because the id of a fan in the items table is 3
-- quantity_purchased = 1, because Scott Scott bought one fan
select * from items;
select * from purchase;
select * from customers;
INSERT INTO purchase (customer_id,item_id,quantity_purchased)
VALUES (
	(select customer_id from customers where first_name = 'Scott' and last_name = 'Scott'),
	(select item_id from items where item = 'Fan'),
	1 
);
INSERT INTO purchase (customer_id,item_id,quantity_purchased)
VALUES (
	(select customer_id from customers where first_name = 'Melanie' and last_name = 'Johnson'),
	(select item_id from items where item = 'Small Desk'),
	10 
);
INSERT INTO purchase (customer_id,item_id,quantity_purchased)
VALUES (
	(select customer_id from customers where first_name = 'Greg' and last_name = 'Jones'),
	(select item_id from items where item = 'Small Desk'),
	2 
);

-- Part II

-- Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
SELECT * FROM purchase;
-- All purchases, joining with the customers table.
SELECT * FROM purchase JOIN customers ON customers.customer_id = purchase.customer_id;
-- Purchases of the customer with the ID equal to 5.
SELECT item FROM items WHERE item_id = (
	SELECT item_id FROM purchase WHERE customer_id = 5
);
-- Purchases for a large desk AND a small desk
SELECT * FROM purchase 
WHERE item_id = (select item_id from items where item ='Large Desk')
OR item_id = (select item_id from items where item ='Small Desk');

-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name
SELECT cu.first_name,cu.last_name,it.item FROM customers AS cu,items AS it
WHERE cu.customer_id IN (select customer_id from purchase)
AND it.item_id IN (select item_id from purchase)
-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
INSERT INTO purchase (customer_id,quantity_purchased)
VALUES (
	(select customer_id from customers where first_name = 'Scott' and last_name = 'Scott'),
	5 
); 