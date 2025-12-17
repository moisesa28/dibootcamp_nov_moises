--Olympic Data Exploration

--Exercise 1: Detailed Medal Analysis

--Task 1: Identify competitors who have won at least one medal in events spanning
--both Summer and Winter Olympics. Create a temporary table to store these competitors 
--and their medal counts for each season, and then display the contents of this table.

CREATE TEMP TABLE temp_dual_season_medalists (
    person_id INT,
    summer_medals INT,
    winter_medals INT
);


INSERT INTO temp_dual_season_medalists (person_id, summer_medals, winter_medals)
SELECT
    gc.person_id,

    -- Summer medal count
    (
        SELECT COUNT(*)
        FROM games_competitor gc_s
        JOIN games g_s
            ON gc_s.games_id = g_s.id
        JOIN competitor_event ce_s
            ON gc_s.id = ce_s.competitor_id
        WHERE gc_s.person_id = gc.person_id
          AND g_s.season = 'Summer'
          AND ce_s.medal_id <> 4
    ) AS summer_medals,

    -- Winter medal count
    (
        SELECT COUNT(*)
        FROM games_competitor gc_w
        JOIN games g_w
            ON gc_w.games_id = g_w.id
        JOIN competitor_event ce_w
            ON gc_w.id = ce_w.competitor_id
        WHERE gc_w.person_id = gc.person_id
          AND g_w.season = 'Winter'
          AND ce_w.medal_id <> 4
    ) AS winter_medals

FROM games_competitor gc
WHERE gc.person_id IN (
    -- Must have at least one Summer medal
    SELECT gc1.person_id
    FROM games_competitor gc1
    JOIN games g1 ON gc1.games_id = g1.id
    JOIN competitor_event ce1 ON gc1.id = ce1.competitor_id
    WHERE g1.season = 'Summer'
      AND ce1.medal_id <> 4
)
AND gc.person_id IN (
    -- Must have at least one Winter medal
    SELECT gc2.person_id
    FROM games_competitor gc2
    JOIN games g2 ON gc2.games_id = g2.id
    JOIN competitor_event ce2 ON gc2.id = ce2.competitor_id
    WHERE g2.season = 'Winter'
      AND ce2.medal_id <> 4
)
GROUP BY gc.person_id;

SELECT * FROM temp_dual_season_medalists

--Task 2: Create a temporary table to store competitors who have won medals in exactly 
--two different sports, and then use a subquery to identify the top 3 competitors 
--with the highest total number of medals across all sports. Display the contents of this table.

CREATE TEMP TABLE temp_two_sport_medalists (
    person_id INT,
    total_medals INT
);

INSERT INTO temp_two_sport_medalists (person_id, total_medals)
SELECT
    gc.person_id,
    (
        -- total medals across all sports
        SELECT COUNT(*)
        FROM games_competitor gc2
        JOIN competitor_event ce2
            ON gc2.id = ce2.competitor_id
        WHERE gc2.person_id = gc.person_id
          AND ce2.medal_id <> 4
    ) AS total_medals
FROM games_competitor gc
WHERE gc.person_id IN (
    -- competitors with medals in exactly two sports
    SELECT gc1.person_id
    FROM games_competitor gc1
    JOIN competitor_event ce1
        ON gc1.id = ce1.competitor_id
    JOIN event e1
        ON ce1.event_id = e1.id
    WHERE ce1.medal_id <> 4
    GROUP BY gc1.person_id
    HAVING COUNT(DISTINCT e1.sport_id) = 2
)
GROUP BY gc.person_id;

SELECT *
FROM temp_two_sport_medalists
ORDER BY total_medals DESC
LIMIT 3;

--Exercise 2: Region and Competitor Performance

--Task 1: Retrieve the regions that have competitors who have won the highest number of medals
--in a single Olympic event. Use a subquery to determine the event with the highest number of
--medals for each competitor, and then display the top 5 regions with the highest total medals.

SELECT
    ce.competitor_id,
    MAX(event_medal_count) AS max_medals_in_event
FROM (
    SELECT
        competitor_id,
        event_id,
        COUNT(*) AS event_medal_count
    FROM competitor_event
    WHERE medal_id <> 4
    GROUP BY competitor_id, event_id
) ce
GROUP BY ce.competitor_id;

SELECT --query – aggregate by region and return top 5
    nr.region_name,
    SUM(cm.max_medals_in_event) AS total_medals
FROM (
    -- highest medal count per competitor in a single event
    SELECT
        ce.competitor_id,
        MAX(event_medal_count) AS max_medals_in_event
    FROM (
        SELECT
            competitor_id,
            event_id,
            COUNT(*) AS event_medal_count
        FROM competitor_event
        WHERE medal_id <> 4
        GROUP BY competitor_id, event_id
    ) ce
    GROUP BY ce.competitor_id
) cm
JOIN games_competitor gc
    ON cm.competitor_id = gc.id
JOIN person_region pr
    ON gc.person_id = pr.person_id
JOIN noc_region nr
    ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

--Task 2: Create a temporary table to store competitors who have participated in more
--than three Olympic Games but have not won any medals. Retrieve and display the contents
--of this table, including their full names and the number of games they participated in.

CREATE TEMP TABLE temp_multi_games_no_medals (
    person_id INT,
    games_participated INT
);

INSERT INTO temp_multi_games_no_medals (person_id, games_participated)
SELECT
    gc.person_id,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM games_competitor gc
WHERE gc.person_id NOT IN (
    -- competitors who have won at least one medal
    SELECT gc2.person_id
    FROM games_competitor gc2
    JOIN competitor_event ce
        ON gc2.id = ce.competitor_id
    WHERE ce.medal_id <> 4
)
GROUP BY gc.person_id
HAVING COUNT(DISTINCT gc.games_id) > 3;

SELECT
    p.full_name,
    t.games_participated
FROM temp_multi_games_no_medals t
JOIN person p
    ON t.person_id = p.id
ORDER BY t.games_participated DESC;
