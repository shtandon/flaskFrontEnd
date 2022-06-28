from os import access
from flask import * 
from flask import session
#from flask_socketio import SocketIO, emit
#from flask.ext.login import current_user, logout_user
from Orchestrator.Orchestrator import *

from Authentication.auth import Authentication
from DataHandler.datahandler import DataHandler
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/')  
def home():  
   
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    print("==================================")
    auth_obj=Authentication()
    dataHandler_obj= DataHandler()
    orches_obj= Orchestrator()
    error = None;  
    username = request.form.get('username')
    session['username'] = request.form.get('username')
    password = request.form.get('password')
    #Orchestrator(username, password)


    print("In login: ",session['username'])

    acc,frombox,tobox, counter, mailsmoved= orches_obj.Navigate_process(auth_obj,dataHandler_obj,username, password )
    session['acc'] = acc
    session['frombox'] = frombox
    session['tobox'] = tobox
    session['counter'] = counter
    session['mailsmoved'] = mailsmoved

   
  
    if request.method == "POST":  
       

        if(request.form['username']!=acc):
       # if ((request.form['pass'] != 'abc') and (request.form['username'] != 'shruti')) :
            error = "invalid credentials"  
        else:  
            #flash("you are successfuly logged in")  
            
            #return redirect(url_for('home'))  
            return redirect(url_for('results'))  
    return render_template('login.html',error=error)  
  
@app.route('/results')  
def results():  
        print("In results: ",session['username'])
        if 'username' in session:
            print("yess")
            username = session['username']
            
            return render_template("result.html")  
        return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
    print("In logout: ",session['username'])
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))
   #return "logged out"
          
if __name__ == '__main__':  
    app.run(debug = True, port=8000)  