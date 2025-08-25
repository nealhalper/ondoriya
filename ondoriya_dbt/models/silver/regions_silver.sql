select 
{{ clean_columns(source('bronze', 'regions')) }}
from {{ source('bronze', 'regions') }}
