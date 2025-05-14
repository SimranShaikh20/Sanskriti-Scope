import streamlit as st
import snowflake.connector
import pandas as pd
import altair as alt

st.title("📊 Tourism Trends & Seasonality")

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
cur.execute("SELECT * FROM TOURISM_TRENDS")
df = cur.fetch_pandas_all()

# Show seasonal trend
st.markdown("### 📅 Tourist Arrivals by Month")
line_chart = alt.Chart(df).mark_line().encode(
    x='MONTH',
    y='TOURISTS',
    color='STATE'
).interactive()
st.altair_chart(line_chart, use_container_width=True)

# Least visited states
st.markdown("### 📍 Underexplored States")
least_visited = df.groupby('STATE')['TOURISTS'].sum().nsmallest(5).reset_index()
st.bar_chart(least_visited.set_index("STATE"))

cur.close()
conn.close()
