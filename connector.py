import snowflake.connector

# Ensure the correct connection parameters
conn = snowflake.connector.connect(
       
    account = "NJRTACQ-FA51430",
    user = "SIMRANSHAIKH20",
    password = "SimranShaikh@20",
    role = "ACCOUNTADMIN",
    warehouse = "COMPUTE_WH",
    database = "CULTURAL_DB",
    schema = "CULTURAL_SCHEMA"
)

# Execute a query to test connection
try:
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    print(cursor.fetchone())
finally:
    cursor.close()
    conn.close()
