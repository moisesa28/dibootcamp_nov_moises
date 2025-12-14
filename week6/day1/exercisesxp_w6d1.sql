--exercises xp week 6 day1

-- CREATE TABLE items (
--     id SERIAL PRIMARY KEY,
--     name TEXT NOT NULL,
--     price NUMERIC(10,2) NOT NULL
-- );


-- CREATE TABLE customers(
-- customers_id SERIAL PRIMARY KEY,
-- firs_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL
-- );

--insert the following items to each list
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

-- INSERT INTO items (name, price)
-- VALUES
--     ('Small Desk', 100),
--     ('Large Desk', 300),
--     ('Fan', 80);
	
-- SELECT * FROM items;

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

-- INSERT INTO customers (firs_name,last_name)
-- VALUES
-- ('Greg','Jones'),
-- ('Sandra','Jones'),
-- ('Scott','Scott'),
-- ('Trevor','Green'),
-- ('Melanie','Johnson')

-- SELECT * FROM customers
-- ALTER TABLE customers
-- RENAME COLUMN firs_name TO first_name;

-- Use SQL to fetch the following data from the database:

-- 1. All the items.
-- SELECT * FROM items

-- 2. All the items with a price above 80 (80 not included).
-- SELECT * FROM items WHERE price > 80

-- 3. All the items with a price below 300. (300 included)
-- SELECT * FROM items WHERE price < 300

-- 4. All customers whose last name is ‘Smith’ (What will be your outcome?).
-- SELECT * FROM customers WHERE last_name = 'Smith' 

-- 5. All customers whose last name is ‘Jones’.
-- SELECT * FROM customers WHERE last_name = 'Jones'

-- 6. All customers whose firstname is not ‘Scott’.
-- SELECT * FROM customers WHERE first_name != 'Scott'

