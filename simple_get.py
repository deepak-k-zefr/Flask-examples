from flask import Flask
app=Flask(__name__)

## GET  Requests

### Step 1: Hello

@app.route("/")
def hello():
	return(jsonify({"Hello":"Deepak"}))

if __name__ == '__main__':
	app.run(debug=True)
	main()
