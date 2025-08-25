select 
{{ clean_columns(source('bronze', 'people')) }}
from {{ source('bronze', 'people') }}
