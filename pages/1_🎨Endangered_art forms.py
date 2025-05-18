import streamlit as st
from snowflake.snowpark import Session
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- Page Configuration ---
st.set_page_config(page_title="Endangered Art Forms Explorer", layout="wide")

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

# --- Create Snowflake Session ---
session = create_session()

# --- Load Data from Snowflake ---
df = session.table("HERITAGE_DATA").to_pandas()

# Normalize region for filtering
df["REGION_CLEAN"] = df["REGION"].str.lower()

# --- UI ---
st.markdown("## 🎨 Endangered Art Forms Explorer")
st.markdown("---")

# --- State Multi-Select ---
unique_states = sorted(df["REGION"].dropna().unique())
states = st.multiselect(
    "Select State(s)",
    options=unique_states,
    default=unique_states,
    placeholder="Choose one or more states to filter by"
)

# --- Filter Data ---
selected_states_lower = [s.lower() for s in states]
filtered_df = df[df["REGION_CLEAN"].apply(lambda x: any(state in x for state in selected_states_lower))]
filtered_df = df[df["REGION_CLEAN"].isin(selected_states_lower)]


# --- Display Filtered Table ---
st.subheader("📑 Filtered Art Forms")
if not filtered_df.empty:
    display_df = filtered_df.drop(columns=["REGION_CLEAN"])
    st.dataframe(display_df, use_container_width=True, hide_index=True)
else:
    st.warning("No art forms found for the selected state(s).")

# --- Map Plotting ---
st.subheader("📍 Art Form Locations")
map_center = [20.59, 78.96]
m = folium.Map(location=map_center, zoom_start=5)

for _, row in filtered_df.iterrows():
    try:
        lat = float(row["LATITUDE"])
        lon = float(row["LONGITUDE"])
        folium.Marker(
            location=[lat, lon],
            popup=f'{row["ARTFORM"]} ({row["REGION"]})',
            icon=folium.Icon(color="red" if row["ENDANGERED"] == "Yes" else "blue")
        ).add_to(m)
    except:
        continue

st_folium(m, use_container_width=True)
