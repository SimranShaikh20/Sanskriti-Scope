import streamlit as st
import pandas as pd
import snowflake.connector

# Title
st.title("Incredible India - Cultural Art Forms & Responsible Tourism")

# Snowflake connection
conn = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    warehouse=st.secrets["snowflake"]["warehouse"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"],
    role=st.secrets["snowflake"]["role"]
)

# Fetch data
cur = conn.cursor()
cur.execute("SELECT * FROM ARTS")  # change table name if needed
df = cur.fetch_pandas_all()

# Filters
region_filter = st.selectbox("Select Address", ["All"] + sorted(df['ADDRESS'].unique().tolist()))
endangered_filter = st.checkbox("Show only endangered art forms")

# Apply filters
if region_filter != "All":
    df = df[df['ADDRESS'] == region_filter]
if endangered_filter:
    df = df[df['ENDANGERED'] == True]

# Show table
st.dataframe(df)

# Stats
st.markdown("### UNESCO Listed Count")
st.write(df["UNESCO_LISTED"].value_counts())

# Close connection
cur.close()
conn.close()
