{% macro clean_columns(relation) %}
    {% set columns = adapter.get_columns_in_relation(relation) %}
    {% for col in columns %}
        {{ col.name | lower | trim | replace(' ', '_') }} as {{ col.name | lower | trim | replace(' ', '_') }}{% if not loop.last %}, {% endif %}
    {% endfor %}
{% endmacro %}