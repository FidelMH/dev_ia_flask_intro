from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/contact')
def contact():
    return(
        """
            <h1>Voici un Titre </h1>
            <p>Ceci est un paragraphe de contact. N'hésitez pas à nous joindre pour toute question ou information supplémentaire.</p>
        """
    )

@app.route('/user/<username>')
def user(username):
    return render_template("perso.html",person=username)

