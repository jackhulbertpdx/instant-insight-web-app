# streamlit_app.py

import streamlit as st
import os

# Everything is accessible via the st.secrets dict:
st.write("user:", st.secrets["user"])
st.write("password:", st.secrets["password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["user"] == st.secrets["user"],
)


# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from STG_POOLS;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.POOL_NAME} has a :{row.POOL_NAME}:")
