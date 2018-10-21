
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from config import url
from forms import Npo_form

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="True"
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Npo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
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
    print('<-- index -->')

    if form.validate_on_submit():
        print('<-- form validate -->')
        name = form.name.data
        email = form.email.data
        website = form.website.data
        description = form.description.data
        seeking = form.seeking.data
        contributors = form.contributors.data
        phone = form.phonenumber.data
        company = Npo(name=name, phone=phone, email=email, description=description, seeking=seeking, contributors=contributors, website=website)

        print('company -->', company.__dict__)

        db.session.add(company)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/post')
def donor():
    form = Npo_form()
    return render_template('form.html', form=form)


@app.route('/find')
def company():
    # if the request has a filter
    if request.args.get('seeking'):
        seeking = request.args.get('seeking')
        npos = Npo.query.filter_by(contributors=seeking).all()
        return render_template('company.html', npos=npos)

    # if the request has a filter
    if request.args.get('id'):
        id = request.args.get('id')
        npo = Npo.query.filter_by(id=id).first()
        return render_template('page.html', npo=npo)

    # if the request doesn't have a filter
    npos = Npo.query.all()
    return render_template('company.html', npos=npos)


if __name__ == "__main__":
    app.run()

