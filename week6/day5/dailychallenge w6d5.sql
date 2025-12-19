-- Daily Challenge : Advanced Movie Data Analysis

-- Task 1: Calculate the Average Budget Growth 
-- Rate for Each Production Company:
-- Calculate the average budget growth rate for each production
-- company across all movies they have produced.
-- Use window functions to determine the budget growth rate and then
-- calculate the average growth rate.
WITH budget_growth AS (
    SELECT
        pc.company_name,
        m.movie_id,
        m.release_date,
        m.budget,
        LAG(m.budget) OVER (
            PARTITION BY pc.company_id
            ORDER BY m.release_date
        ) AS prev_budget
    FROM movies.movie m
    JOIN movies.movie_company mc
        ON m.movie_id = mc.movie_id
    JOIN movies.production_company pc
        ON mc.company_id = pc.company_id
    WHERE m.budget IS NOT NULL
),
growth_rates AS (
    SELECT
        company_name,
        (budget - prev_budget) * 1.0 / prev_budget AS growth_rate
    FROM budget_growth
    WHERE prev_budget IS NOT NULL
	AND prev_budget <> 0
)
SELECT
    company_name,
    AVG(growth_rate) AS avg_budget_growth_rate
FROM growth_rates
GROUP BY company_name
ORDER BY avg_budget_growth_rate DESC;

-- Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that
-- are rated above the average rating of all movies.
-- Use window functions and CTEs to calculate the
-- average rating and filter the actors based on this criterion.
WITH avg_movie_rating AS (
    SELECT
        AVG(vote_average) AS avg_rating
    FROM movies.movie
    WHERE vote_average IS NOT NULL
),
above_avg_movies AS (
    SELECT
        m.movie_id
    FROM movies.movie m
    CROSS JOIN avg_movie_rating a
    WHERE m.vote_average > a.avg_rating
),
actor_movie_counts AS (
    SELECT
        p.person_name AS actor_name,
        COUNT(mc.movie_id) AS movie_count
    FROM above_avg_movies aam
    JOIN movies.movie_cast mc
        ON aam.movie_id = mc.movie_id
    JOIN movies.person p
        ON mc.person_id = p.person_id
    GROUP BY p.person_name
),
ranked_actors AS (
    SELECT
        actor_name,
        movie_count,
        RANK() OVER (ORDER BY movie_count DESC) AS actor_rank
    FROM actor_movie_counts
)
SELECT
    actor_name,
    movie_count
FROM ranked_actors
WHERE actor_rank = 1;

-- Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre,
-- considering only the last three movies released in the genre.
-- Use window functions with the ROWS frame specification to achieve this.
SELECT
    g.genre_name,
    m.title AS movie_title,
    m.release_date,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_id
        ORDER BY m.release_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue_last_3
FROM movies.movie m
JOIN movies.movie_genres mg
    ON m.movie_id = mg.movie_id
JOIN movies.genre g
    ON mg.genre_id = g.genre_id
WHERE m.revenue IS NOT NULL
ORDER BY g.genre_name, m.release_date;

-- Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the 
-- highest total revenue. Use window functions and CTEs to group 
-- movies by their series and calculate the total revenue.
WITH series_revenue AS (
    SELECT
        k.keyword_name AS series_name,
        m.movie_id,
        m.revenue
    FROM movies.movie m
    JOIN movies.movie_keywords mk
        ON m.movie_id = mk.movie_id
    JOIN movies.keyword k
        ON mk.keyword_id = k.keyword_id
    WHERE m.revenue IS NOT NULL
),
series_totals AS (
    SELECT
        series_name,
        SUM(revenue) AS total_revenue
    FROM series_revenue
    GROUP BY series_name
),
ranked_series AS (
    SELECT
        series_name,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS series_rank
    FROM series_totals
)
SELECT
    series_name,
    total_revenue
FROM ranked_series
WHERE series_rank = 1;


