SELECT faction FROM {{ ref('faction_distribution_silver') }}
WHERE faction NOT LIKE 'Factionless' AND faction != 'Total'
ORDER BY percent DESC