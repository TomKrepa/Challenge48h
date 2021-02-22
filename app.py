from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

    def __repr__(self):
        return '<Post "{}">' % self.title

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/posts')
def posts():
    return render_template('posts/index.html')

@app.route('/user')
def user():
    return render_template('pages/user.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5000)