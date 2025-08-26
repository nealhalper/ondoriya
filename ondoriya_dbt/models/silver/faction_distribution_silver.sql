select
    faction,
    CAST(REPLACE(percent, '%', '') AS DOUBLE) AS percent
from (
    select
        {{ clean_columns(source('bronze', 'faction_distribution')) }}
    from {{ source('bronze', 'faction_distribution') }}
)
