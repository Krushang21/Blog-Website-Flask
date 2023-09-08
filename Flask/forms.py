from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class registerForm(FlaskForm): #inheritFromFlaskForm
    username =  StringField('Username', validators=[DataRequired(), Length(min=4, max=20)]) #Stringfield is imported form wtforms
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirmPassword= PasswordField('confirmPassword', validators=[DataRequired(), EqualTo ('password')])
    submit= SubmitField('SignUp')
    
class loginForm(FlaskForm): #inheritFromFlaskForm
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember= BooleanField('RememberMe')
    submit= SubmitField('Login')
