SELECT COUNT(DISTINCT person_id) AS total_population
FROM {{ ref('people_silver') }}