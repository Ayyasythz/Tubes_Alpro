from flask import Blueprint, render_template, request, flash,redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfuly!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again!', category='error')
        else:
            flash('Email does\'t exsist ', category='error')
            
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        fullname = request.form.get('fullname')
        password = request.form.get('password')
        passwordc = request.form.get('passwordc')
        gender = request.form.get('gender')
        
        user = User.query.filter_by(email=email).first()
        usernames = User.query.filter_by(username=username).first()
        if user:
             flash("Email Already exists.", category='error')
        elif usernames:
            flash("Email Already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(username) < 2:
            flash("username must be greater than 1 characters.",category='error')
        elif len(fullname) < 2:
            flash("Fullname must be greater than 1 characters.",category='error')
        elif password != passwordc:
            flash("Passwords dont\'t match.", category='error')
        elif len(password) < 8 :
             flash("Password must be at least 8 characters",category='error')
        else:
            new_user = User(email=email, username=username,fullname=fullname,password=generate_password_hash(password, method='sha256'), gender=gender,role="user")
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))
        
    return render_template("register.html")