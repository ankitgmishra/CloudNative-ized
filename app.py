
# from flask_login import login_required

# from auth import init_auth,login_required

from flask import Flask, jsonify, request, render_template
from auth import login_manager,login_required

from auth import auth

from api import api,limiter

import os 



app = Flask(__name__)


login_manager.init_app(app)

app.secret_key = os.urandom(24) 
limiter.init_app(app)



# Register 
app.register_blueprint(auth)
app.register_blueprint(api)


# login_manager = init_auth(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
       return render_template('documentation.html')

@app.route('/ipl-api-documentation')
def iplDocumentation():
       return render_template('iplapi_documentation.html')
@app.route('/news-api-documentation')
def newsDocumentation():
       return render_template('news_apiDocumentation.html')


# @app.route('/dashboard')
# @login_required
# def dashboard():
#        api_key = session.get('api_key')
#        return render_template('dashboard.html')






    
@login_manager.unauthorized_handler
def unauthorized():
    return "Login Required"



# app.run(debug=True)
