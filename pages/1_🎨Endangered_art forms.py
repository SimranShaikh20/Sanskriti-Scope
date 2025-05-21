import streamlit as st
from snowflake.snowpark import Session
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

# --- Page Configuration ---
st.set_page_config(page_title="Endangered Art Forms Explorer", layout="wide")

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

# --- Create Snowflake Session ---
session = create_session()

# --- Load Data from Snowflake ---
try:
    # Optional: View tables in schema to confirm availability
    st.write("📦 Available tables in schema:")
    tables_df = session.sql("SHOW TABLES IN SCHEMA CULTURAL_DB.CULTURAL_SCHEMA").to_pandas()
    st.dataframe(tables_df)

    # Fetch data using fully qualified table name
    query = "SELECT * FROM CULTURAL_DB.CULTURAL_SCHEMA.HERITAGE_DATA"
    df = session.sql(query).to_pandas()
    st.success("✅ Data fetched successfully from HERITAGE_DATA!")

except Exception as e:
    st.error("❌ Failed to load data from Snowflake.")
    st.exception(e)
    st.stop()

# Normalize region if needed
df["REGION_CLEAN"] = df["REGION"].str.lower()

# --- UI ---
st.markdown("## 🎨 Endangered Art Forms Explorer")
st.markdown("---")

# --- Dropdown for Art Form Selection ---
artform_list = sorted(df["ARTFORM"].dropna().unique())
selected_artform = st.selectbox("🎭 Select an Art Form", ["--Select--"] + artform_list)

# --- Filtering based on dropdown only ---
if selected_artform == "--Select--":
    filtered_df = df.copy()
else:
    filtered_df = df[df["ARTFORM"] == selected_artform]

# --- Display Filtered Table ---
st.subheader("📑 Filtered Art Forms")
if not filtered_df.empty:
    display_df = filtered_df.drop(columns=["REGION_CLEAN"])
    st.dataframe(display_df, use_container_width=True, hide_index=True)
else:
    st.warning("No art forms found matching your selection.")

# --- Map Plotting with Marker Clustering ---
st.subheader("📍 Art Form Locations")
map_center = [20.59, 78.96]
m = folium.Map(location=map_center, zoom_start=5)
marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered_df.iterrows():
    try:
        lat = float(row["LATITUDE"])
        lon = float(row["LONGITUDE"])
        popup_html = f"""
        <b>{row['ARTFORM']}</b><br>
        Region: {row['REGION']}<br>
        Endangered: {row['ENDANGERED']}<br>
        Description: {row.get('DESCRIPTION', 'No description')}
        """
        folium.Marker(
            location=[lat, lon],
            popup=popup_html,
            icon=folium.Icon(color="red" if str(row["ENDANGERED"]).lower() == "yes" else "blue")
        ).add_to(marker_cluster)
    except Exception:
        continue

# --- Display Map ---
st_folium(m, use_container_width=True)
