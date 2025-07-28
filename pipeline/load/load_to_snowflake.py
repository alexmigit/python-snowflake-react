from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
from config.snowflake_config import snowflake_config

# Function to get a Snowflake connection
# This function uses the snowflake_config dictionary to establish a connection
def get_conn():
    conn = snowflake.connector.connect(
        **snowflake_config
    )
    return conn

# Function to load data into Snowflake
# This function takes a dictionary of DataFrames and writes them to Snowflake
# Each DataFrame is written to a staging table with the prefix 'stg_'
def load_to_snowflake(df_dict):
    conn = get_conn()
    for table, df in df_dict.items():
        write_pandas(conn, df, f"stg_{table}")
    conn.close()
