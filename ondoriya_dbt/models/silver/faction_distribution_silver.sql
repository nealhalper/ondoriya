select 
{{ clean_columns(source('bronze', 'faction_distribution')) }}
from {{ source('bronze', 'faction_distribution') }}
