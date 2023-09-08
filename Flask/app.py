from flask import Flask, render_template, url_for
from forms import registerForm, loginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f84055293d020b8aa518054d42fc1e8f'
posts = [
        {
        'author':'Krushang',
        'Title':'AutoBiography',
        'content':'FirstPostContent',
        'date':'21 September'
        },
        {
        'author':'Palky',
        'Title':'Nahane Jaa',
        'content':'Variyali',
        'date':'28 September'
        }
    ]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
@app.route('/about')
def about():
    return render_template('about.html', posts=posts)
@app.route('/Register')
def register():
    form = registerForm()
    return render_template('register.html', form=form)
@app.route('/login')
def login():
    form = loginForm()
    return render_template('Login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
