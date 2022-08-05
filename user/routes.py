from crypt import methods
from flask import Flask
from app import app
from user.models import Hardware, User

@app.route('/user/signup',methods = ['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/signin',methods = ['POST'])
def signin():
    return User().signin()

@app.route('/dashboard/checkout',methods = ['POST'])
def checkout():
    return Hardware().checkout()

@app.route('/dashboard/checkin',methods = ['POST'])
def checkin():
    return Hardware().checkin()
