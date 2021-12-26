from flask import Flask, abort
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Suren!!!'

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

## Debugging A Flask Application
@app.route('/users/<int:user_id>/')
def user(user_id):
    users = ['Dhanush', 'sergio', 'surendar']
    try:
        return '<h2>Helloo {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)