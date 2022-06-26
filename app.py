from flask import Flask, render_template, request, redirect, url_for
from Orchestrator.Orchestrator import *
app = Flask(__name__)

@app.route('/')
def home():
   
    return render_template('home.html')
@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    a = Orchestor(username, password)
   # if a==1:
    #     return redirect(url_for('success'))
    #else:
     #    return redirect(url_for('failur'))
  #  return (username, password)
    return render_template('login.html')
   # Orchestor(questions)
    
@app.route('/success')
def success():
    return "Mails moved to folder"

@app.route('/failure')
def failur():
    return "Wrong userid password"


if __name__ == '__main__':
   # Orchestor()
    app.run(debug=True)




