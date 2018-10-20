from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from config import url
from form import Npo_form

app = Flask(__name__)
app.config['SECRET_KEY'] = "NPOST.ME"
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Npo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    seeking = db.Column(db.String(50), nullable=False)
    contributors = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'

@app.route('/', methods=["GET", "POST"])
def index():
    form = Npo_form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        website = form.website.data
        description = form.description.data
        seeking = form.seeking.data
        contributors = form.contributors.data
        company = Npo(name=name, email=email, description=description, seeking=seeking, contributors=contributors, website=website)
        db.session.add(company)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

@app.route('/donor')
def donor():
    return render_template('donor.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

@app.route('/company')
def company():
    return render_template('company.html')

if __name__ == "__main__":
    app.run()

