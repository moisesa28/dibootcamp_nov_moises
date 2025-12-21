-- Daily Challenge: Cleaning and Transforming Employee Record Data with SQL

-- Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Insert 20 sample records 
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

SELECT * FROM employees;

--Identify and handle any missing value.
SELECT *
	FROM employees
	WHERE employee_id IS NULL
	OR employee_name IS NULL
	OR salary IS NULL
	OR hire_date IS NULL
	OR department IS NULL; -- only one null in dataset, in department where employee_id = 13

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;

--making names consistant
UPDATE employees
SET employee_name = INITCAP(employee_name);

-- making the hire_date a date
ALTER TABLE employees
ALTER COLUMN hire_date TYPE DATE
USING hire_date::DATE;

--checking for duplicates
SELECT
    employee_name,
    salary,
    hire_date,
    department,
    COUNT(*) AS duplicate_count
FROM employees
GROUP BY
    employee_name,
    salary,
    hire_date,
    department
HAVING COUNT(*) > 1; -- there is none
 
 --check for duplicates in row
SELECT
    employee_name,
    hire_date,
    department,
    COUNT(*) AS duplicate_count
FROM employees
GROUP BY employee_name, hire_date, department
HAVING COUNT(*) > 1; --there is NONE

--checking for outliers in salary:
SELECT
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    AVG(salary) AS avg_salary,
    STDDEV(salary) AS stddev_salary
FROM employees; --no big outliers in salary.

-- The data has been cleaned and ordered. Each column has the 
-- correct data type, there are no duplicates, formatting has been done, "any"
-- and there are no outliers in the salary.
SELECT * FROM employees ORDER BY department;






