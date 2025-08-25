#RUN ONCE to generate silver models
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
models_silver_dir = os.path.join(script_dir, "models", "silver")

os.makedirs(models_silver_dir, exist_ok=True)

tables = [
    "faction_distribution",
    "households",
    "language_building_blocks",
    "language_roots",
    "moons",
    "people",
    "planets",
    "region_biome",
    "regions"
]

template = """select 
{{{{ clean_columns(source('bronze', '{table}')) }}}}
from {{{{ source('bronze', '{table}') }}}}
"""

for table in tables:
    with open(os.path.join(models_silver_dir, f"{table}_silver.sql"), "w") as f:
        f.write(template.format(table=table))