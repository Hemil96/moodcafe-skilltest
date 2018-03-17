# Import libraries
from flask import Flask, request, render_template, redirect
import dbconnect
import json

app = Flask(__name__)

# Routing
@app.route('/', methods=['POST', 'GET'])
def authenticate():

    if request.method == 'GET': # handling GET request
        try:
            data = dbconnect.authenticate.fetch_all()
            return render_template('index.html',data = data)
        except:
            return render_template('index.html')
        
    elif request.method == 'POST': # handling POST request
        username = request.form['username'] # getting username from user 
        email = request.form['email'] # getting email from user
        dbconnect.authenticate.intertData(username,email)
        try:
            data = dbconnect.authenticate.fetch_all()
            return render_template('index.html',data = data)
        except:
            return render_template('index.html')
        

if __name__ == "__main__":
    app.run(debug=True)

        