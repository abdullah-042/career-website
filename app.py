from flask import Flask, render_template, jsonify
# from flask module import Flask class

# create an instance of the Flask class
app = Flask(__name__)
# change favicon of the app

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Calgary, AB',
    'salary': 'CAD $80,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Toronto, ON',
    'salary': 'CAD $83,000'
}, {
    'id': 3,
    'title': 'Front-End Developer',
    'location': 'Vancouver, BC',
    'salary': 'CAD $85,000'
}, {
    'id': 4,
    'title': 'Back-End Developer',
    'location': 'Calgary, AB',
    'salary': 'CAD $85,000'
}, {
    'id': 1,
    'title': 'IT Support Specialist',
    'location': 'Ottawa, ON',
    'salary': 'CAD $80,000'
}]


# create a route root
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
