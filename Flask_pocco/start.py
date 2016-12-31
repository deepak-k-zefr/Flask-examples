
from flask import Flask

app=Flask(__name__)


@app.route("/")

def helloWorld():
	return("Hello world")



### GET Requests


@app.route("/random")
def random():
    return "Random Output"

@app.route("/getRequest")
def get():
    return "This is a get request"

import datetime
@app.route("/time")
def time():
    return str(datetime.datetime.now())


# 4.3.1 Variable Rules
# To add variable parts to a URL you can mark these special sections as
# <variable_name>. Such a part is then passed as a keyword argument to
# your function. Optionally a converter can be used by specifying a rule with
# <converter:variable_name>. Here are some nice examples:


### POST Requests
@app.route('/pokemon/<pokemon_name>')
def show_user_profile(pokemon_name):
# show the user profile for that user
	return 'The name of the pokemon is %s' % pokemon_name


@app.route('/pokemonStrength/<int:strength>')
def pokemon_id(strength):
	return"Pokemon Strength is %d" % strength


@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

# The following converters exist:
# int accepts integers
# float like int but for floating point values
# path like the default but also accepts slashes


### POST requests
@app.route("/postRequest/<int:post_id>")
def post(post_id):
    return "This is a post request with POST_ID: %d" % post_id



@app.route("/FavNum/<float:num>")
def string(num):
    return "My Favotite Number is %f" % num



# Unique URLs / Redirection Behavior
# Flask’s URL rules are based on Werkzeug’s routing module. The idea behind that
# module is to ensure beautiful and unique URLs based on precedents laid down by
# Apache and earlier HTTP servers.
# Take these two rules:

@app.route("/about")
def about():
	return " Trying to illustate type of URLs supported by Flask Type I"

@app.route("/projects/")
def projects():
	return " Trying to illustate type of URLs supported by Flask Type II"




# 4.3.2 URL Building
# If it can match URLs, can Flask also generate them? Of course it can. To build a URL
# to a specific function you can use the url_for() function. It accepts the name of the
# function as first argument and a number of keyword arguments, each corresponding
# to the variable part of the URL rule. Unknown variable parts are appended to the URL
# as query parameters. Here are some examples:



# from flask import Flask, url_for
# @app.route('/')
# def index(): pass

# @app.route('/login')
# def login(): pass

# @app.route('/user/<username>')
# def profile(username): pass

# with app.test_request_context():
#     print (url_for('index'))
#     print (url_for('login'))
#     print (url_for('login', next='/'))
#     print (url_for('profile', username='John Doe'))



# 4.3.3 HTTP Methods
# HTTP (the protocol web applications are speaking) knows different methods for accessing
# URLs. By default, a route only answers to GET requests, but that can be
# changed by providing the methods argument to the route() decorator. Here are some
# examples:

@app.route("/login",methods=['GET','POST'])
def login():
    if request.methods=="POST":
        do_the_login()
    else:
        show_the_login_form()

	



# The HTTP method (also often called “the verb”) tells the server what the clients wants
# to do with the requested page. The following methods are very common:
# GET The browser tells the server to just get the information stored on that page and
# send it. This is probably the most common method.
# HEAD The browser tells the server to get the information, but it is only interested in
# the headers, not the content of the page. An application is supposed to handle
# that as if a GET request was received but to not deliver the actual content. In
# Flask you don’t have to deal with that at all, the underlying Werkzeug library
# handles that for you.
# POST The browser tells the server that it wants to post some new information to that
# URL and that the server must ensure the data is stored and only stored once.
# This is how HTML forms usually transmit data to the server.
# PUT Similar to POST but the server might trigger the store procedure multiple times
# by overwriting the old values more than once. Now you might be asking why
# this is useful, but there are some good reasons to do it this way. Consider that
# 16
# the connection is lost during transmission: in this situation a system between the
# browser and the server might receive the request safely a second time without
# breaking things. With POST that would not be possible because it must only be
# triggered once.
# DELETE Remove the information at the given location
# if __name__=='__main__':
# 	#app.run()
# 	app.run(host='0.0.0.0') #This tells your operating system to listen on all public IPs.


# 	4.2 Debug Mode
# The run() method is nice to start a local development server, but you would have to
# restart it manually after each change to your code. That is not very nice and Flask can
# do better. If you enable debug support the server will reload itself on code changes,
# and it will also provide you with a helpful debugger if things go wrong.
# There are two ways to enable debugging. Either set that flag on the application object:



## Looks for hello.html intemplates folder
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__=='__main__':
	app.debug = True
	app.run()