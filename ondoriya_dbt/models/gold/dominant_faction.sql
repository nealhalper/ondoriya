SELECT faction FROM {{ ref('faction_distribution_silver') }}
WHERE faction NOT LIKE 'Factionless'
ORDER BY percent DESC
LIMIT 1