from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB_LISTINGS = [
  {
    'id':1,
    'title':"Data Analyst",
    'location':"Pune, India",
    'salary':"Rs. 10,00,000"
  },
  {
    'id':2,
    'title':"Data Engineer",
    'location':"Ontario, Canada",
    'salary':"$ 1,00,000"
  },
  {
    'id':3,
    'title':"Full Stack Developer",
    'location':"Hong Kong, Japan",
    'salary':"JPY 1,50,000"
  },
  {
    'id':4,
    'title':"Quality Assurance",
    'location':"London, UK",
    'salary':"$ 1,20,000"
  },
  {
    'id':5,
    'title':"Data Engineer",
    'location':"Ohio, USA",
    'salary':"$ 1,30,000"
  }
]

@app.route("/") 
def landing_page():
  return render_template("home.html", jobs = JOB_LISTINGS)

@app.route("/api/job_postings")
def api_call():
  return jsonify(JOB_LISTINGS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) 