from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donor')
def donor():
    return render_template('donor.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

if __name__ == "__main__":
    app.run()
