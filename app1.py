from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime



with open('templates/config.json', 'r') as c:
    params = json.load(c)["params"]

# create the app
app = Flask(__name__)
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
if(params["local_server"]):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['production_uri']

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    img_id = db.Column(db.String(20), nullable=True)
    year = db.Column(db.String(20), nullable=False)
    quote = db.Column(db.String(300), nullable=True)


@app.route('/')
def index():
    return render_template('index.html', params=params)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/achievements')
def achievements():
    return render_template('achievements.html')


@app.route('/members')
def members():
    curr_year = "2023-24"
    Mem = Members.query.filter(Members.year.like(f"{curr_year}%")).all()
    return render_template('members.html', Mem=Mem)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)