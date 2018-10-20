from flask import Flask, render_template
from forms import Npo_form
app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="True"
@app.route('/',methods=["POST","GET"])
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
