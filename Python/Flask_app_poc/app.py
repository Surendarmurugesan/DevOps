from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Suren!!!'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'