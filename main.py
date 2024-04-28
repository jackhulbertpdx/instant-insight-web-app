# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from STG_POOLS;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.POOL_NAME} has a :{row.POOL_NAME}:")