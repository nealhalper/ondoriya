SELECT r.full_name, COUNT(DISTINCT p.person_id) AS people_per_region
FROM {{ ref('regions_silver') }} r
JOIN {{ ref('people_silver') }} p ON r.region_id = p.current_region_id
GROUP BY r.region_id, r.full_name
ORDER BY people_per_region DESC
LIMIT 10