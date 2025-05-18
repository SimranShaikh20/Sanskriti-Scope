import streamlit as st
from snowflake.snowpark import Session
import pandas as pd
import folium
from streamlit_folium import st_folium
from recommender import get_route_recommendations

# --- Snowflake Connection Parameters ---
connection_parameters = {
    "user": st.secrets["snowflake"]["user"],
    "password": st.secrets["snowflake"]["password"],
    "account": st.secrets["snowflake"]["account"],
    "warehouse": st.secrets["snowflake"]["warehouse"],
    "database": st.secrets["snowflake"]["database"],
    "schema": st.secrets["snowflake"]["schema"],
    "role": st.secrets["snowflake"]["role"]
}

@st.cache_resource
def create_session():
    return Session.builder.configs(connection_parameters).create()

session = create_session()

# --- Load Data from Snowflake ---
df = session.table("HERITAGE_DATA").to_pandas()

st.title("🛤️ Cultural Spots Recommender")

# --- User Input ---
start_district = st.selectbox("Choose your starting Place", df["REGION"].unique())

# --- Recommendation Logic ---
recommended = get_route_recommendations(df, start_district)

# --- Display Results ---
if recommended.empty:
    st.warning("No recommendations available. Try another starting point.")
else:
    st.subheader("📍 Suggested Places")

    # Show Table (use uppercase column names)
    st.dataframe(
        recommended[["ARTFORM", "REGION", "ENDANGERED", "UNESCOLISTED", "DISTANCE_KM"]],
        hide_index=True
    )

    # Map Display
    m = folium.Map(location=[recommended["LATITUDE"].mean(), recommended["LONGITUDE"].mean()], zoom_start=6)

    start_row = df[df["REGION"] == start_district].iloc[0]
    folium.Marker(
        location=[start_row["LATITUDE"], start_row["LONGITUDE"]],
        popup=f"Start: {start_row['ARTFORM']} ({start_row['REGION']})",
        icon=folium.Icon(color="green")
    ).add_to(m)

    for _, row in recommended.iterrows():
        folium.Marker(
            location=[row["LATITUDE"], row["LONGITUDE"]],
            popup=f"{row['ARTFORM']} ({row['REGION']})",
            icon=folium.Icon(color="red")
        ).add_to(m)

    st_folium(m, width=700)

    st.markdown(
        """
        ### 📌 Why these recommendations?
        These spots are selected based on their cultural significance and proximity to your starting point. By visiting these places, you contribute to the preservation of endangered art forms.
        """
    )
