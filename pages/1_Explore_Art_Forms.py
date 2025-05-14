import streamlit as st
import pandas as pd
import snowflake.connector

st.title("🎨 Explore Traditional Art Forms")

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

cur = conn.cursor()
cur.execute("SELECT * FROM ARTS")
df = cur.fetch_pandas_all()

# Filters
region_filter = st.selectbox("Select Region/State", ["All"] + sorted(df['ADDRESS'].unique()))
if region_filter != "All":
    df = df[df['ADDRESS'] == region_filter]

if st.checkbox("Only show endangered art forms"):
    df = df[df['ENDANGERED'] == True]

st.dataframe(df)

st.markdown("### 🏛️ UNESCO Listed Count")
st.bar_chart(df["UNESCO_LISTED"].value_counts())

cur.close()
conn.close()
