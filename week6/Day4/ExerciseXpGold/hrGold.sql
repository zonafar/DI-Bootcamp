
-- Update Statement
-- Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
-- email column should be: ‘not available’
-- commission_pct column should be: 0.10
UPDATE employees 
SET email = 'not available'
WHERE department_id = 10;
-- Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
UPDATE employees
SET email = 'available'
WHERE department_id = (select department_id from departments where department_name LIKE '%Accounting%');
-- Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
select * from employees where employee_id = 105;
UPDATE employees
SET salary = 8000
WHERE salary < 5000 AND employee_id = 105;

-- Aggregate Functions
-- Write a query to find the number of jobs available in the employees table.
SELECT count(e.employee_id) FROM employees as e
JOIN jobs as j ON j.job_id = e.job_id;
-- Write a query to get the number of employees working in each post.
SELECT j.job_title,count(e.employee_id) FROM employees as e
JOIN jobs as j ON j.job_id = e.job_id
GROUP BY j.job_title;
-- Write a query to get the difference between the highest and lowest salaries.
SELECT (max(salary) - min(salary)) FROM employees;
-- Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
SELECT m.employee_id,m.first_name,m.last_name,e.first_name,e.last_name,e.salary FROM employees as m
JOIN employees as e ON m.employee_id = e.manager_id
WHERE e.salary = (select min(salary) from employees);
-- Write a query to get the average salary for each post excluding programmer.
SELECT j.job_title,AVG(e.salary) FROM employees as e
JOIN jobs as j ON j.job_id = e.job_id
WHERE j.job_title NOT IN (select job_title from jobs where job_title ILIKE'Programmer')
GROUP BY j.job_title;
-- Write a query to get the average salary for all departments that employ more than 4 employees.
-- 
create or replace function get_dept_count(dept_id INTEGER)
returns INTEGER
language plpgsql
as
$$
declare
   counter integer;
begin
   counter := (select count(*) 
   from employees
   where department_id = dept_id);  
	if counter > 4 then
   		return dept_id;
	else
		return NULL;
	END if;
end;
$$;
-- 
SELECT d.department_name,AVG(e.salary) FROM employees as e
JOIN departments as d ON d.department_id = e.department_id
WHERE get_dept_count(e.department_id) = d.department_id 
GROUP BY d.department_name;

-- Alter Table Statement
-- Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
ALTER TABLE locations 
RENAME state_province TO state;
select  *from locations;
-- Write a SQL statement to add a primary key to the “location_id” column in the locations table.
ALTER TABLE locations
ADD CONSTRAINT pk_loc PRIMARY KEY(location_id);

-- Create Tables
-- Some Review:

-- ON UPDATE CASCADE action allows you to perform the cross-table update
-- ON DELETE RESTRICT action rejects the deletion.
-- ON DELETE CASCADE action allows to delete records in the employees(child) table that refers to a record in the jobs(parent) table when the record in the parent table is deleted
-- ON DELETE SET NULL action will set the foreign key column values in the child table(employees) to NULL when the record in the parent table(jobs) is deleted, with a condition that the foreign key column in the child table must accept NULL values.
-- ON UPDATE SET NULL action resets the values in the rows in the child table(employees) to NULL values when the rows in the parent table(jobs) are updated.
-- The default action is ON DELETE RESTRICT.
-- ON DELETE NO ACTION and the ON UPDATE NO ACTION actions will reject the deletion and any updates.


-- You have to decide which constraint should be used in every question below:



-- Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
	-- make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
	-- make sure that no countries except Italy, India and China will be entered in the table.
DROP TABLE IF EXISTS new_countries;
CREATE TABLE new_countries(
	country_id SERIAL NOT NULL PRIMARY KEY,
	country_name VARCHAR(100) CHECK (country_name SIMILAR TO '%(Italy|India|China)%')
);

-- Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.
SELECT * INTO duplicated_new_countries
FROM new_countries;
-- Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
	-- make sure that the max_salary column won’t exceed 25000.
	-- make sure that job_title, min_salary and max_salary have the following default values:
	-- job_title is blank
	-- min_salary is 8000
	-- max_salary is NULL.
CREATE TABLE new_jobs(
	job_id SERIAL NOT NULL PRIMARY KEY,
	job_title VARCHAR(100) DEFAULT '',
	min_salary INTEGER DEFAULT (8000),
	max_salary INTEGER DEFAULT NULL CHECK (max_salary < 25000)
);

-- Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.
	-- make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
	-- make sure that the foreign key column job_id, references the column job_id in the “new_jobs” table.
CREATE TABLE new_employees(
	employee_id SERIAL NOT NULL PRIMARY KEY ,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	email VARCHAR(90),
	phone_number  VARCHAR(90) ,
	hire_date DATE,
	job_id INTEGER,
	salary INTEGER,
	CONSTRAINT fk_job 
	FOREIGN KEY (job_id)
	REFERENCES new_jobs(job_id)
);

-- Write a SQL statement to create a table called “new_job_history” the table should include the following columns: employee_id, start_date, end_date, job_id
	-- make sure that the foreign key employee_id references the column employee_id in the “new_employees” table.
	-- make sure that the foreign key job_id is equal to an id that exists in the “new_jobs” table.
CREATE TABLE new_job_history(
	employee_id SERIAL NOT NULL PRIMARY KEY ,
	start_date DATE,
	end_date DATE,
	job_id INTEGER,
	CONSTRAINT fk_emp 
	FOREIGN KEY (employee_id)
	REFERENCES new_employees(employee_id),
	CONSTRAINT fk_job 
	FOREIGN KEY (job_id)
	REFERENCES new_jobs(job_id)
);


-- Insert
-- Write a SQL statement to insert a record with your own value into the “new_countries” table.
-- Using only one insert statement insert 3 row of data to the “new_countries” table
INSERT INTO new_countries(country_name)
values  ('Italy'),
		('India'),
		('China');

-- Write a SQL statement to insert the rows whithin the “new_countries” table to a duplicate table.
SELECT country_name
INTO duplicated_new_countries2
FROM new_countries
WHERE country_name IN (select country_name from new_countries);
-- Write a SQL statement to insert data into the “new_employees” table, the job_id column must contain values which exist in the “new_jobs” table.




