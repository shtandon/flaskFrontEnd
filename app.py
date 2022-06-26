from flask import Flask, render_template, request, redirect, url_for
from Orchestrator.Orchestrator import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    username = request.form.get('username')
    password = request.form.get('password')
    Orchestor(username, password)
    return render_template('home.html')

if __name__ == '__main__':
   # Orchestor()
    app.run(debug=True)




