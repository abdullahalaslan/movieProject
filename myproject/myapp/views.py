from flask import render_template
from myapp import app


@app.route('/')
@app.route('/anasayfa')
def index():
    return render_template('index.html',title='AnaSayfa')

    
@app.route('/users')
def users():
    kullanicilar =[
        {'name':'Abdullah','title':'Web Developer'},
        {'name':'Kazım','title':'Android Developer'},
        {'name':'Murat','title':'Devops Developer'},
    ]
    return render_template('users.html',title='Kullanicilar Listesi',users=kullanicilar)
