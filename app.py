import os
import snowflake.connector
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Snowflake using environment variables
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

# Execute a query to get the Snowflake version
cursor = conn.cursor()
cursor.execute("SELECT CURRENT_VERSION()")
version = cursor.fetchone()
print(f"Snowflake version: {version[0]}")

# Streamlit UI setup
st.title('Snowflake Streamlit POC')

# Query Snowflake and display results
st.write("Fetching data from Snowflake...")

cursor.execute("SELECT * FROM users LIMIT 10")
data = cursor.fetchall()

# Display data in Streamlit
st.write(data)

# Close the cursor and connection
cursor.close()
conn.close()
