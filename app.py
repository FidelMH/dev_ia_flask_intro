from flask import Flask, render_template,request,jsonify,redirect
from markupsafe import escape
from database import Data

data = Data()


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
    return f"Hello {username}"

@app.get('/age')
def get_age():
    return render_template('age.html')

@app.post('/age')
def post_age():

    return render_template('age.html', age = request.form['age'])

@app.route('/articles')
def articles():
    articles_list = [
        {
            "title": "Les bases de Python",
            "author": "Marie Dupont"
        },
        {
            "title": "Introduction à Flask",
            "author": "Jean Martin"
        },
        {
            "title": "Le Machine Learning pour les débutants",
            "author": "Sophie Lambert"
        },
        {
            "title": "Web Development avec Python",
            "author": "Pierre Durand"
        }
    ]
    
    return render_template("articles.html", articles=articles_list)

@app.route('/api/ping')
def api_ping():
    return jsonify({'ping':'pong'})

@app.post('/users/add')
def add_user():
    username = escape(request.form['username'])
    data.add_user(username)
    return redirect("/users")

@app.get('/users')
def get_users():
    users_list = data.get_users()
    return render_template('users.html', users = users_list )

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/search')
def search():
    q = request.args.get('q','')
    print(q)
    return q


@app.route('/blog')
def blog():
    return render_template('blog.html')