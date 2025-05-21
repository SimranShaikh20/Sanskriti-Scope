import streamlit as st
from snowflake.snowpark import Session
import pandas as pd
import folium
from streamlit_folium import st_folium
from recommender import get_route_recommendations

# --- Snowflake Connection Parameters ---
connection_parameters = {
     "user": "your user name",
    "password": "your password",
    "account": "your account name",
    "warehouse": "your warehouse name",
    "database": "your database name",
    "schema": "your schema name",
    "role": "your role name"
}

@st.cache_resource
def create_session():
    return Session.builder.configs(connection_parameters).create()

session = create_session()

# --- Load Data from Snowflake ---
try:
    # List all available tables for debugging
    tables_df = session.sql("SHOW TABLES IN SCHEMA CULTURAL_DB.CULTURAL_SCHEMA").to_pandas()
    st.write("📋 Available Tables:")
    st.dataframe(tables_df)

    # Read from fully qualified table name
    df = session.table("CULTURAL_DB.CULTURAL_SCHEMA.HERITAGE_DATA").to_pandas()
    st.success("✅ Data loaded from HERITAGE_DATA.")

except Exception as e:
    st.error("❌ Failed to load data from Snowflake.")
    st.exception(e)
    st.stop()

# --- App UI ---
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

    # Display filtered table
    st.dataframe(
        recommended[["ARTFORM", "REGION", "ENDANGERED", "UNESCOLISTED", "DISTANCE_KM"]],
        hide_index=True
    )

    # Display map with markers
    m = folium.Map(location=[recommended["LATITUDE"].mean(), recommended["LONGITUDE"].mean()], zoom_start=6)

    # Start location marker
    start_row = df[df["REGION"] == start_district].iloc[0]
    folium.Marker(
        location=[start_row["LATITUDE"], start_row["LONGITUDE"]],
        popup=f"Start: {start_row['ARTFORM']} ({start_row['REGION']})",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Recommended locations
    for _, row in recommended.iterrows():
        folium.Marker(
            location=[row["LATITUDE"], row["LONGITUDE"]],
            popup=f"{row['ARTFORM']} ({row['REGION']})",
            icon=folium.Icon(color="red")
        ).add_to(m)

    st_folium(m, width=700)

    # Explanation section
    st.markdown(
        """
        ### 📌 Why these recommendations?
        These spots are selected based on their cultural significance and proximity to your starting point. 
        By visiting these places, you contribute to the preservation of endangered art forms.
        """
    )
