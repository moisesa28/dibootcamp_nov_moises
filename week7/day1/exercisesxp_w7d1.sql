--Exercises XP
-- Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- 1. Create a temporary table that join all tables and create a new one using LEFT JOIN.
SELECT *
	INTO emp_dataset
	FROM salaries s
	FULL JOIN companies c
	ON s.comp_name = c.company_name
	FULL JOIN functions f
	ON s.func_code = f.function_code
	FULL JOIN employees e
	ON s.employee_id = e.employee_code_emp;

SELECT * FROM emp_dataset;

-- 2. Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
-- 3. Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
-- 4. Transform this new table into a dataset “df_employee” for analysis.
SELECT CONCAT(employee_id, CAST(date AS date)) AS id,
	   CAST(date AS date) AS month_year,
       employee_id, 
       employee_name, 
	   gender, 
	   age,
       salary,
       function_group, 
       company_name, 
       company_city, 
       company_state, 
       company_type, 
       const_site_category
INTO df_employee
FROM emp_dataset

--Exercise 2: Cleaning Data for Consistency and Quality
-- 1. run the following SQLite request and observe your new table.
SELECT * FROM df_employee;

-- 2. Remove all unwanted spaces from all text columns using TRIM
UPDATE df_employee
SET		id = TRIM(id),
		employee_id	= TRIM(employee_id::text)::integer, --since the employee id is identifies as an integer, we used the previous syntax
		employee_name = TRIM(employee_name),
		gender = TRIM(gender),
		function_group = TRIM(function_group),
		company_name = TRIM(company_name),
		company_city = TRIM(company_city),
		company_state = TRIM(company_state),
		company_type = TRIM(company_type),
		const_site_category = TRIM(const_site_category)

-- 3. Check for NULL values and empty values.
SELECT *
	FROM df_employee
	WHERE id IS NULL
	OR month_year IS NULL
	OR employee_id IS NULL
	OR employee_name IS NULL
	OR gender IS NULL
	OR age IS NULL
	OR salary IS NULL
	OR function_group IS NULL
	OR company_name IS NULL
	OR company_city IS NULL
	OR company_state IS NULL
	OR company_type IS NULL
	OR const_site_category IS NULL;

SELECT *
	FROM df_employee
	WHERE id = ''
	OR employee_name = ''
	OR gender = ''
	OR salary = ''
	OR function_group = ''
	OR company_name = ''
	OR company_city = ''
	OR company_state = ''
	OR company_type = ''
	OR const_site_category = ''

-- 4. Delete rows of the detected missing values.
SELECT COUNT(*) AS gender_null_values
	FROM df_employee
	WHERE gender is null; -- there are 448 null values in gender

SELECT COUNT(gender) AS m_values
	FROM df_employee
	WHERE gender ='M';-- there are 141 rows as M

SELECT COUNT(gender) AS f_values
	FROM df_employee
	WHERE gender ='F';	-- there are 40 rows as F

SELECT COUNT(*) AS age_null_values
	FROM df_employee
	WHERE age is  null; -- there are 448 null values in age

SELECT COUNT(*) AS company_null_values
	FROM df_employee
	WHERE company_name is  null; --there are 120 null values in company_name

SELECT COUNT(*) AS month_null_values
	FROM df_employee
	WHERE month_year is  null; --129 null values

SELECT COUNT(*) AS function_group_null_values
	FROM df_employee
	WHERE function_group is  null; --92 null values

SELECT COUNT(*) AS employee_id_null_values
	FROM df_employee
	WHERE employee_id is  null; --129 null values

SELECT COUNT(*) AS employee_name_null_values
	FROM df_employee
	WHERE employee_name is  null; --129 null values

SELECT COUNT(*) AS salary_null_values
	FROM df_employee
	WHERE salary is  null; --129 null values

SELECT COUNT(*) AS company_city_null_values
	FROM df_employee
	WHERE company_city is  null;	--120 null values

SELECT COUNT(*) AS company_type_null_values
	FROM df_employee
	WHERE company_type is  null; --120 null values

SELECT COUNT(*) AS const_site_category_null_values
	FROM df_employee
	WHERE const_site_category is  null; --120null values

SELECT COUNT(const_site_category) AS count_missing_const_site_category
	FROM df_employee
	WHERE const_site_category = ''-- there are 92 blank values in const_site_category

SELECT COUNT(salary) AS count_missing_salary
	FROM df_employee
	WHERE salary = ''; -- 1 missing value

SELECT COUNT(id) AS count_missing_salary
	FROM df_employee
	WHERE id = ''; --129 missing values

DELETE FROM df_employee
WHERE const_site_category = '';

DELETE FROM df_employee
WHERE salary = '';

DELETE FROM df_employee
WHERE id = '';
----
--check duplicates and spelling
SELECT DISTINCT company_city
FROM df_employee
GROUP BY company_city
ORDER BY company_city;

UPDATE df_employee
SET company_city = 'Goiania'
WHERE company_city = 'Goianiaa';

SELECT DISTINCT company_type
FROM df_employee
GROUP BY company_type
ORDER BY company_type;

UPDATE df_employee
SET company_type = 'Construction Site'
WHERE company_type = 'Construction Sites'

SELECT DISTINCT const_site_category
FROM df_employee
GROUP BY const_site_category
ORDER BY const_site_category;

UPDATE df_employee
SET const_site_category = 'Commercial'
WHERE const_site_category = 'Commerciall';

SELECT DISTINCT id ,COUNT(id) as duplicated
FROM df_employee
GROUP BY id

ALTER TABLE df_employee
ALTER COLUMN salary TYPE INTEGER
USING REPLACE(salary, ',', '')::INTEGER;

SELECT * FROM df_employee;

-- Exercise 3 : Calculating Current Employee Counts by Company
-- How many employees do the companies have today?
SELECT COUNT (employee_id) AS total_employees
FROM df_employee; --There are 408 total employees

-- Group them by company
SELECT COUNT (employee_id) AS total_employees, company_name
FROM df_employee
GROUP BY company_name
ORDER BY total_employees DESC;


-- Exercise 4 : Analyzing Employee Distribution by City and Over Time
-- What is the total number of employees each city? Add a percentage column
SELECT
    company_city,
    COUNT(employee_id) AS employee_count,
	COUNT(employee_id) * 100 / SUM(COUNT(employee_id)) OVER () AS percentage
FROM
    df_employee
GROUP BY
    company_city
ORDER BY
    employee_count DESC;

-- What is the total number of employees each month?
SELECT
    month_year,
    COUNT(*) AS employees_by_month
FROM
    df_employee
GROUP BY
    month_year
ORDER BY
    employees_by_month DESC;

-- What is the average number of employees each month?
SELECT (COUNT(employee_id) / COUNT(DISTINCT month_year)) AS avg_employees_per_month
FROM df_employee

-- Exercise 5 : Analyzing Employment Trends and Salary Metrics
-- What is the minimum and maximum number of employees throughout all the months?
SELECT min(employee_id) AS minimum_employees, MAX(employee_id) AS maximum_employees, month_year
FROM df_employee
GROUP BY month_year --the df_employee table only shows one month.

-- What is the monthly average number of employees by function group?
SELECT AVG(employee_id), function_group
FROM df_employee
GROUP BY function_group;

-- What is the annual average salary?
SELECT AVG(salary) AS average_salary, month_year
FROM df_employee
GROUP BY month_year; --the df_employee table only shows one month.


