SELECT faction FROM {{ ref('faction_distribution_silver') }}
WHERE faction != 'Total'
ORDER BY percent DESC
LIMIT 1