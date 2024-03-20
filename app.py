from flask import Flask, render_template
# from flask module import Flask class

# create an instance of the Flask class
app = Flask(__name__)
# change favicon of the app

# create a route
@app.route('/')
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
