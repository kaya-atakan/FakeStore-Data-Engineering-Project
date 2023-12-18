import requests
import psycopg2
import os

url = 'https://fakestoreapi.com/carts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process data (store in a variable or convert to CSV)
else:
    print('Failed to fetch data:', response.status_code)


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

# Iterate through your fetched data and insert into PostgreSQL
for row in data:
    for product in row['products']:
        cur.execute("""
            INSERT INTO carts (userid, date, productId, quantity)
            VALUES (%s, %s, %s, %s)
        """, (row['userId'], row['date'], product['productId'], product['quantity']))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()