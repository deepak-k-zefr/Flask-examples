# First we imported the Flask class. 
# An instance of this class will be our WSGI application.
from flask import Flask

# Next we create an instance of this class. The first argument is the name of the application’s module or package. 
# If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different 
# ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on

app=Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')

# The function is given a name which is also used to generate URLs for that particular function, 
# and returns the message we want to display in the user’s browser.

def hello_world():
    return 'Hello, World!'


# $ export FLASK_APP=hello.py
# $ flask run
#  * Running on http://127.0.0.1:5000/


## Returing a String
from flask import jsonify	
@app.route("/<name>")
def hello(name):
	return "Name is %s" % name

## Returning an Int:
@app.route("/<int:age>")
def age(age):
   return "age is %d" % age

## Jsonify a Dictionary
import  datetime
today = datetime.date.today()
@app.route("/time")
def time():
	return jsonify({"Now the Time is":today})

if __name__ == '__main__':
	app.run(debug=True)
	main()