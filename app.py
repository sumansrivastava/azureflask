from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Welcom! You are here that means you hosted well !!</h1>'

@app.route('/about/')
def about():
    return '<h2>If you are seeing this pages. Conratulations your webapp is routeing fine.</h2>'
