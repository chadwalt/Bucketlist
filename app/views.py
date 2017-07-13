
from flask import render_template, request, redirect, url_for, json, session

from app import app
from app.application import App
from app.model import Users, Bucket

#initializing the app class
login_meth = App()
users_meth = Users()
bucket_meth = Bucket()

@app.route('/')
def index():
    return render_template("login/index.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        
        result = login_meth.login(data['username'], data['password'])

        if result:
            
            ## Move to the dashboard
            return redirect(url_for('dashboard'))
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
        #return data['first_name'] + '' + data['sur_name'] + '' + data['username'] + '' +  data['password'] + '' +  data['email']

        result = login_meth.signup(data['first_name'],data['sur_name'],data['username'], data['password'], data['email'])

        # print(login_meth.users)
        # print("This is printig to the file.")
        # return 'These are the users.'

        #return result

        if result == 'user exists' or result == 'empty fields':
            return redirect(url_for('signup'))
        else:
            ## Redirec the user to the signp interface
            return redirect(url_for('index'))    

@app.route('/dashboard')
def dashboard(): 
    ## Someone has to be logined to view the dashboard
    if 'user_id' not in session:
        return redirect(url_for('signup'))

    bucketlist = users_meth.list_items();
    return render_template("main_app/index.html", buckets = bucketlist)


@app.route('/save_bucket', methods = ['POST', 'GET'])
def save_bucket(): 
    if request.method == 'POST':
        data = request.form
        bucket = data['bucket']
        time = data['time']

    result = users_meth.add_bucket(bucket,time);

    return json.dumps(result)        

@app.route('/bucket_items/<int:id>', methods = ['POST', 'GET'])
def bucket_items(id): 
    if request.method == 'GET':
        ## Someone has to be logined to view the dashboard
        if 'user_id' not in session:
            return redirect(url_for('signup'))

        result = bucket_meth.bucket_items(id)

        return render_template("main_app/bucketListItems.html", items = result)    
