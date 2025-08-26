import duckdb
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Ondoriya Data Visualization')

con = duckdb.connect('D:/data/ondoriya/bronze.duckdb')

result = con.execute("SELECT total_population FROM main_gold.total_population").fetchone()
total_population = result[0] if result else 0
st.subheader("Ondoriya KPIs")
st.metric(label="Total Population", value=f"{total_population:,}")

result = con.execute("SELECT faction FROM main_gold.dominant_faction").fetchone()
dominant_faction = result[0] if result else "N/A"
st.metric(label="Dominant Faction", value=dominant_faction)

df = con.execute("SELECT * FROM main_gold.faction_distribution").fetchdf()
st.subheader('Faction Distribution in Ondoriya')
colors = plt.cm.tab20.colors
bar_colors = [colors[i % len(colors)] for i in range(len(df))]
plt.figure(figsize=(8, 5))
plt.bar(df['faction'], df['percent'], color=bar_colors)
plt.xlabel('Faction')
plt.ylabel('Percent')
plt.title('Faction Distribution in Ondoriya')
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()
st.pyplot(plt)

df = con.execute("SELECT * FROM main_gold.top_5_most_populous_regions").fetchdf()
st.subheader("Top 5 Most Populous Regions")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Population and Average Age (Dual Axis)")
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
ax1.bar(df['full_name'], df['region_population'], color='skyblue', label='Population')
ax2.plot(df['full_name'], df['average_age'], color='orange', marker='o', label='Average Age')
ax1.set_xlabel('Region')
ax1.set_ylabel('Population', color='skyblue')
ax2.set_ylabel('Average Age', color='orange')
ax2.set_ylim(100, 125)
plt.title('Population and Average Age by Region')
plt.xticks(rotation=45)
fig.tight_layout()
st.pyplot(fig)

df = con.execute("SELECT * FROM main_gold.household_type_demographics_top5regions").fetchdf()
st.header("Household Type Breakdown in Top 5 Regions")

regions = df['region'].unique()
for region in regions:
    region_df = df[df['region'] == region][['household_type', 'household_count', 'percent_of_households']]
    st.subheader(f"Household Types in {region}")
    st.dataframe(region_df, use_container_width=True, hide_index=True)

con.close()

