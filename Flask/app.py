from flask import Flask, render_template, url_for, flash, redirect
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


'''@app.route('/Register', methods=('GET', 'POST'))
def register():#Yaha se dekh
    form = registerForm()
    print("InputFucntion")
    if form.validate_on_submit():
        print("InputValidate")
        flash(f'Account Created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)'''


#@app.route("/Register", methods=['GET', 'POST'])
@app.route('/Register', methods=('GET', 'POST'))
def register():
    form = registerForm()
    print("FunctionCall")
    if form.validate_on_submit():
        print("VAlidateCall")
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',  form=form)

@app.route('/login')
def login():
    form = loginForm()
    return render_template('Login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
