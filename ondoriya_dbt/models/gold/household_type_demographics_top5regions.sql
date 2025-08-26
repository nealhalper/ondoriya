WITH top_regions AS (
    SELECT r.region_id, r.full_name
    FROM {{ ref('regions_silver') }} r
    JOIN {{ ref('people_silver') }} p ON r.region_id = p.current_region_id
    GROUP BY r.region_id, r.full_name
    ORDER BY COUNT(DISTINCT p.person_id) DESC
    LIMIT 5
)
SELECT
    tr.full_name AS region,
    hs.household_type,
    COUNT(*) AS household_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY tr.full_name), 2) AS percent_of_households
FROM top_regions tr
JOIN {{ ref('households_silver') }} hs ON tr.region_id = hs.region_id
GROUP BY tr.full_name, hs.household_type
ORDER BY tr.full_name, percent_of_households DESC