
from flask import Blueprint, redirect, render_template,request, jsonify,render_template,session,request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from tinydb import TinyDB, Query
import os

import ipl
from keyGeneration import generate_api_key,save_api_key
from tinydb import where

from api import limiter
from flask_limiter.util import get_remote_address

auth = Blueprint('auth', __name__)

# auth.secret_key = os.urandom(24) 
# global login_manager
login_manager = LoginManager(auth)

login_manager.login_view = 'login'

db = TinyDB('users.json')

class User(UserMixin):
    pass




def init_auth(auth):
    login_manager.init_auth(auth)
    return login_manager

# @auth.route("/loginpage")
# def loginpage():
#     return render_template("login.html")

@auth.route("/registerpage")
def registerPage():
    return render_template("register.html")


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))



@auth.route('/register', methods=['POST'])
def register():

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        fullname = data.get('fullname')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Check if the username already exists
        if db.search(Query().username == username):
            return jsonify({'error': 'Username already exists'}), 400

        # In a real-world scenario, you would hash and salt the password
        user_id = len(db)
        rate_limit_day = 24
        rate_limit_hour = 4
        db.insert({'id': user_id, 'fullname':fullname,'email':email, 'username': username, 'password': password,'rate_limit_hour':rate_limit_hour,'rate_limit_day':rate_limit_day})
        api_key = generate_api_key()
        save_api_key(user_id, api_key)

        return jsonify({'message': 'Registration successful'}), 201


@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method == "POST":
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = db.get((Query().username == username) & (Query().password == password))

        if user:
            # user_obj = User()
            # user_obj.id = user['id']
            user_obj = User()
            user_obj.id = user['id']
            user_obj.username = user['username']
            user_obj.api_key= user['api_key']  
        
            user_obj.rate_limit_hour= user['rate_limit_hour']  
            user_obj.rate_limit_day= user['rate_limit_day'] 
            login_user(user_obj)

            session['api_key'] = user['api_key']
            session['rate_limit_hour'] = user['rate_limit_hour']
            session['rate_limit_day']  = user['rate_limit_day'] 
            
            print("----User Logged In------API Key here : ",session['api_key'] )
            # login_user(user_obj)
            return jsonify({'message': 'Login successful'}), 200
    
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        if current_user.is_authenticated:
            return redirect(url_for('auth.dashboard'))  # Redirect to dashboard if user is already logged in
        return render_template("login.html")
    
      

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
    # return jsonify({'message': 'Logout successful'}), 200


@login_manager.unauthorized_handler
def unauthorized():
    return "Login Required"

@auth.route('/protected')
@login_required
def protected():
    return jsonify({'message': f'Hello, {current_user.id}! This is a protected resource.'})


@auth.route('/dashboard')
# @login_required
def dashboard():
    if current_user.is_anonymous:
        return redirect(url_for('auth.login'))
    user_id = current_user.get_id()  # Assuming you are using Flask-Login

    # Check if the user has an API key in the session
    if 'api_key' not in session:
        # If not, generate a new API key and save it for the user
        api_key = generate_api_key()
        save_api_key(user_id, api_key)

        # Store the API key in the session
        session['api_key'] = api_key

        session["rate_limit_day"] = rate_limit_day
        session["rate_limit_hour"] = rate_limit_hour

       
    else:
        # If the API key is already in the session, use it
        api_key = session['api_key']
        rate_limit_hour = session["rate_limit_hour"] 
        rate_limit_day = session["rate_limit_day"]






    return render_template('dashboard.html', api_key=api_key,remaining_request_for_day=rate_limit_day, remaining_request_for_hour=rate_limit_hour)