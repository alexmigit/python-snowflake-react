from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
from config.snowflake_config import snowflake_config
from concurrent.futures import ThreadPoolExecutor

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
    try:
        def write_table(table_df):
            table, df = table_df
            write_pandas(conn, df, f"stg_{table}")
        # Use ThreadPoolExecutor to parallelize the writing of DataFrames
        with ThreadPoolExecutor() as executor:
            executor.map(write_table, df_dict.items())
    finally:
        conn.close()
