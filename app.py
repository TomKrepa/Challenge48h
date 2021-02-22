from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/user')
def user():
    return render_template('pages/user.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)