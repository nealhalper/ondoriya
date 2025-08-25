select 
{{ clean_columns(source('bronze', 'language_roots')) }}
from {{ source('bronze', 'language_roots') }}
