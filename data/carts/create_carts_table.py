import psycopg2
import os

# Get the path to the .env file manually
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
env_file_path = os.path.join(parent_directory, '.env')

# Read the .env file
with open(env_file_path) as f:
    env_vars = {line.strip().split('=')[0]: line.strip().split('=')[1] for line in f}

# Establish connection
conn = psycopg2.connect(
    dbname=env_vars['DB_NAME'],
    user=env_vars['DB_USER'],
    password=env_vars['DB_PASSWORD'],
    host=env_vars['DB_HOST'],
    port=env_vars['DB_PORT']
)

# Create a cursor object using the connection
cur = conn.cursor()

# SQL command to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS carts (
    id SERIAL PRIMARY KEY,
    userid INTEGER,
    date TIMESTAMP,
    productId INTEGER,
    quantity INTEGER
);
'''

# Execute the SQL command to create the table
cur.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()