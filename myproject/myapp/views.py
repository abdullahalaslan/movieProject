from flask import render_template
from myapp import app


@app.route('/')
@app.route('/anasayfa')
def index():
    return render_template('index.html')

@app.route('/users')
def users():

    return render_template('users.html')
