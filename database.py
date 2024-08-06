from sqlalchemy import create_engine, text
import urllib.parse
import os

original_password = os.environ['DB_PASSWORD']
encoded_password = urllib.parse.quote_plus(original_password)

db_user = os.environ['DB_USER']
connection_string = f'postgresql+psycopg2://{db_user}:{encoded_password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

print(connection_string)

engine = create_engine(connection_string)

jobs = []
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM iu_jobs"))

        jobs = [dict(row) for row in result.mappings()]
except Exception as e:
    print(f"Error: {e}")
  
print(jobs)
