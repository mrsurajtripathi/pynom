from flask import Flask
from flask import render_template, abort, redirect, url_for
from flask import request
from flask import session
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

roles=('Admin','Viewer')

# adding user for static login dictionary has been created down
user_dict={}
user_dict['amit@mail.com']={id:1,"name":"Amit","password":"mypass"}
user_dict['suraj@mail.com']={id:2,"name":"Suraj","password":"pass2"}
user_dict['amit@mail.com']['role']=roles[1]
user_dict['suraj@mail.com']['role']=roles[0]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def hello(name=None):
    print(session)
    if 'user' in session:
        name=session["user"]['name']
    return render_template('admin/dashboard.html', person=name)

@app.route('/login',methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email']:
            if (isvalid(request.form['email'],request.form['password'])):
                session['user'] = user_dict[request.form['email']]
                return redirect(url_for('hello'))
            else:
                error='Invalid Username or password'
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/test')
def test_page():
    print(user_dict)
    return ''

def isvalid(username,password): 
    dictU=user_dict[username]
    dictP = user_dict[username]['password']
    print(f"{username==dictU} {password==dictP} {user_dict[username]} {user_dict[username]['password']}")
    if (username in user_dict and password == dictP):
        return True
    else:
        return False
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('login'))


