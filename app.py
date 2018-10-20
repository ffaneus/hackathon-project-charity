from flask import Flask, render_template
from forms import Npo_form
app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="True"
@app.route('/',methods=["POST","GET"])
import psycopg2
from config import url
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "NPOST.ME"
app.config['SQLACHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)

class NPO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.name}'

@app.route('/')
def index():
    form=Npo_form()
    return render_template('index.html',form=form)

@app.route('/donor')
def donor():
    return render_template('donor.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

if __name__ == "__main__":
    app.run()
