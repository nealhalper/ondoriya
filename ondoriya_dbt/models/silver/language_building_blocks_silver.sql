select 
{{ clean_columns(source('bronze', 'language_building_blocks')) }}
from {{ source('bronze', 'language_building_blocks') }}
