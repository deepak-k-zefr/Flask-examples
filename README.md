Some Simple  Flask Examples

( Inspired from https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)


## Designing a simple web service

The task of designing a web service or API that adheres to the REST guidelines then becomes an exercise in identifying the resources that will be exposed and how they will be affected by the different request methods.


In this example we are building a simple payroll application that stores information of different employees.

The first thing to do is to decide what is the root URL to access this service. For example, we could expose this service as:

```
http://[hostname]/payroll/api/v1.0/
```

Here I have decided to include the name of the application and the version of the API in the URL. Including the application name in the URL is useful to provide a namespace that separates this service from others that can be running on the same system. Including the version in the URL can help with making updates in the future, since new and potentially incompatible functions can be added under a new version, without affecting applications that rely on the older functions.

The next step is to select the resources that will be exposed by this service. This is an extremely simple application, we only have tasks, so our only resource will be the tasks in our to do list.

Our tasks resource will use HTTP methods as follows:


| HTTP Method  |   URI                 | Action |
|--------------|:----------------------|:-----|
|GET	|http://[hostname]/payroll/api/v1.0/tasks	|Retrieve list of tasks|
|GET	|http://[hostname]/payroll/api/v1.0/tasks/[task_id]	|Retrieve a task|
|POST	|http://[hostname]/payroll/api/v1.0/tasks	|Create a new task|
|PUT	|http://[hostname]/payroll/api/v1.0/tasks/[task_id]	|Update an existing task|
|DELETE|	http://[hostname]/payroll/api/v1.0/tasks/[task_id]	|Delete a task|


We can define a task as having the following fields:
**employee-name**: unique identifier for tasks.String type.
**department**:  String type.
**designation**:  Text type.
**age** Numeric type.


Let's begin by installing Flask in a virtual environment. If you don't have virtualenv installed in your system, you can download it from https://pypi.python.org/pypi/virtualenv.


```
$ mkdir payroll
$ cd payroll-api
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```

Now that we have Flask installed let's create a simple web application, which we will put in a file called app.py:

```
#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

```


To run this application we have to execute app.py:

```
python app.py
```

### Implementing RESTful services in Python and Flask
The clients of our web service will be asking the service to add, remove and modify details about employees, so clearly we need to have a way to store these details. The obvious way to do that is to build a small database, here we use a list of dictionaries instead.


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


http://127.0.0.1:5000/payroll/api/v1.0/employees

RESPONSE:
```{
  "employees": [
    {
      "age": 64, 
      "department": "Finance", 
      "designation": "Economist", 
      "name": "John Adams"
    }, 
    {
      "age": 63, 
      "department": "Research", 
      "designation": "Scientist", 
      "name": "Geoff Hinton"
    }
  ]
}```

```curl -i http://127.0.0.1:5000/payroll/api/v1.0/employees
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 278
Server: Werkzeug/0.11.15 Python/3.6.1
Date: Sat, 06 Jan 2018 06:08:20 GMT

{
  "employees": [
    {
      "age": 64, 
      "department": "Finance", 
      "designation": "Economist", 
      "name": "John Adams"
    }, 
    {
      "age": 63, 
      "department": "Research", 
      "designation": "Scientist", 
      "name": "Geoff Hinton"
    }
  ]
}```

Retrieve data of an entry based on the ID of the entry.
```
curl -i http://127.0.0.1:5000/payroll/api/v1.0/employees/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 143
Server: Werkzeug/0.11.15 Python/3.6.1
Date: Sat, 06 Jan 2018 06:25:11 GMT


When we ask for resource id #2 we get it, but when we ask for #3 we get back the 404 error. Below is a method to handle the error gracefully:

```
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
 ```
{
  "employees": {
    "age": 64, 
    "department": "Finance", 
    "designation": "Economist", 
    "id": 1, 
    "name": "John Adams"
  }
}
```

Next in our list is the POST method, which we will use to insert a new item in our task database:

Adding a new employee is also pretty easy. The request.json will have the request data, but only if it came marked as JSON. If the data isn't there, or if it is there, but we are missing a name item then we return an error code 400, which is the code for the bad request.


```@app.route('/payroll/api/v1.0/employees/', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    employee = {
        'id': employees[-1]['id'] + 1,
        'name': request.json['name'],
        'designation': request.json.get('designation', ""),
        'department': request.json.get('department', "")
    }
    employees.append(employee)
    return jsonify({'employee': employee}), 201```
    
We then create a new employee dictionary, using the id of the last task plus one (a cheap way to guarantee unique ids in our simple database). We tolerate a missing description field, and we assume the done field will always start set to False.

We append the new task to our tasks array, and then respond to the client with the added task and send back a status code 201, which HTTP defines as the code for "Created".

To test this new function we can use the following curl command:


```curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Nikola Tesla","department":"physics"}' http://127.0.0.1:5000/payroll/api/v1.0/employees/
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 119
Server: Werkzeug/0.11.15 Python/3.6.1
Date: Sat, 06 Jan 2018 06:42:11 GMT

{
  "employee": {
    "department": "physics", 
    "designation": "", 
    "id": 4, 
    "name": "Nikola Tesla"
  }
}
```
After this request completed we can obtain the updated list of employees:
```
curl -i http://127.0.0.1:5000/payroll/api/v1.0/employees
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 501
Server: Werkzeug/0.11.15 Python/3.6.1
Date: Sat, 06 Jan 2018 06:45:49 GMT

{
  "employees": [
    {
      "department": "Finance", 
      "designation": "Economist", 
      "id": 1, 
      "name": "John Adams"
    }, 
    {
      "department": "Research", 
      "designation": "Scientist", 
      "id": 2, 
      "name": "Geoff Hinton"
    }, 
    {
      "department": "", 
      "designation": "", 
      "id": 3, 
      "name": "Nikola Tesla"
    }, 
    {
      "department": "physics", 
      "designation": "", 
      "id": 4, 
      "name": "Nikola Tesla"
    }
  ]
}
```
