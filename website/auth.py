from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from time import sleep

auth = Blueprint('auth', __name__)

@auth.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        return
    else:
        return render_template('books.html')

@auth.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        # login_user(user)
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                sleep(2)
                return redirect(url_for('views.index'))
            else:
                flash("Incorrect password. Please try again.", category='error')
                return redirect(url_for('auth.login'))
        else:
            flash("Email does not exist. Please try again.", category='error')
            return redirect(url_for('auth.login'))

    else:
        return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email is already associated with an account. Please log in.', category='error')
            return redirect(url_for('auth.register'))

        else:
            if len(email) < 4:
                flash('Email must be greater than 3 characters', category='error')
                return redirect(url_for('auth.register'))

            elif len(firstname) < 2:
                flash('First name must have a minimum of 2 characters', category='error')
                return redirect(url_for('auth.register'))
            elif password != confirm:
                flash('Passwords do not match. Try again.', category='error')
                return redirect(url_for('auth.register'))
            elif len(password) < 8:
                flash('Password must have a minimum of 8 characters.', category='error')
                return redirect(url_for('auth.register'))

            else:
                new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password, method='sha256'))
                flash('Account created.', category='success')
                sleep(3)
                # new_user = User.query.filter_by(email=email).first()
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('views.index'))
    else:
        return render_template('register.html', user=current_user)

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    sleep(2)
    return redirect(url_for('auth.login'))

