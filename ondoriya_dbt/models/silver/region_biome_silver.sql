select 
{{ clean_columns(source('bronze', 'region_biome')) }}
from {{ source('bronze', 'region_biome') }}
