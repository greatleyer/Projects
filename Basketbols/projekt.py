from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'tarasdayn123'
app.config['UPLOAD_FOLDER'] = 'static/files'
@app.route("/")
def home():
    return render_template('main.html')

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/players")
def players():
    return render_template("players.html")

@app.route("/bronza")
def bronza():
    return render_template("bronza.html")

@app.route("/abl")
def abl():
    return render_template("abl.html")

@app.route("/altliga")
def altliga():
    return render_template("altliga.html")

@app.route("/u13")
def u13():
    return render_template("u13.html")

@app.route("/u19")
def u19():
    return render_template("u19.html")


if __name__ == "__main__":
    app.run(debug = True)