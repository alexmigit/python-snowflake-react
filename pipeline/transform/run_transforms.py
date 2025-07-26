from config.snowflake_config import snowflake_config
import snowflake.connector

# Function to run SQL files
def run_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
    conn = snowflake.connector.connect(**snowflake_config)
    cs = conn.cursor()
    cs.execute(sql)
    cs.close()
    conn.close()

# Function to run all transformations
def run_all_transforms():
    # Create dimension tables
    run_sql_file('transform/sql/create_dim_tables.sql')
    # Create fact table
    run_sql_file('transform/sql/create_fact_table.sql')
