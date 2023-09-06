from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')



@app.route("/V15l0N")
def vision():
  return render_template('vision.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
