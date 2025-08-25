select 
{{ clean_columns(source('bronze', 'households')) }}
from {{ source('bronze', 'households') }}
