from flask import Blueprint
from flask import render_template, redirect, url_for, request, flash
from src.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import scrap_database


from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Invalid username and password')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email_address = request.form.get('email_address')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Email Address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(username=username, password=generate_password_hash(password, method='sha256'), email_address=email_address)

    scrap_database.session.add(new_user)
    scrap_database.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
