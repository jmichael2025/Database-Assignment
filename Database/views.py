from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('login.html')
@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return "Username or email already exists. Please choose a different one."

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template('register.html')

@views.route('/users')
def users():

    users = User.query.all()

    output=""
    for user in users:
        output += f"Username: {user.username}, Email: {user.email}<br>"

    return output

@views.route('/account')
def account():
    return render_template('account.html')

@views.route('/edit')
def edit():
    return render_template('edit.html')

@views.route('/create')
def create():
    return render_template('create.html')

