SELECT r.full_name, AVG(p.age) AS average_age, COUNT(DISTINCT p.person_id) AS region_population
FROM {{ ref('regions_silver') }} r
JOIN {{ ref('people_silver') }} p ON r.region_id = p.current_region_id
GROUP BY r.full_name
ORDER BY region_population DESC
LIMIT 5