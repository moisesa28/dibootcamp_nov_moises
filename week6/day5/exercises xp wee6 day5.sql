-- Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre,
--Display the genre name, movie title, and their rank based on popularity.

SELECT m.title, m.popularity, g.genre_name,
RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popular_movies_by_genre
FROM movies.movie m
JOIN movies.movie_genres mg ON m.movie_id = mg.movie_id
JOIN movies.genre g ON mg.genre_id = g.genre_id;


--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
--Use the NTILE() function to divide the movies 
-- produced by each production company into quartiles based on revenue.
-- Display the company name, movie title, revenue, and quartile.

SELECT pc.company_name, m.title, m.revenue,
ntile(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS top_movies_revenue
FROM movies.movie m
JOIN movies.movie_company mc ON m.movie_id = mc.movie_id
JOIN movies.production_company pc ON mc.company_id = pc.company_id
WHERE m.revenue IS NOT NULL;


-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Use the SUM() function with the ROWS frame specification to calculate
-- the running total of movie budgets within each genre.
-- Display the genre name, movie title, budget, and running total budget.
select
	g.genre_name,
	m.title as movie_title,
	m.budget,
	sum(m.budget) over (
		partition by
			g.genre_name
		order by
			m.budget rows between unbounded preceding
			and current row
	) as running_total_budget
from
	movies.movie m
	join movies.movie_genres mg on m.movie_id = mg.movie_id
	join movies.genre g on mg.genre_id = g.genre_id
where
	m.budget is not null
	AND m.budget != 0
order by
	g.genre_name,
	m.budget;

-- Task 4: Identify the Most Recent Movie for Each Genre
-- Use the FIRST_VALUE() function to find the most recent movie 
-- within each genre based on the release date. Display the genre
-- name, movie title, and release date.

SELECT DISTINCT
    g.genre_name,
    FIRST_VALUE(m.title) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC
    ) AS most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (
        PARTITION BY g.genre_name
        ORDER BY m.release_date DESC
    ) AS release_date
FROM movies.movie m
JOIN movies.movie_genres mg
    ON m.movie_id = mg.movie_id
JOIN movies.genre g
    ON mg.genre_id = g.genre_id
WHERE m.release_date IS NOT NULL
ORDER BY g.genre_name;


-- Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number 
-- of movies they have appeared in. Display the actor’s 
-- name and their rank.

SELECT
    actor_name,
    DENSE_RANK() OVER (ORDER BY movie_count DESC) AS actor_rank
FROM (
    SELECT
        p.person_name AS actor_name,
        COUNT(mc.movie_id) AS movie_count
    FROM person p
    JOIN movie_cast mc
        ON p.person_id = mc.person_id
    GROUP BY p.person_name
) AS actor_counts
ORDER BY actor_rank, actor_name;


--Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the
-- highest average movie rating. Display the director’s name and 
-- their average rating.

WITH director_avg_ratings AS (
    SELECT
        p.person_name AS director_name,
        AVG(m.vote_average) AS avg_rating
    FROM movies.movie m
    JOIN movies.movie_crew mc
        ON m.movie_id = mc.movie_id
    JOIN movies.person p
        ON mc.person_id = p.person_id
    WHERE mc.job = 'Director'
      AND m.vote_average IS NOT NULL
    GROUP BY p.person_name
),
ranked_directors AS (
    SELECT
        director_name,
        avg_rating,
        RANK() OVER (ORDER BY avg_rating DESC) AS director_rank
    FROM director_avg_ratings
)
SELECT
    director_name,
    avg_rating
FROM ranked_directors
WHERE director_rank = 1;


--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies
--acted by each actor. Display the actor’s name and the cumulative revenue.

SELECT
    p.person_name AS actor_name,
    m.title AS movie_title,
    m.release_date,
    m.revenue,
    SUM(m.revenue) OVER (
        PARTITION BY p.person_id
        ORDER BY m.release_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM movies.person p
JOIN movies.movie_cast mc
    ON p.person_id = mc.person_id
JOIN movies.movie m
    ON mc.movie_id = m.movie_id
WHERE m.revenue IS NOT NULL
ORDER BY actor_name, m.release_date;


--Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have
--the highest total budget. Display the director’s name and the total budget.

WITH director_budgets AS (
    SELECT
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM movies.movie m
    JOIN movies.movie_crew mc
        ON m.movie_id = mc.movie_id
    JOIN movies.person p
        ON mc.person_id = p.person_id
    WHERE mc.job = 'Director'
      AND m.budget IS NOT NULL
    GROUP BY p.person_name
),
ranked_directors AS (
    SELECT
        director_name,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) AS budget_rank
    FROM director_budgets
)
SELECT
    director_name,
    total_budget
FROM ranked_directors
WHERE budget_rank = 1;

