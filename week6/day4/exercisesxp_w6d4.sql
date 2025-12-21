-- Exercise XP: Advanced Olympic Data Analysis

--Exercise 1: Complex Subquery Analysis

--Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. 
--Use a correlated subquery to achieve this.

SELECT * FROM medal;

SELECT * FROM competitor_event;


SELECT
    m.medal_name,
    AVG(gc.age) AS average_age
FROM games_competitor gc
JOIN competitor_event ce
    ON gc.id = ce.competitor_id
JOIN medal m
    ON ce.medal_id = m.id
WHERE m.medal_name <> 'NA'
  AND EXISTS (
      SELECT 1
      FROM competitor_event ce2
      WHERE ce2.competitor_id = gc.id
        AND ce2.medal_id = ce.medal_id)
GROUP BY m.medal_name;


--Task 2: Identify the top 5 regions with the highest number of unique 
--competitors who have participated in more than 3 different events. 
--Use nested subqueries to filter and aggregate the data.

SELECT
    nr.region_name,
    COUNT(DISTINCT gc.id) AS unique_competitors
FROM noc_region nr
JOIN games_competitor gc
    ON nr.id = gc.id
WHERE gc.id IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    WHERE ce.competitor_id IN (
        SELECT ce2.competitor_id
        FROM competitor_event ce2
        GROUP BY ce2.competitor_id
        HAVING COUNT(DISTINCT ce2.event_id) > 3
    )
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;


--Task 3: Create a temporary table to store the total number of medals won by each
--competitor and filter to show only those who have won more than 2 medals. 
--Use subqueries to aggregate the data.

CREATE TEMP TABLE temp_competitor_medal_totals (
    competitor_id INT,
    total_medals INT
);


INSERT INTO temp_competitor_medal_totals (competitor_id, total_medals)
SELECT
    gc.id AS competitor_id,
    (
        SELECT COUNT(*)
        FROM competitor_event ce
        WHERE ce.competitor_id = gc.id
          AND ce.medal_id <> 4
    ) AS total_medals
FROM games_competitor gc
WHERE gc.id IN (
    SELECT ce2.competitor_id
    FROM competitor_event ce2
    WHERE ce2.medal_id <> 4
    GROUP BY ce2.competitor_id
    HAVING COUNT(*) > 2
);  

SELECT * FROM temp_competitor_medal_totals;

--Task 4: Use a subquery within a DELETE statement to remove records of competitors
--who have not won any medals from a temporary table created for analysis.

DELETE FROM temp_competitor_medal_totals
WHERE competitor_id IN (
    SELECT gc.id
    FROM games_competitor gc
    WHERE gc.id NOT IN (
        SELECT ce.competitor_id
        FROM competitor_event ce
        WHERE ce.medal_id <> 4
    )
);
SELECT * FROM temp_competitor_medal_totals;


-- Exercise 2: Advanced Data Manipulation and Optimization

-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. 
-- Use a correlated subquery within the UPDATE statement.

UPDATE olympics.person p
SET height = (
    SELECT AVG(p2.height)
    FROM olympics.person p2
    JOIN olympics.person_region pr2
        ON p2.id = pr2.person_id
    WHERE pr2.region_id = (
        SELECT pr.region_id
        FROM olympics.person_region pr
        WHERE pr.person_id = p.id
        LIMIT 1
    )
    AND p2.height IS NOT NULL
)
WHERE p.height IS NULL;


--Task 2: Insert new records into a temporary table for competitors who participated
--in more than one event in the same games and list their total number of events
--participated. Use nested subqueries for filtering.

CREATE TEMP TABLE temp_multi_event_competitors (
    competitor_id INT,
    games_id INT,
    total_events INT
);

INSERT INTO temp_multi_event_competitors (competitor_id, games_id, total_events)
SELECT
    gc.id AS competitor_id,
    gc.games_id,
    (
        SELECT COUNT(*)
        FROM competitor_event ce
        WHERE ce.competitor_id = gc.id
    ) AS total_events
FROM games_competitor gc
WHERE gc.id IN (
    SELECT ce1.competitor_id
    FROM competitor_event ce1
    WHERE ce1.competitor_id IN (
        SELECT ce2.competitor_id
        FROM competitor_event ce2
        GROUP BY ce2.competitor_id
        HAVING COUNT(ce2.event_id) > 1
    )
);

SELECT * FROM temp_multi_event_competitors


--Task 3: Identify regions where the average number of medals won per competitor
--is greater than the overall average. Use subqueries to calculate and compare averages.

SELECT
    nr.region_name,
    AVG(region_competitor_medals.medal_count) AS avg_medals_per_competitor
FROM olympics.noc_region nr
JOIN (
    -- medals per competitor per region
    SELECT
        pr.region_id,
        gc.id AS competitor_id,
        COUNT(ce.medal_id) AS medal_count
    FROM olympics.games_competitor gc
    JOIN olympics.person_region pr
        ON gc.person_id = pr.person_id
    JOIN olympics.competitor_event ce
        ON gc.id = ce.competitor_id
    WHERE ce.medal_id <> 4
    GROUP BY pr.region_id, gc.id
) AS region_competitor_medals
    ON nr.id = region_competitor_medals.region_id
GROUP BY nr.region_name
HAVING AVG(region_competitor_medals.medal_count) >
(
    -- overall average medals per competitor
    SELECT AVG(medal_count)
    FROM (
        SELECT
            gc.id AS competitor_id,
            COUNT(ce.medal_id) AS medal_count
        FROM olympics.games_competitor gc
        JOIN olympics.competitor_event ce
            ON gc.id = ce.competitor_id
        WHERE ce.medal_id <> 4
        GROUP BY gc.id
    ) AS overall_competitor_medals
)
ORDER BY avg_medals_per_competitor DESC;

-- Task 4: Create a temporary table to track competitors’ participation across
--  different seasons and identify those who have participated in both Summer and Winter games.

CREATE TEMP TABLE temp_competitor_seasons (
    person_id INT,
    season TEXT
);

INSERT INTO temp_competitor_seasons (person_id, season)
SELECT DISTINCT
    gc.person_id,
    g.season
FROM games_competitor gc
JOIN games g
    ON gc.games_id = g.id;
    
SELECT
    person_id
FROM temp_competitor_seasons
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2;