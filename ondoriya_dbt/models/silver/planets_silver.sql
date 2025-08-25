select 
{{ clean_columns(source('bronze', 'planets')) }}
from {{ source('bronze', 'planets') }}
