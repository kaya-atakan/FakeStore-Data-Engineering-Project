import requests
import psycopg2
import os

# Get the path to the .env file manually
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
env_file_path = os.path.join(parent_directory, '.env')

# Fetch data from the FakeStore API
url = 'https://fakestoreapi.com/products'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print('Failed to fetch data:', response.status_code)

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

# Iterate through fetched data and insert into PostgreSQL 'products' table
for product in data:
    rating = product['rating']
    cur.execute("""
        INSERT INTO products (id, title, price, description, category, image, rating_rate, rating_count)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        product['id'],
        product['title'],
        product['price'],
        product['description'],
        product['category'],
        product['image'],
        rating['rate'],
        rating['count']
    ))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
