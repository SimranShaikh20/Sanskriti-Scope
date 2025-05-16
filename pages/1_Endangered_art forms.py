import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Load Data
df = pd.read_csv(r"data/heritage_data.csv")

st.title("🎨 Endangered Art Forms Explorer")

# Sidebar Filters
states = st.multiselect("Select State(s)", df["Region"].unique(), default=df["Region"].unique())

filtered_df = df[(df["Region"].isin(states)) & (df["Endangered"].isin(['Yes','No']))]

# Show Table
st.subheader("Filtered Art Forms")
st.dataframe(filtered_df,use_container_width=True,hide_index=True)

# Show Map
m = folium.Map(location=[20.59, 78.96], zoom_start=5)
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f'{row["Art form"]} ({row["Region"]})',
        icon=folium.Icon(color="red" if row["Endangered"] == "Yes" else "blue")
    ).add_to(m)

st.subheader("📍 Art Form Locations")
st_data = st_folium(m,use_container_width=True)
