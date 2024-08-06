# from flask import Flask, render_template, jsonify
# from database import engine
# from sqlalchemy import text

# app=Flask(__name__)

# # JOB_LISTINGS = [
# #   {
# #     'id':1,
# #     'title':"Data Analyst",
# #     'location':"Pune, India",
# #     'salary':"Rs. 10,00,000"
# #   },
# #   {
# #     'id':2,
# #     'title':"Data Engineer",
# #     'location':"Ontario, Canada",
# #     'salary':"$ 1,00,000"
# #   },
# #   {
# #     'id':3,
# #     'title':"Full Stack Developer",
# #     'location':"Hong Kong, Japan",
# #     'salary':"JPY 1,50,000"
# #   },
# #   {
# #     'id':4,
# #     'title':"Quality Assurance",
# #     'location':"London, UK",
# #     'salary':"$ 1,20,000"
# #   },
# #   {
# #     'id':5,
# #     'title':"Data Engineer",
# #     'location':"Ohio, USA",
# #     'salary':"$ 1,30,000"
# #   }
# # ]

# def get_jobs():
#   original_password = 'Nishan@1609#'
#   encoded_password = urllib.parse.quote_plus(original_password)
#   connection_string = f'postgresql+psycopg2://postgres.kzlspmlggperqjtjkkzw:{encoded_password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

#   engine = sqlalchemy.create_engine(connection_string)
#   jobs = []

#   try:
#       with engine.connect() as conn:
#           result = conn.execute(sqlalchemy.text("SELECT * FROM iu_jobs"))
#           jobs = [dict(row) for row in result.mappings()]
#   except Exception as e:
#       print(f"Error: {e}")

#   return jobs

# @app.route("/") 
# def landing_page():
#   jobs = get_jobs()
#   return render_template("home.html", jobs = jobs)

# # @app.route("/api/job_postings")
# # def api_call():
# #   return jsonify(JOB_LISTINGS)

# if __name__ == "__main__":
#   app.run(host="0.0.0.0", debug=True) 

# app.py
from flask import Flask, render_template, jsonify 
import sqlalchemy
import urllib.parse
import os

app = Flask(__name__)

def get_jobs():
    original_password = os.environ['DB_PASSWORD']
    encoded_password = urllib.parse.quote_plus(original_password)

    db_user = os.environ['DB_USER']
    connection_string = f'postgresql+psycopg2://{db_user}:{encoded_password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

    engine = sqlalchemy.create_engine(connection_string)
    jobs = []

    try:
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text("SELECT * FROM iu_jobs"))
            jobs = [dict(row) for row in result.mappings()]
    except Exception as e:
        print(f"Error: {e}")

    return jobs

def get_job(id):
  original_password = os.environ['DB_PASSWORD']
  encoded_password = urllib.parse.quote_plus(original_password)

  db_user = os.environ['DB_USER']
  connection_string = f'postgresql+psycopg2://{db_user}:{encoded_password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres'

  engine = sqlalchemy.create_engine(connection_string)
  
  with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM iu_jobs WHERE id = :id"), {"id": id})

  rows = result.mappings().all()
  if len(rows) == 0:
    return None
  else:
    return dict(rows[0])

@app.route('/')
def landing_page():
    jobs = get_jobs()
    return render_template("home.html", jobs=jobs)

@app.route("/api/job_postings")
def api_call():
  jobs = get_jobs()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = get_job(id)

  if not job:
    return "Not Found", 404
    
  return render_template("jobpage.html", job=job)

if __name__ == '__main__':
    app.run(debug=True)
