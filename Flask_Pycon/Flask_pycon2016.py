from flask import Flask
app=Flask(__name__)

## GET  Requests

### Step 1: Hello
@app.route("/")
def hello():
	return "Hello World"




### Step 2: JSON
from flask import jsonify

@app.route("/json")
def helloJson():
	return jsonify({"Message":"Helo World"})


### Step 3: JSON puppy
@app.route("/puppy")
def puppy():
    puppy={"name":"Rover",
	        "Image-URL":"http://example.com/rover.jpg"}
    return jsonify(puppy)


### POST Requests
#Step 5: Multiple Puppies
PUPPIES = [
    {
        "name": "Rover",
        "image_url": "http://example.com/rover.jpg",
    },
    {
        "name": "Spot",
        "image_url": "http://example.com/spot.jpg",
    },
]

@app.route("/<int:index>")
def get_puppy(index):
	try:
		puppy=PUPPIES[index]
	except IndexError:
		abort(404)
	return jsonify(puppy)



if __name__ == '__main__':
	app.run(debug=True)

