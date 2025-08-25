select 
{{ clean_columns(source('bronze', 'moons')) }}
from {{ source('bronze', 'moons') }}
