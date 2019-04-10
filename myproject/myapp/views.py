from flask import render_template
from myapp import app


@app.route('/')
@app.route('/anasayfa')
def index():
    return render_template('index.html')

@app.route('/users')
def users():

    return render_template('users.html')
@app.route('/chat')
def chat():

    return render_template('chat.html')
@app.route('/listeler')
def listeler():

    return render_template('listeler.html')
@app.route('/listeDetay')
def listeDetay():

    return render_template('listeDetay.html')
@app.route('/haberler')
def haberler():

    return render_template('haberler.html')
@app.route('/haberDetay')
def haberDetay():

    return render_template('haberDetay.html')
@app.route('/iletisim')
def iletisim():

    return render_template('iletisim.html')
