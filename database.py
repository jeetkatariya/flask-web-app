from sqlalchemy import create_engine, text
import urllib.parse
import os

# Original password
original_password = os.environ['DB_PASSWORD']

# Encode the password part if it contains special characters
encoded_password = urllib.parse.quote_plus(original_password)

db_user = os.environ['DB_USER']
# Correctly formatted connection string with the encoded password
connection_string = f'postgresql+psycopg2://{db_user}:{encoded_password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

# Print the connection string to verify
print(connection_string)

# Create the engine
engine = create_engine(connection_string)

# Initialize jobs as an empty list in case of failure
jobs = []

# Try to connect and execute a query
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM iu_jobs"))

        # Convert rows to dictionaries
        jobs = [dict(row) for row in result.mappings()]
except Exception as e:
    print(f"Error: {e}")

# Print jobs to verify the output
print(jobs)
