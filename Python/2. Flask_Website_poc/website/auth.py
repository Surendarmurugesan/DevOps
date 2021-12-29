from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="DevOps-tools")

@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route("/sign-up/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('Firstname must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Password doesn\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            #Add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")