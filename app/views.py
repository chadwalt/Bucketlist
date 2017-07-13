
from flask import render_template, request, redirect, url_for

from app import app
from app.application import App

#initializing the app class
login_meth = App()

@app.route('/')
def index():
    return render_template("login/index.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        
        result = login_meth.login(data['username'], data['password'])

        if result:
            return 'User exists'
        else:
            ##return 'User dont exist'
            ## Redirec the user to the signp interface
            return redirect(url_for('signup'))
    #return render_template("login/index.html")

@app.route('/signup')
def signup():
    return render_template("login/signup.html")


@app.route('/create_account',methods = ['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        data = request.form

        #login_meth = App()
        result = login_meth.signup(data['first_name'],data['sur_name'],data['username'], data['password'], data['email'])

        print(login_meth.users)
        print("This is printig to the file.")
        return 'These are the users.'

        if result:
            return 'User exists'
        else:
            ## Redirec the user to the signp interface
            return redirect(url_for('index'))    

