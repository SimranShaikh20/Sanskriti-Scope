import streamlit as st
import snowflake.connector
import pandas as pd

st.title("📂 Data Explorer & Download")

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

# Select Table
table = st.selectbox("Choose table to view:", ["ARTS", "TOURISM_TRENDS"])
cur.execute(f"SELECT * FROM {table}")
df = cur.fetch_pandas_all()

st.dataframe(df)
st.download_button("Download CSV", df.to_csv(index=False), f"{table}.csv", "text/csv")

cur.close()
conn.close()
