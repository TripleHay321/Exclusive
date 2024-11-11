from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
#Make sure that flask_login and bcrypt are installed
from flask_login import login_user,logout_user,current_user,UserMixin, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'exclusivesite'

class HomeForm(FlaskForm):
    search = StringField(validators = [InputRequired(), Length
    (min=1, max=500)], render_kw={"placeholder": "What are you looking for?"})

    submit = SubmitField("Submit")

@app.route('/')
def home():
    form = HomeForm()
    return render_template('home.html', title='Home', form=form)

@app.route('/login.html')
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)
