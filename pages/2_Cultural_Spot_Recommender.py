import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from recommender import get_route_recommendations

# Load data
df = pd.read_csv("data/heritage_data.csv")

st.title("🛤️ Cultural spots Recommender")

start_district = st.selectbox("Choose your starting Place", df["Region"].unique())
recommended = get_route_recommendations(df, start_district)

if recommended.empty:
    st.warning("No recommendations available. Try another starting point.")
else:
    st.subheader("📍 Suggested Places")

    # Show table
    st.dataframe(recommended[["Art form", "Region", "Endangered", "UNESCO Listed", "distance_km"]],hide_index=True)

    # Draw on map
    m = folium.Map(location=[recommended["latitude"].mean(), recommended["longitude"].mean()], zoom_start=6)

    start_row = df[df["Region"] == start_district].iloc[0]
    folium.Marker(
        location=[start_row["latitude"], start_row["longitude"]],
        popup=f"Start: {start_row['Art form']} ({start_row['Region']})",
        icon=folium.Icon(color="green")
    ).add_to(m)

    for _, row in recommended.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['Art form']} ({row['Region']})",
            icon=folium.Icon(color="red")
        ).add_to(m)

    st_folium(m, width=700)
